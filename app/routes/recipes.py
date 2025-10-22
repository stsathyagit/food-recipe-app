from fastapi import APIRouter, Query
from app.services.ollama_service import generate_recipes

router = APIRouter()

@router.get("/suggest")
def suggest_recipes(
    ingredients: str = Query(..., description="Comma-separated ingredients"),
    meal_type: str = Query("any", description="Meal type: breakfast, lunch, dinner")
):
    recipes = generate_recipes(ingredients, meal_type)
    return {"recipes": recipes}
