from operator import itemgetter

def get_ecr_repo_names(list_of_repos):
    for repo in list_of_repos:
        print(f"Repository Name: {repo['repositoryName']}\n")

def get_repo_image_tags(client, repo_name):
    images_list = client.describe_images(repositoryName=repo_name)['imageDetails']

    image_tag_list = []

    for image in images_list:
        image_tag_list.append({
            'tag': image['imageTags'],
            'pushed_at': image['imagePushedAt']
        })

    sorted_images_list = sorted(image_tag_list, key=itemgetter("pushed_at"), reverse=True)
    for image in sorted_images_list:
        print(image)




