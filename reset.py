import paramiko

def mikrotik_reset_and_restore(hostname, username, password, backup):
    # Establish an SSH connection to the MikroTik router
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh_client.connect(hostname, username=username, password=password, look_for_keys=False)

        restore_command = f"/system backup load name={backup} password=1"
        ssh_client.exec_command(restore_command)
    finally:
        ssh_client.close()

if __name__ == "__main__":
    router_hostnames = [
        'your_router_ip1',
        'your_router_ip2',
        'your_router_ip3',
        'your_router_ip4',

    ]
    router_username = "router_username"
    router_password = "router_password"
    backupfile = "yourbackupfile.backup"

    for hostname in router_hostnames:
        mikrotik_reset_and_restore(hostname, router_username, router_password,backupfile)
