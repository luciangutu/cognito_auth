import json
import base64


def lambda_handler(event, context):
    print('event:', json.dumps(event))
    print('queryStringParameters:', json.dumps(event['queryStringParameters']))

    if "headers" in event:
        jwt = event["headers"]["Authorization"]
    else:
        return {
            "isBase64Encoded": False,
            'statusCode': 400,
            "headers": {},
            'body': json.dumps({})
        }

    def decode_jwt(_jwt):
        _, jwt_payload, _ = _jwt.replace('Bearer ', '').split(".")
        # padding as per https://stackoverflow.com/a/64616721/12075722
        padded = jwt_payload + "=" * divmod(len(jwt_payload), 4)[1]
        jwt_payload = base64.b64decode(padded).decode("utf-8")
        return json.loads(jwt_payload)["email"]

    Body = {
        "response": {
           "resultStatus": "SUCCESS",
           "results": {
               "email": decode_jwt(jwt)
           }
        }
    }

    return {
        "isBase64Encoded": False,
        'statusCode': 200,
        "headers": {},
        'body': json.dumps(Body)
    }
