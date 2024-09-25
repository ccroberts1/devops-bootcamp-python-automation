import time
import boto3
import paramiko

image_id='ami-0ebfd941bbafe70c6'
key_name='python-server'
instance_type='t3.medium'

ssh_user='ec2-user'
ssh_private_key_path='/Users/alban/Downloads/python-server.pem'

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

# ec2_creation_result = ec2_resource.create_instances(
#     ImageId=image_id,
#     InstanceType=instance_type,
#     KeyName=key_name,
#     MinCount=1,
#     MaxCount=1,
#     TagSpecifications=[
#         {
#             'ResourceType': 'instance',
#             'Tags': [
#                 {
#                     'Key': 'Name',
#                     'Value': 'python-server'
#                 }
#             ]
#         }
#     ])
# instance = ec2_creation_result[0]
# instance_id=instance.id
#
# ec2_instance_running = False
#
# while not ec2_instance_running:
#     print("Getting instance status")
#     statuses = ec2_client.describe_instance_status(
#         InstanceIds=[instance_id]
#     )
#     if len(statuses['InstanceStatuses']) != 0:
#         ec2_status = statuses['InstanceStatuses'][0]
#         instance_status = ec2_status['InstanceStatus']['Status']
#         system_status = ec2_status['SystemStatus']['Status']
#         state = ec2_status['InstanceState']['Name']
#         ec2_instance_running = instance_status == 'ok' and system_status == 'ok' and state == 'running'
#     if not ec2_instance_running:
#         print("sleeping for 30 seconds")
#         time.sleep(30)
#
# print("Instance up and running!")
#
# describe_instances_response = ec2_client.describe_instances(
#     Filters=[
#         {
#             'Name': 'tag:Name',
#             'Values': [
#                 'python-server',
#             ]
#         }
#     ]
# )
#
# print(describe_instances_response)
#
# instance = describe_instances_response['Reservations'][0]['Instances'][0]
# ssh_host = instance['PublicIpAddress']
#
# print("Connecting to EC2 server...")

# ssh_commands = [
#     'sudo yum update -y && sudo yum install -y docker',
#     'sudo systemctl start docker',
#     'sudo usermod -aG docker ec2-user',
#     'docker run -d -p 8080:80 --name nginx nginx'
# ]
#
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname='98.81.243.117', username=ssh_user, key_filename=ssh_private_key_path)
#
# for command in ssh_commands:
#     stdin, stdout, stderr = client.exec_command(command)
#     stdin.close()
#     print(stdout.readlines())
#
# client.close()

security_group = ec2_client.describe_security_groups(
    GroupNames=['default']
)
sg_permissions = security_group['SecurityGroups'][0]['IpPermissions']

print(security_group)
print(sg_permissions)

nginx_port_open = False
for permission in sg_permissions:
    if 'FromPort' in permission and permission['FromPort'] == 8080:
        nginx_port_open = True

if not nginx_port_open:
    open_nginx_port_response = ec2_client.authorize_security_group_ingress(
        FromPort=8080,
        ToPort=8080,
        GroupName='default',
        CidrIp='0.0.0.0/0',
        IpProtocol='tcp'
    )

print(f"Nginx Port Status:{nginx_port_open}")


