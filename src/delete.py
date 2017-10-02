import os

import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        response = table.delete_item(
            Key={
                'keyname': event['pathParameters']['keyname']
            },
            ReturnValues='ALL_OLD'
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return "{}".format(e.response['Error']['Message'])
    else:
        if 'Attributes' in response:
            retval = {
                "statusCode": 200
            }
        else:
            retval = {
                "statusCode": 404
            }
   
    return retval
