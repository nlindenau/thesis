[![Unit tests](https://github.com/nlindenau/thesis/actions/workflows/run-pytest.yml/badge.svg)](https://github.com/nlindenau/thesis/actions/workflows/run-pytest.yml)

# RVAL - Ravintoarvolaskuri - Nutrition Facts Calculator

## About the project

RVAL is a simple API, helping you to check nutrition facts of your meal. It takes a list of ingredients and their weights, and returns a nutrition facts label for the entire meal. 

RVAL stands for Ravintoarvolaskuri, or in English: Nutrition Facts Calculator. RVAL supports queries in English.

RVAL uses [Fineli](https://fineli.fi/fineli/en/index) and its [API](https://fineli.fi/fineli/fi/avoin-data?) (in Finnish) as the source of data for calculations. Fineli and its API are created maintained by the Finnish Institute for Health and Welfare (THL). 

This project is a part of my Master's thesis at Centria UAS. 

## Tech Stack 

- Python (+ Functions Framework, pytest, ruff)
- Docker
- Terraform
- AWS & GCP 
- GitHub Actions

## Running the application locally

```sh
pip install -r src/requirements.txt 
functions-framework --target nutrition_facts_calculator --debug --source=src/app.py --host=127.0.0.1 --port=5000
```

The application will take your POST requests at http://127.0.0.1:5000/.

## Deploying to Google Cloud Functions

1. Create Google Cloud Project 
2. Authenticate with Google Cloud CLI
3. Select your project: `gcloud config set project`
4. Run deployment command:
```sh
gcloud functions deploy rval \
--gen2 \
--region=europe-north1 \ (you can substitute for another region)
--runtime=python311 \
--source=src \
--entry-point=nutrition_facts_calculator \
--allow-unauthenticated \
--trigger-http
```
If the deployment is successful, you will see the function's URL in your console.
NOTE: the function will be public.


## Example request body

### POST

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
    }
]
```

When giving names of your ingredients, be the most descriptive you can. Fineli returns a long list at every query, with some entries being not at all related to the query word.

RVAL tries to fuzzy match your original query to the results from Fineli, but this is not 100% reliable method. In the API response, you will get a list of Fineli entries that RVAL fuzzy matched to your original query.

Suggested pattern of naming is `item`, `descriptor`. For example `Spaghetti pasta, dry` returns much more accurate results than just `pasta`. For fruit and vegetables, descriptors like `average` or `with skin` work really well.

Weights should be provided in grammes.

## Example response body

### 200 OK 
```json
{
    "fineli_returned_ingredients": [
        "Apple, Average, With Skin",
        "Cream Cheese, Low-Fat, 11% Fat, Plain",
        "Honey"
    ],
    "nutrition_facts": {
        "carbohydrates": 33.22,
        "energy": 217.76,
        "fat": 5.76,
        "protein": 4.25,
        "salt": 388.87,
        "saturated_fat": 3.83,
        "sugars": 32.96
    },
    "original_ingredients": [
        "Apple, average",
        "Cream Cheese, low-fat",
        "Honey, raw"
    ]
}
```