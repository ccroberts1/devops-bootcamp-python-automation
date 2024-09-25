import boto3

from ecr import get_ecr_repo_names, get_repo_image_tags
from subnets import get_all_subnets
from iam import get_user_info, get_most_active_user

ec2_client = boto3.client('ec2')
all_subnets = ec2_client.describe_subnets()['Subnets']

# get_all_subnets(all_subnets)

iam_client = boto3.client('iam')
all_users = iam_client.list_users()['Users']

# get_user_info(all_users)
# get_most_active_user(all_users)

ecr_client = boto3.client('ecr')
all_ecr_repos = ecr_client.describe_repositories()['repositories']

get_ecr_repo_names(all_ecr_repos)
get_repo_image_tags(ecr_client, all_ecr_repos[0]['repositoryName'])

