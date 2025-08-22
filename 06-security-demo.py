# Demonstrates creating an IAM user and attaching a policy using boto3

import boto3

iam = boto3.client('iam')

def create_user(username):
    # Create a new IAM user with the given username
    iam.create_user(UserName=username)

def attach_policy(username):
    # Attach the AdministratorAccess policy to the user
    iam.attach_user_policy(
        UserName=username,
        PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
    )

if __name__ == '__main__':
    username = 'cloud-demo-user'
    create_user(username)
    attach_policy(username)