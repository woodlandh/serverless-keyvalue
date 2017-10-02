import json
import time
import logging
import os
import re

from src import decimalencoder
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Missing key: text")
        return

    if not re.match(r'^[A-Za-z0-9_, ]+$', data['text']):
        logging.error("Validation Failed")
        raise Exception("text must be alphanumeric")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        response = table.update_item(
            Key={
                'keyname': event['pathParameters']['keyname']
            },
            ExpressionAttributeNames={
              '#value_text': 'text',
            },
            ExpressionAttributeValues={
              ':text': data['text'],
              ':updatedAt': timestamp,
            },
            UpdateExpression='SET #value_text = :text, '
                             'updatedAt = :updatedAt',
            ReturnValues='ALL_NEW',
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return "{}".format(e.response['Error']['Message'])
    else:
        if 'Attributes' in response:
            retval = {
                "statusCode": 200,
                "body": json.dumps(response['Attributes'],
                                   cls=decimalencoder.DecimalEncoder)
            }
        else:
            retval = {
                "statusCode": 404,
                "body": "Unknown, no data returned from database."
            }

    return retval
