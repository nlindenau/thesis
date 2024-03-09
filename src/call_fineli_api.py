import requests

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

def print_all_food_names(fineli_response, language="en"):
    '''Pretty print Fineli response basic data.

    Keyword arguments:
    fineli_response -- JSON of the Fineli API response.
    language -- search language (default en)
    '''
    print("Food ID - Food name")
    for element in fineli_response:
        print(element["id"], "-" ,element["name"][language])