from copy import deepcopy
from thefuzz import fuzz

from src.call_fineli_api import get_data_from_fineli

def get_list_of_nutrition_values(fineli_response, language="en"):
    '''Clean up Fineli response to get only the EU-law required information for nutrition declaration per item.

    Keyword arguments:
    fineli_response -- JSON of the Fineli API response.
    language -- search language (default en)
    '''
    processed_response = []

    for element in fineli_response:
        #Create a shortened version of an entry from fineli response
        new_item = {
            "name": element["name"][language],        
            "energy": element["energyKcal"],
            "fat": element["fat"],
            "saturatedFat": element["saturatedFat"],
            "carbohydrates": element["carbohydrate"],
            "sugars": element["sugar"],
            "protein": element["protein"],
            "salt": element["salt"]
        }
        processed_response.append(new_item) 
    
    return (processed_response)

def run_fineli_workflow(query):
    '''Query Fineli API and clean up the response for further processing.

    Keyword arguments:
    query -- the name of the ingredient
    '''
    fineli_response = get_data_from_fineli(query)
    clean_fineli_response = get_list_of_nutrition_values(fineli_response)
    return clean_fineli_response


def get_names_similarity_score(processed_fineli_response, original_query_word):
    '''Assign a Fuzzy Matching similarity score for all foods in a cleaned list of Fineli responses. Uses token set ratio.

    Keyword arguments:
    processed_fineli_response -- preprocessed list of Fineli responses 
    original_query_word -- original query entered by the user calling the API.
    '''
    processed_fineli_response_w_similarity_score = deepcopy(processed_fineli_response)
    for element in processed_fineli_response_w_similarity_score: 
        similarity_score = fuzz.token_set_ratio(original_query_word, element["name"])
        element["similarity_score"] = similarity_score
    return processed_fineli_response_w_similarity_score

def get_most_similar_entry(list_w_similarity_score):
    '''Get the entry with the highest fuzzy matching similarity score.

    Keyword arguments:
    list_w_similarity_score -- list of items with similarity score
    original_query_word -- original query entered by the user calling the API.
    '''
    highest_score_entry = {}
    highest_similarity_score = 0 
    for element in list_w_similarity_score:
        if element["similarity_score"] > highest_similarity_score:
            highest_score_entry = element
            highest_similarity_score = highest_score_entry["similarity_score"]

    
    return highest_score_entry

def run_fuzzy_matching_workflow(cleaned_fineli_response, query):
    '''Assign similarity scores and get the most matching entry from a pre-cleaned Fineli response list.

    Keyword arguments:
    cleaned_fineli_response -- Fineli response, containing only nutrition facts required by the EU
    '''
    cleaned_fineli_response_w_similarity_score = get_names_similarity_score(cleaned_fineli_response, query)
    most_similar_entry = get_most_similar_entry(cleaned_fineli_response_w_similarity_score)
    most_similar_entry["original_query"] = query

    return most_similar_entry

def print_all_food_names(fineli_response, language="en"):
    '''Pretty print Fineli response basic data. Helper function for debugging.

    Keyword arguments:
    fineli_response -- JSON of the Fineli API response.
    language -- search language (default en)
    '''
    print("Food ID - Food name")
    for element in fineli_response:
        print(element["id"], "-" ,element["name"][language])