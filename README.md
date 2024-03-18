[![Unit tests](https://github.com/nlindenau/thesis/actions/workflows/run-pytest.yml/badge.svg)](https://github.com/nlindenau/thesis/actions/workflows/run-pytest.yml)

# RVAL - Ravintoarvolaskuri - Nutrition Facts Calculator

## About the project

RVAL is a simple API, helping you to check nutrition facts of your meal. It takes a list of ingredients and their weights, and returns a nutrition facts label for the entire meal. 

RVAL stands for Ravintoarvolaskuri, or in English: Nutrition Facts Calculator. RVAL supports queries in English.

RVAL uses [Fineli](https://fineli.fi/fineli/en/index) and its [API](https://fineli.fi/fineli/fi/avoin-data?) (in Finnish) as the source of data for calculations. Fineli and its API are created maintained by the Finnish Institute for Health and Welfare (THL). 

This project is a part of my Master's thesis at Centria UAS. 

## Tech Stack 

- Python (+ Flask, pytest, ruff)
- Docker
- Terraform
- AWS & GCP 
- GitHub Actions

## Running the application locally

### With Flask 
```sh
pip install -r requirements.txt 
flask --app src.app run
```

The application will take your POST requests at http://127.0.0.1:5000/api/v1/nutritionfacts.
The application also provides a hello world message at http://127.0.0.1:5000.

## Example request payload

### api/v1/nutritionfacts

```json
[
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
```

When giving names of your ingredients, be the most descriptive you can. Fineli returns a long list at every query, with some entries being not at all related to the query word.

RVAL tries to fuzzy match your original query to the results from Fineli, but this is not 100% reliable method. In the API response, you will get a list of Fineli entries that RVAL fuzzy matched to your original query.

Suggested pattern of naming is `item`, `descriptor`. For example `Spaghetti pasta, dry` returns much more accurate results than just `pasta`. For fruit and vegetables, descriptors like `average` or `with skin` work really well.

Weights should be provided in grammes.

