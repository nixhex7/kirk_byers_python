'''This script connects to a cisco lab router and logs
activites to a local text file
'''
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    #"session_log": 'my_session.txt',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'delete flash:/testfile3.txt'
output = net_connect.send_command(command, expect_string=r'test',
                         strip_prompt=False, strip_command=False)
output += net_connect.send_command('testfile3.txt', expect_string=r'confirm',
                         strip_prompt=False, strip_command=False)
output += net_connect.send_command('y', expect_string=r'#',
                         strip_prompt=False, strip_command=False)
print(output)
