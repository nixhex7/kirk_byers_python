'''This script connects to a cisco lab router and logs
activites to a local text file
'''
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    #"session_log": 'my_session.txt',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
