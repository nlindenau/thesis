from process_user_request import get_list_of_ingredients, get_ingredients_facts_from_fineli, calculate_nutiritonal_values_for_servings, sum_nutritional_values_for_all_ingredients, create_full_response


def main():
    user_request = [
    {
        "name": "Apple, average",
        "weight": 300
    },
    {
        "name": "Cream Cheese, low-fat",
        "weight": 50
    },
    {
        "name": "Honey, raw",
        "weight": 10
    },
]
    ingredients = get_list_of_ingredients(user_request)

    #cleaned_fineli_response = run_fineli_workflow(query)
    #most_similar_entry = run_fuzzy_matching_workflow(cleaned_fineli_response, query)
    #print(type(most_similar_entry))

    #print(most_similar_entry)

    fineli_list = get_ingredients_facts_from_fineli(ingredients)

    fineli_ingredients = get_list_of_ingredients(fineli_list)

    print(fineli_list)

    nutritional_values_for_servings = calculate_nutiritonal_values_for_servings(user_request, fineli_list)

    final_label = sum_nutritional_values_for_all_ingredients(nutritional_values_for_servings)

    response = create_full_response(ingredients, fineli_ingredients, final_label)

    print(response)

main()
