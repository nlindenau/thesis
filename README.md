[![Unit tests](https://github.com/nlindenau/thesis/actions/workflows/run-pytest.yml/badge.svg)](https://github.com/nlindenau/thesis/actions/workflows/run-pytest.yml)

# RVAL - Ravintoarvolaskuri - Nutrition Facts Calculator

## About the project

RVAL is a simple API, helping you to check nutrition facts of your meal. It takes a list of ingredients and their weights, and returns a nutrition facts label for the entire meal. 

RVAL stands for Ravintoarvolaskuri, or in English: Nutrition Facts Calculator. RVAL supports queries in English, Finnish and Swedish.

RVAL uses [Fineli](https://fineli.fi/fineli/en/index) and its [API](https://fineli.fi/fineli/fi/avoin-data?) (in Finnish) as the source of data for calculations. Fineli and its API are created maintained by the Finnish Institute for Health and Welfare (THL). 

This project is a part of my Master's thesis at Centria UAS. 

## Tech Stack 

- Python + pytest + Flask 
- Docker
- Terraform
- AWS & GCP 
- GitHub Actions