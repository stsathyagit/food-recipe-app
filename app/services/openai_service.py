import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_recipe_idea(ingredients: str) -> str:
    prompt = f"Create a unique and delicious recipe using these ingredients: {ingredients}."
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative chef who writes clear recipes."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return completion.choices[0].message.content.strip()
