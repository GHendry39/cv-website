import json
import boto3
from botocore.exceptions import ClientError

# Create a DynamoDB client. This line creates a connection to the DynamoDB service.
# 'boto3' is the AWS SDK for Python, allowing our Python code to talk to AWS services.
dynamodb = boto3.resource('dynamodb')
# Specify the DynamoDB table we want to interact with. Make sure 'myTable' matches the name you created.
table = dynamodb.Table('VisitorCount')

# This is the main function that Lambda will run when it's triggered.
# 'event' contains the data sent to our Lambda function (e.g., the numbers from our frontend).
# 'context' provides runtime information about the invocation, function, and execution environment.
def lambda_handler(event, context):
    # Extract the visitor count from the 'event' data.
    # .get() is used to safely retrieve values, returning None if the key doesn't exist.
    browser_count = event.get('browserCount')
    partition_key = event.get('id')

    # Prepare the data (item) to be stored in our DynamoDB table.
    # Each key-value pair here represents an attribute in our database record.
    item = {
        'id': partition_key,  # This matches our Partition Key in DynamoDB
        'visitor-count': browser_count
    }

    # Attempt to store the item in the DynamoDB table.
    try:
        table.put_item(Item=item) # 'put_item' is the DynamoDB operation to add a new item.
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
            'message': 'Visitor Count stored successfully',
            })
    }