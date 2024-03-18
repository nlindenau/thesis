import requests

#Fineli and its API are created and maintained by the Finnish Institute for Health and Welfare (THL).
#more at: https://fineli.fi/fineli/en/index
FINELI_API_URL = " https://fineli.fi/fineli/api/v1/foods"

def get_data_from_fineli(ingredient: str) -> list:
    '''Query Fineli API.

    Keyword arguments:
    ingredient -- the name of ingredient 
    '''
    query_params = {
        "q": ingredient,
        "lang": "en",
    }
    # sending request without User-Agent results in 403 Forbidden response
    headers = {
    'User-Agent': 'RVAL (Ravintolaskuri) application'
    }
    response = requests.get(url=FINELI_API_URL, params=query_params, headers=headers)
    response = response.json()
    return response