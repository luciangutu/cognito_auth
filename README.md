Get TOKEN from Cognito using user and password


[login.py](login.py) contains the solution for authenticating against Cognito User Pool with user and password (WITHOUT secret)
Requirements:
- Cognito User Pool
- IAM access with permissions to Cognito (AWS keys)
- [Cognito App client](App_client.png) without App client secret 
- Auth Flows Configuration enabled for all
- [Cognito App client settings](App_client_settings.png) with Sign in and sign out URLs, Authorization code grant
- Allowed OAuth Scopes email and openid
- Domain name
- [Api Gateway Authorizer](api_gw_authorizers.png) pointing to Cognito User Pool



[login_with_secrethash.py](login_with_secrethash.py) contains the solution for authenticating against Cognito User Pool with user, password and app client secret.

Requirements:
- Cognito User Pool
- IAM access with permissions to Cognito (AWS keys)
- Cognito App client with App client secret
- Auth Flows Configuration enabled for all
- App client settings with Sign in and sign out URLs, Authorization code grant
- Allowed OAuth Scopes email and openid
- Domain name
- Api Gateway Authorizer pointing to Cognito User Pool

Use the IdToken from the response when calling the Api Gateway endpoint