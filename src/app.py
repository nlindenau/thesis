from call_fineli_api import get_data_from_fineli
from proccess_fineli_data import get_list_of_nutrition_values
from fuzzy_match_fineli_response import get_names_similarity_score, get_most_similar_entry

import pprint

def fineli_workflow(query):
    fineli_response = get_data_from_fineli(query)
    clean_fineli_response = get_list_of_nutrition_values(fineli_response)
    return clean_fineli_response

def get_best_matching_entry(cleaned_fineli_response, query):
    list_with_similarity_scores = get_names_similarity_score(cleaned_fineli_response, query)
    most_similar_result = get_most_similar_entry(list_with_similarity_scores)
    return most_similar_result

def main():
    query = "Strawberry jam"
    fineli_response = fineli_workflow(query)
    most_similar_response = get_best_matching_entry(fineli_response, query)
    print(type(most_similar_response))

    print(most_similar_response)


main()