#!/usr/bin/python3
reading_file = open("/home/anil/ansible/web_server.yml", "r")

data = reading_file.read()

data = data.replace('welcome to new ansible web testing','Welcome To New Ansible Web Testing')

reading_file.close()

reading_file = open("/home/anil/ansible/web_server.yml", "w")

reading_file.write(data)

reading_file.close()
