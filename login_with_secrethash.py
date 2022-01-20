import base64
import hashlib
import hmac
import json
import boto3

cognito_username = 'lgutu@example.com'
cognito_password = 'somepassword1234'
app_client_id = '3j9qc6rldde0h8bp0u1tqshm22'
app_client_secret = '5jt415s8cfk9jovkdno2qse1hlmfgikvm731p84jave54s1itl1'

message = bytes(cognito_username + app_client_id, 'utf-8')
key = bytes(app_client_secret, 'utf-8')
secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()

client = boto3.client('cognito-idp', region_name='eu-west-1')

try:
    response = client.admin_initiate_auth(
        UserPoolId='eu-west-1_7hmLTKa6y',
        ClientId=app_client_id,
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters={
            'USERNAME': cognito_username,
            'PASSWORD': cognito_password,
            'SECRET_HASH': secret_hash
        },
    )
    print(json.dumps(response, indent=4))
except Exception as err:
    print(err)

