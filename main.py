from fastapi import FastAPI, Query, Path
from models.product import Product
from router.product import router as product_router

app = FastAPI()


@app.get('/')
def message():
    return "Hola Mundo 123!"


app.include_router(product_router)
