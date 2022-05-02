from conjur import Client
from conjur_iam_client import create_conjur_iam_client_from_env
import os

def lambda_handler(event, context):
    # Retrieved from user-defined Lambda environment variables
    iam_role_name = os.environ['IAM_ROLE_NAME']
    # Retrieved from Lambda-defined runtime environment variables
    access_key = os.environ['AWS_ACCESS_KEY_ID']
    secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
    token = os.environ['AWS_SESSION_TOKEN']
    # Set to false if self-signed or LetsEncrypt certificates are used
    ssl_verify=False

    conjur_client = create_conjur_iam_client_from_env(iam_role_name, access_key, secret_key, token, ssl_verify=ssl_verify)
    conjur_list = conjur_client.list()
    return {
        "list": conjur_list
    }
