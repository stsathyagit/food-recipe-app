import ollama

MODEL = "phi3"  # Faster than Mistral for recipe generation

def generate_recipes(ingredients: str, meal_type: str):
    prompt = f"""
    You are a professional chef.
    Create 3 unique {meal_type} recipes using these ingredients: {ingredients}.
    For each recipe, include:
    - Name
    - List of ingredients
    - Short instructions

    Respond in JSON format like:
    [
      {{
        "name": "...",
        "ingredients": ["...", "..."],
        "instructions": "..."
      }}
    ]
    """
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            options={"num_predict": 250, "temperature": 0.8}
        )
        # The model returns text; ensure it's valid JSON structure
        return parse_llm_response(response["message"]["content"])
    except Exception as e:
        return [{"error": f"Error generating recipes: {e}"}]

def parse_llm_response(content: str):
    import json, re
    # Extract JSON-like content safely
    try:
        match = re.search(r'\[.*\]', content, re.S)
        if match:
            return json.loads(match.group(0))
    except Exception:
        pass
    # fallback: return as plain text
    return [{"text": content}]
