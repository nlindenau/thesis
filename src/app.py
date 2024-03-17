from flask import Flask, request, jsonify
from src.process_user_request import get_list_of_ingredients, get_ingredients_facts_from_fineli, calculate_nutiritonal_values_for_servings, sum_nutritional_values_for_all_ingredients, create_full_response

app = Flask(__name__)

EXAMPLE_RETURN = {"message": "hello"}
@app.route("/")
def welcome_message():
    return "<p>Hello from RVAL.</p>"

@app.post("/api/v1/nutritionfacts")
def nutrition_facts_calculator():
    request_body = request.json 
    request_body = sorted(request_body, key=lambda d: d['name'])

    ingredients = get_list_of_ingredients(request_body)
    ingredients.sort()

    fineli_list = get_ingredients_facts_from_fineli(ingredients)
    fineli_list = sorted(fineli_list, key=lambda d: d['name'])

    fineli_ingredients = get_list_of_ingredients(fineli_list)
    fineli_ingredients.sort()

    nutritional_values_for_servings = calculate_nutiritonal_values_for_servings(request_body, fineli_list)

    final_label = sum_nutritional_values_for_all_ingredients(nutritional_values_for_servings)

    response = create_full_response(ingredients, fineli_ingredients, final_label)

    return jsonify(response)
