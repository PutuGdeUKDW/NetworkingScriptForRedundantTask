import paramiko

def mikrotik_reset_and_restore(hostname, username, password,name,pw,backup):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh_client.connect(hostname, username=username, password=password, look_for_keys=False)
        ssh_client.exec_command(f"/user add name={name} group=full password={pw}")
        ssh_client.exec_command(f'/system backup save name={backup}')
        print(hostname+" Done!")

    finally:
        ssh_client.close()

if __name__ == "__main__":
    router_hostnames = [
        'your_router_ip1',
        'your_router_ip2',
        'your_router_ip3',
        'your_router_ip4',

    ]
    router_username = "routerUsername"
    router_password = "routerPassword"
    
    yournewusername = "yournewusername"
    yournewpassword = "yournewpassword"

    backupfile = "yourbackupfile.backup"

    for hostname in router_hostnames:
        mikrotik_reset_and_restore(hostname, router_username, router_password,yournewusername,yournewpassword,backupfile)