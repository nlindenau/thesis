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

## Example request

```json
request = [
    {
        "name": "Apple, raw",
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
RVAL tries to fuzzy match your original query to the results of Fineli, but this is not 100% reliable method.

Suggested pattern of naming is [Item], [descriptor]. For example [Spaghetti pasta, dry] returns much more accurate results than just [pasta]. 

Weights should be provided in grammes.