import boto3

ec2_client = boto3.client('ec2')

all_subnets = ec2_client.describe_subnets()['Subnets']

def get_all_subnets():
    for subnet in all_subnets:
        print(subnet['SubnetId'])

