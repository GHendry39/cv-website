import json
import boto3
from botocore.exceptions import ClientError

# Create a DynamoDB client. This line creates a connection to the DynamoDB service.
# 'boto3' is the AWS SDK for Python, allowing our Python code to talk to AWS services.
dynamodb = boto3.resource('dynamodb')
# Specify the DynamoDB table we want to interact with. Make sure 'myTable' matches the name you created.
table = dynamodb.Table('VisitorCount')
browser_count = 0

# This is the main function that Lambda will run when it's triggered.
# 'event' contains the data sent to our Lambda function (e.g., the numbers from our frontend).
# 'context' provides runtime information about the invocation, function, and execution environment.
def lambda_handler(event, context):
    # Extract the visitor count from the 'event' data.
    # .get() is used to safely retrieve values, returning None if the key doesn't exist.
    # browser_count = event.get('browserCount')
    # partition_key = event.get('id')

        # Attempt to store the item in the DynamoDB table.
    try:
        table.update_item(
            Key={'id': '1',},
            UpdateExpression='SET visitorCount = :val1',
            ExpressionAttributeValues={
                ':val1': browser_count+1
            }
        )   
    except ClientError as e:
        # If there's an error storing data (e.g., permission issues), return a 500 error.
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Error storing data in DynamoDB: {e.response["Error"]["Message"]}'})
        }

    # If everything was successful, return a success message and the calculation details.
    # The 'statusCode: 200' indicates success.
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Visitor Count updated successfully',
            'result': {
                'browserCount': browser_count
            }
            })
    }