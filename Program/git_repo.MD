```python
import requests
import json
api_url = "https://api.github.com/users/kumarrkslinux/repos"
pesponse1 = requests.get(api_url)
presponse2 = pesponse1.json()
for i in presponse2:
    print(i['html_url'])
    
>python APINEW.py
https://github.com/kumarrkslinux/Ansible
https://github.com/kumarrkslinux/ansible-for-devops
https://github.com/kumarrkslinux/build_tools_to_automate_python
https://github.com/kumarrkslinux/certified-kubernetes-administrator-course
https://github.com/kumarrkslinux/Cloud
https://github.com/kumarrkslinux/file
https://github.com/kumarrkslinux/hashicorp-certified-vault-associate
https://github.com/kumarrkslinux/iDRAC-Redfish-Scripting
https://github.com/kumarrkslinux/kubernetes
https://github.com/kumarrkslinux/kubernetes-101
https://github.com/kumarrkslinux/kubernetes-the-hard-way
https://github.com/kumarrkslinux/Master-Statistics-Live-Series
https://github.com/kumarrkslinux/Python
https://github.com/kumarrkslinux/scrape-automation
https://github.com/kumarrkslinux/Terraform
https://github.com/kumarrkslinux/terraform-aws-ec2-instance
https://github.com/kumarrkslinux/terraform-beginner-to-advanced-resource
https://github.com/kumarrkslinux/terraform-examples
https://github.com/kumarrkslinux/Vault
