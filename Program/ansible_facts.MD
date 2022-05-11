```python
import json
import os

def get_unreachable_hosts():
    facts_dir = '/app/data/ansible_facts'
    hosts_list = []
    for _, _, files in os.walk(facts_dir):
        for file in files:
            with open(os.path.join(facts_dir, file), 'r') as _:
                facts = json.loads(_.read())
                if 'ansible_facts' not in facts.keys():
                    hosts_list.append(file)
    return hosts_list
hosts_list = get_unreachable_hosts()
print(hosts_list)

def main():
    get_unreachable_hosts()

if __name__ == '__main__':
    main()
