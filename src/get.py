import os
import json

from src import decimalencoder
import boto3
from botocore.exceptions import ClientError
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        response = table.get_item(
            Key={
                'keyname': event['pathParameters']['keyname']
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        if 'Item' in response:
            retval = {
                "statusCode": 200,
                "body": json.dumps(response['Item'],
                                   cls=decimalencoder.DecimalEncoder)
            }
        else:
            retval = {
                "statusCode": 404
            }

    return retval
