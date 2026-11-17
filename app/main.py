from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Annotated


app = FastAPI(
    title="PrintShop API", 
    description="Backend for printing company", 
    version="0.1.0"
    )

class Product(BaseModel):
    id: int
    name: str
    category: str

class ProductCreate(BaseModel):
    name: str
    category: str


@app.get("/api/v1/health")
def health_check() -> dict:
    return { 
        "status": "ok",
        "service": "printshop-api", 
    }



products_list = [
    {"id": 1, "name": "Визитки", "category": "Полиграфия", "internal_cost": 150},
    {"id": 2, "name": "Листовки", "category": "Полиграфия"},
    {"id": 3, "name": "Буклеты", "category": "Полиграфия"}
]

@app.get("/api/v1/products", response_model=list[Product])
def get_products_list(limit: Annotated[int, Query(ge=1, le=100)] = 10) -> list[dict]:
    return products_list[:limit]

@app.get("/api/v1/products/{product_id}", response_model=Product)
def get_product(product_id: int) -> dict:
    for p in products_list:
        if p["id"] == product_id:
            return p

    raise HTTPException( # Ошибка 404
        status_code=404,
        detail="Product not found"
    )

@app.post("/api/v1/products", status_code=201, response_model=Product)
def create_product(data: ProductCreate):
    new_id = max((product["id"] for product in products_list), default=0) + 1 # генерация нового id (max(id)+1)

    new_product = Product(
        id=new_id, 
        name=data.name, 
        category=data.category
        )
    products_list.append(new_product.model_dump())
    return new_product