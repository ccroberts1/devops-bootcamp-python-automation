import boto3
import os

repo_name = os.environ['ECR_REPO_NAME']

ecr_client = boto3.client('ecr')

images_list = ecr_client.describe_images(repositoryName=repo_name)['imageDetails']

image_tags_list = []
for image in images_list:
    print(image)
    image_tags_list.append(image['imageTags'][0])

for tag in image_tags_list:
    print(tag)