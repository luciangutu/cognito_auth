import boto3
import config

client = boto3.client('cognito-idp', region_name=config.cognito_region)

try:
    response = client.admin_create_user(
        UserPoolId=config.cognito_userpool_id,
        Username=config.cognito_username,
        TemporaryPassword=config.cognito_password,
    )
    print(response)
    response = client.admin_set_user_password(
        UserPoolId=config.cognito_userpool_id,
        Username=config.cognito_username,
        Password=config.cognito_password,
        Permanent=True
    )
    print(response)
except Exception as err:
    print(err)
