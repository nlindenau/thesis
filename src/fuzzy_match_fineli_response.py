from thefuzz import fuzz
from copy import deepcopy


def get_names_similarity_score(processed_fineli_response, original_query_word):
    '''Assign a Fuzzy Matching similarity score for all foods in a cleaned list of Fineli responses. Uses token set ratio.

    Keyword arguments:
    processed_fineli_response -- preprocessed list of Fineli responses using process_fineli_data.get_list_of_nutrition_values() 
    original_query_word -- original query entered by the user calling the API.
    '''
    processed_fineli_response_w_similarity_score = deepcopy(processed_fineli_response)
    for element in processed_fineli_response_w_similarity_score: 
        similarity_score = fuzz.token_set_ratio(original_query_word, element["name"])
        element["similarity_score"] = similarity_score
    return processed_fineli_response_w_similarity_score

def get_most_similar_entry(list_w_similarity_score):
    '''Assign a Fuzzy Matching similarity score for all foods in a cleaned list of Fineli responses.

    Keyword arguments:
    processed_fineli_response -- preprocessed list of Fineli responses using process_fineli_data.get_list_of_nutrition_values() 
    original_query_word -- original query entered by the user calling the API.
    '''
    highest_score_entry = {}
    highest_similarity_score = 0 
    for element in list_w_similarity_score:
        if element["similarity_score"] > highest_similarity_score:
            highest_score_entry = element
            highest_similarity_score = highest_score_entry["similarity_score"]
    
    return highest_score_entry