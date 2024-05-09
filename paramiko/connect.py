import paramiko

hostname='192.168.56.101'
port = 22

username = 'node'
password = 'node'

command = 'uname -r'

with paramiko.SSHClient() as client:
    client.load_system_host_keys()
    client.connect(hostname,port,username,password)

    (stdin,stdout,stderr) = client.exec_command(command)
    output = stdout.read()

    print(str(output,'utf8'))