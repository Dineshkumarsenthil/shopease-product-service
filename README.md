# ShopEase Product Service

A simple Product Management microservice built with FastAPI and run inside Docker. Products are stored in memory, so the data is lost when the app restarts.

## Technology Stack
- Python 3.11
- FastAPI and Uvicorn
- Pydantic
- Docker
- Swagger UI and Postman for testing
- Git and GitHub

## Project Structure
```
shopease-product-service/
├── app/
│   ├── main.py                 
│   ├── routers/product_routes.py
│   ├── schemas/product_schema.py
│   ├── models/product_model.py
│   ├── services/product_service.py
│   └── config/settings.py
├── screenshots/
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── .env
└── README.md
```

## Installation
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run Locally
```
uvicorn app.main:app --reload --port 8003
```
Open http://localhost:8003/docs

## Run with Docker
```
docker build -t shopease-product-service .
docker run -d --name shopease-product-container -p 8003:8003 shopease-product-service
docker ps
docker logs shopease-product-container
```
Open http://localhost:8003/docs

To stop or remove the container:
```
docker stop shopease-product-container
docker rm -f shopease-product-container
```

## API Endpoints

| Method | Endpoint | Description | Success code |
|---|---|---|---|
| POST | /api/products/ | Create a product | 201 |
| GET | /api/products/ | List products (optional category, skip, limit) | 200 |
| GET | /api/products/{product_id} | Get one product | 200 |
| PUT | /api/products/{product_id} | Update a product | 200 |
| DELETE | /api/products/{product_id} | Delete a product | 204 |

Error codes: 400 invalid request, 404 product not found, 422 validation error, 500 server error.

## Testing
1. Start the container and open http://localhost:8003/docs
2. Use "Try it out" on each endpoint.
3. Test: valid create, empty name, negative price, negative stock, get all, get by ID, invalid ID, update, delete, get deleted product, category filter and pagination.
