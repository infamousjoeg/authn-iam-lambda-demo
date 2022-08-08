# authn-iam-lambda-demo

A demonstration using @cyberark Conjur's authn-iam integration with AWS Lambda.

## Usage

1. Download [latest zip file](https://github.com/infamousjoeg/authn-iam-lambda-demo/releases/latest) from Releases and upload to AWS Lambda function.
   Ensure that you unpack and remove the repo contents from the default Github folder. Re-compress the contents so lambda_function.py is in the root of the zip.
2. Set the following environment values with their relevant values in the Lambda function definition:
   1. `CONJUR_APPLIANCE_URL`: URL of the Conjur appliance.
   2. `CONJUR_ACCOUNT`: Account name.
   3. `CONJUR_AUTHN_LOGIN`: Login name.
   4. `AUTHN_IAM_SERVICE_ID`: Service ID of the authn-iam service.
   5. `CONJUR_CERT_FILE`: Path to the Conjur TLS certificate file, if not using a trusted TLS certificate (self-signed or LetsEncrypt.
   6. `IAM_ROLE_NAME`: Name of the IAM role assigned to the Lambda function.
3. Adjust the Lambda's Timeout to 1 minute to avoid task timeout errors.
4. Adjust the Conjur variable value in "lambda_function.py", line 17, to match the secret which you'd like to print to screen

## Lambda Best Practices

It is important to understand that AWS Lambda functions are restricted to internal communication to other resources within the VPC it is assigned to. If the Conjur service is external to the VPC, a NAT Gateway must be attached to the Lambda function for external access.

If you're just setting up a demo or POC, you may just want to use the private IP address of the Conjur Follower in the same VPC as the Lambda function and set `ssl_verify` to `False` in [lambda_function.py](). Otherwise, be sure to attach a subnet to the Lambda function that is a NAT Gateway.
