import json
import os

from src import decimalencoder
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        response = table.scan()
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        if 'Items' in response:
            retval = {
                "statusCode": 200,
                "body": json.dumps(response['Items'], cls=decimalencoder.DecimalEncoder)
            }
        else:
            retval = {
                "statusCode": 404,
                "body": "No data in database." 
            }

    return retval
