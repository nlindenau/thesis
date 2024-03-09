from call_fineli_api import get_data_from_fineli
from proccess_fineli_data import get_list_of_nutrition_values
from fuzzy_match_fineli_response import get_names_similarity_score, get_most_similar_entry

import pprint

def main():
    query = "Honey, raw"
    fineli_response = get_data_from_fineli("Honey, raw")
    clean_fineli_response = get_list_of_nutrition_values(fineli_response)
    list_with_similarity_scores = get_names_similarity_score(clean_fineli_response, query)
    most_similar_result = get_most_similar_entry(list_with_similarity_scores)
    print(type(most_similar_result))

    print(most_similar_result)


main()