# Demonstrates a simple AWS Lambda function using Python

import json

def lambda_handler(event, context):
    """AWS Lambda: Returns a greeting."""
    # Get the name from the event, default to 'World' if not provided
    name = event.get('name', 'World')
    # Return a JSON-formatted greeting message
    return {
        'statusCode': 200,
        'body': json.dumps(f"Hello, {name}!")
    }

# Deploy using AWS Console or AWS CLI
# Example CLI command:
# aws lambda create-function --function-name HelloLambda --runtime python3.9 \
# --role <role-arn> --handler compute-demo.lambda_handler --zip-file fileb://function.zip