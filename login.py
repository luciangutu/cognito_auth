import boto3
import base64
import hashlib
import hmac
import config


def gen_secret_hash(username, client_id, client_secret):
    message = bytes(username + client_id, 'utf-8')
    key = bytes(client_secret, 'utf-8')
    return base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()


client = boto3.client('cognito-idp', region_name=config.cognito_region)

if config.app_client_secret:
    auth_parameters = {
            'USERNAME': config.cognito_username,
            'PASSWORD': config.cognito_password,
            'SECRET_HASH': gen_secret_hash(config.cognito_username, config.app_client_id, config.app_client_secret)
        }
else:
    auth_parameters = {
            'USERNAME': config.cognito_username,
            'PASSWORD': config.cognito_password
        }

try:
    response = client.admin_initiate_auth(
        UserPoolId=config.cognito_userpool_id,
        ClientId=config.app_client_id,
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters=auth_parameters
    )
    print(response["AuthenticationResult"]["IdToken"])
except Exception as err:
    print(err)
