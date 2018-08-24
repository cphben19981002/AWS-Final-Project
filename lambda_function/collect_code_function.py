import boto3
import json
import os


print('Loading function')
s3 = boto3.client('s3')
apigateway = boto3.client('apigateway')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    apiKey = apigateway.get_api_key(apiKey=event["requestContext"]["identity"]["apiKeyId"],includeValue=True)
    
    body = json.loads(event["body"])
    print(type(body))
    print(body)
    s3.put_object(Bucket=os.environ['StudentLabDataBucket'], Key="code/"+ apiKey["name"] + body["key"],
              Body=body["code"],
              Metadata={"ip":event["requestContext"]["identity"]["sourceIp"], },
              ContentType="application/json"
          )
          
    print(apiKey)
    return respond(None, apiKey["name"])
