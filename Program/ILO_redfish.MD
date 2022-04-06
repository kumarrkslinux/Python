```python
import sys
import redfish
login_host = "https://server_name"
ilo_admin = "new_user"
ilo_passwd = "passowrd"
with redfish.redfish_client(base_url=login_host, username=ilo_admin, password=ilo_passwd) as redfish_object:
      get_detail = redfish_object.get("/redfish/v1/systems/1/bios", None)
      sys.stdout.write("%s\n" % get_detail)
