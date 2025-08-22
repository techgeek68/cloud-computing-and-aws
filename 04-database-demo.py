# Demonstrates basic operations with Amazon DynamoDB

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DemoTable')

def put_item():
    # Add a new item into DemoTable
    table.put_item(Item={'id': '123', 'name': 'CloudDemo'})

def get_item():
    # Retrieve the item by its key and print the result
    response = table.get_item(Key={'id': '123'})
    print(response.get('Item'))

if __name__ == '__main__':
    put_item()
    get_item()