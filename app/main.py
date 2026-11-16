from fastapi import FastAPI

app = FastAPI(
    title="PrintShop API", 
    description="Backend for printing company", 
    version="0.1.0"
    )

@app.get("/api/v1/health")
def health_check():
    return { 
        "status": "ok",
        "service": "printshop-api", 
    }

@app.get("/api/v1/products")
def get_products():
    return {
        "id": 1,
        "name": "Визитки",
        "category": "Полиграфия",
}