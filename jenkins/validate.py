import requests
import time
import os

ssh_host = os.environ['EC2_SERVER']
host_port = os.environ['HOST_PORT']

try:
    time.sleep(15)

    response = requests.get(f"http://{ssh_host}:{host_port}")
    print(f"response status code: {response.status_code}")
    if response.status_code == 200:
        print("Application is running!")
    else:
        print("Application was not deployed successfully")
except Exception:
    print(f"Connection error: {Exception}")