from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.config.settings import settings
from app.routers import product_routes
from app.services.product_service import (
    DuplicateProductError,
    InvalidProductIDError,
    ProductNotFoundError,
)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Independent Product Management microservice (in-memory storage).",
)

app.include_router(product_routes.router)


@app.get("/", tags=["Health"])
def health_check():
    return {"service": settings.app_name, "status": "running"}


def error_response(code: int, error: str, message):
    return JSONResponse(status_code=code, content={"error": error, "message": message})


@app.exception_handler(ProductNotFoundError)
async def not_found_handler(request: Request, exc: ProductNotFoundError):
    return error_response(404, "Not Found", str(exc))


@app.exception_handler(InvalidProductIDError)
async def invalid_id_handler(request: Request, exc: InvalidProductIDError):
    return error_response(400, "Bad Request", str(exc))


@app.exception_handler(DuplicateProductError)
async def duplicate_handler(request: Request, exc: DuplicateProductError):
    return error_response(400, "Bad Request", str(exc))


@app.exception_handler(RequestValidationError)
async def validation_handler(request: Request, exc: RequestValidationError):
    details = [
        {"field": ".".join(str(p) for p in err["loc"][1:]), "message": err["msg"]}
        for err in exc.errors()
    ]
    return error_response(422, "Validation Error", details)


@app.exception_handler(Exception)
async def unexpected_handler(request: Request, exc: Exception):
    return error_response(500, "Internal Server Error", "Something went wrong on the server")