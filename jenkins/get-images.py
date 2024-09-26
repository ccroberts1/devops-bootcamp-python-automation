import boto3
import os

repo_name = os.environ['ECR_REPO_NAME']

ecr_client = boto3.client('ecr')

images = ecr_client.describe_images(repositoryName=repo_name)

image_tags = []
for image in images['imageDetails']:
    image_tags.append(image['imageTags'][0])

for tag in image_tags:
    print(tag)
