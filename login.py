import boto3

cognito_username = 'lgutu@example.com'
cognito_password = 'somepassword1234'
app_client_id = '61d4soo2me83qqor9jmdnagsvb'

client = boto3.client('cognito-idp', region_name='eu-west-1')

try:
    response = client.admin_initiate_auth(
        UserPoolId='eu-west-1_7hmLTKa6y',
        ClientId=app_client_id,
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters={
            'USERNAME': cognito_username,
            'PASSWORD': cognito_password
        },
    )
    print(response["AuthenticationResult"]["IdToken"])
except Exception as err:
    print(err)

