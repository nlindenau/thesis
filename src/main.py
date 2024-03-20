import flask
import functions_framework
import ast
import json

from process_user_request import run_request_processing_workflow

def lambda_handler(event, context):

    event_body = event.get("body") 

    data = ast.literal_eval(event_body)

    response_body = run_request_processing_workflow(data)
    
    response_body = json.dumps(response_body)

    response = {"statusCode": 200,
        "body": response_body}

    return response

@functions_framework.http
def nutrition_facts_calculator(request: flask.Request) -> flask.typing.ResponseReturnValue:
    request_body = flask.request.json 

    response = run_request_processing_workflow(request_body)

    response = flask.jsonify(response)

    return response, 200
