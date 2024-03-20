[![Unit tests](https://github.com/nlindenau/thesis/actions/workflows/run-pytest.yml/badge.svg)](https://github.com/nlindenau/thesis/actions/workflows/run-pytest.yml)

# RVAL - Ravintoarvolaskuri - Nutrition Facts Calculator

## About the project

RVAL is a simple API, helping you to check nutrition facts of your meal. It takes a list of ingredients and their weights, and returns a nutrition facts label for the entire meal. 

RVAL stands for Ravintoarvolaskuri, or in English: Nutrition Facts Calculator. RVAL supports queries in English.

RVAL uses [Fineli](https://fineli.fi/fineli/en/index) and its [API](https://fineli.fi/fineli/fi/avoin-data?) (in Finnish) as the source of data for calculations. Fineli and its API are created maintained by the Finnish Institute for Health and Welfare (THL). 

This project is a part of my Master's thesis at Centria UAS. 

## Tech Stack 

- Python (+ pytest, ruff)
- Docker
- SAM & Functions Framework
- AWS & GCP 
- GitHub Actions

## Prerequisites 

- Python, at least 3.9 and pip
- gcloud CLI
- SAM CLI 

## Running the application locally

### With Functions Framework
```sh
pip install -r src/requirements.txt 
functions-framework --target nutrition_facts_calculator --debug --source=src/app.py --host=127.0.0.1 --port=5000
```

The application will take your POST requests at http://127.0.0.1:5000/. 

### With SAM
```sh
cd aws-sam
sam build 
sam local start-api --debug   
```

The application will take your POST requests at http://127.0.0.1:3000/.

## Deploying the application to the cloud

### Google Cloud

1. [Authenticate with Google Cloud CLI](https://cloud.google.com/docs/authentication/gcloud)
2. Select your project: `gcloud config set project`
3. Run deployment command:
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
NOTE: the function will be public. You can make it private by removing `--allow-unauthenticated` flag.

### AWS

1. [Authenticate to AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html)
2. Change directory to aws-sam
```sh
cd aws-sam
```
3. Build the application
```sh
sam build
```
4. Deploy the application (follow prompts on the command line)
```sh
sam deploy --region eu-north-1 --stack-name rval      
```

If the deployment is successful, you will see the API Gateway's Stage and Prod URL in your console.
NOTE: the function will be public.

## Deleting cloud deployment

### Google Cloud

1. Run `gcloud functions delete rval --region europe-north1 `

### AWS

1. Run `sam delete rval`

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
