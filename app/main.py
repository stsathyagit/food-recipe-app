from fastapi import FastAPI
from app.routes import recipes

app = FastAPI(title="Food Recipes API")

app.include_router(recipes.router, prefix="/recipes", tags=["recipes"])

@app.get("/")
def root():
    return {"message": "Welcome to the Food Recipes API!"}
