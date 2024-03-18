import requests
from src.proccess_fineli_data import get_list_of_nutrition_values

#Fineli and its API are created and maintained by the Finnish Institute for Health and Welfare (THL).
#more at: https://fineli.fi/fineli/en/index
FINELI_API_URL = " https://fineli.fi/fineli/api/v1/foods"

def get_data_from_fineli(ingredient, language="en"):
    '''Query Fineli API.

    Keyword arguments:
    ingredient -- the name of ingredient 
    language -- search language (default en)
    '''
    query_params = {
        "q": ingredient,
        "lang": language,
    }
    # sending request without User-Agent results in 403 Forbidden response
    headers = {
    'User-Agent': 'RVAL (Ravintolaskuri) application'
    }
    response = requests.get(url=FINELI_API_URL, params=query_params, headers=headers)
    response = response.json()
    return response

def run_fineli_workflow(query):
    '''Query Fineli API and clean up the response for further processing.

    Keyword arguments:
    query -- the name of the ingredient
    '''
    fineli_response = get_data_from_fineli(query)
    clean_fineli_response = get_list_of_nutrition_values(fineli_response)
    return clean_fineli_response