import os
import paramiko
from paramiko.client import AutoAddPolicy

ssh_host = os.environ['EC2_SERVER']
ssh_user = os.environ['EC2_USER']
ssh_private_key = os.environ['SSH_KEY_FILE']

docker_registry = os.environ['ECR_REGISTRY']
docker_user = os.environ['DOCKER_USER']
docker_pwd = os.environ['DOCKER_PWD']
docker_image = os.environ['DOCKER_IMAGE']
container_port = os.environ['CONTAINER_PORT']
host_port = os.environ['HOST_PORT']

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(AutoAddPolicy())
ssh_client.connect(hostname=ssh_host, username=ssh_user, pkey=ssh_private_key)

stdin, stdout, stderr = ssh_client.exec_command(f"echo {docker_pwd} | docker login {docker_registry} --username {docker_user} --password-stdin")
stdin.close()
print(stdout.readlines())

stdin, stdout, stderr = ssh_client.exec_command(f"docker run -p {host_port}:{container_port} -d {docker_image}")
stdin.close()
print(stdout.readlines())

ssh_client.close()