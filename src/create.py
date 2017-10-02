import json
import logging
import os
import time
import uuid
import re

import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data or 'keyname' not in data:
        logging.error("Validation Failed")
        raise Exception("Missing one or more keys: keyname, text")
        return

    if not re.match(r'^[A-Za-z0-9_]+$', data['keyname']):
        logging.error("Validation Failed")
        raise Exception("keyname must be alphanumeric")
        return
    
    if not re.match(r'^[A-Za-z0-9_, ]+$', data['text']):
        logging.error("Validation Failed")
        raise Exception("text must be alphanumeric")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'keyname': data['keyname'],
        'text': data['text'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    try:
        response = table.put_item(Item=item)
    except ClientError as e:
        print(e.response['Error']['Message'])
        return "{}".format(e.response['Error']['Message'])
    else:
        if response is not None:
            retval = {
                "statusCode": 200,
                "body": json.dumps(item)
            }
        else:
            retval = {
                "statusCode": 500,
                "body": "Unknown error, no return from database."
            }

    return retval
