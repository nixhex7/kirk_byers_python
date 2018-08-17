#!/usr/bin/env python
from __future__ import print_function, unicode_literals
'''
This script is a basic example of how to
establish an SSH session to a device
'''

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

homerouter = {
    'device_type': 'fortinet',
    'ip': '47.32.124.103', #Current IP of Home Lab Fortinet
    'username': 'admin',
    'password': password,
}

home_rtr = ConnectHandler(**homerouter)
print(home_rtr)
print(home_rtr.find_prompt())

