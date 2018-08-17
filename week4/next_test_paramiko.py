#!/usr/bin/env python
from __future__ import print_function, unicode_literals
'''
This script is the second example that Kirk walks through in his week4 - part 2 
Python for network engineers class
'''

import paramiko
import time
from getpass import getpass

pynet_rtr1 = '184.105.247.70'
port = 22
#pynet_rtr2 = ('184.105.247.71', 161)
username = 'pyclass'
password = getpass()

#Create an SSH Client Object:
remote_conn_pre=paramiko.SSHClient()
#Tell Paramiko to blilndy accept any SSH host keys that it doesn't know about:
#remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Instead of blindly accepting all unknown SSH keys, you can load your system's existing known_hosts keys
remote_conn_pre.load_system_host_keys()
#Initiate the SSH Connection to the target host:
remote_conn_pre.connect(pynet_rtr1, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

#Now you need to invoke a shell:
remote_conn=remote_conn_pre.invoke_shell()

outp = remote_conn.recv(5000)

print(outp)
#remote_conn.send("show ip int brief\n")
remote_conn.send("terminal len 0\n")
time.sleep(1)
#the next line just checks to see if there is any data to read on the router
data_available=remote_conn.recv_ready()
if data_available==True:
    print(data_available)
else:
    print("No Data Available")
    print(data_available)
remote_conn.send("show run\n")
time.sleep(2)
outp = remote_conn.recv(65535)
print(outp)
