#!/usr/bin/env python3
from __future__ import print_function, unicode_literals
'''This is my script for practicing the basics of Python.
Come back to this script for referrence.
'''
my_str = 'Hello World'
my_str2 = "something else"
my_str3 = '''this is a
comment that 
spans multiple lines'''
ip_addr1 = '172.16.1.1'
ip_addr2 = '172.31.17.99'
ip_addr3 = '217.88.17.1'
octets = ip_addr2.split(".")
print(type(my_str))
print(my_str)
print(my_str2)
print(my_str3)
print(repr(my_str3))
print("\n")
print("-" * 80)
print("{:20}{:20}{:20}".format(ip_addr1, ip_addr2, ip_addr3))
print("-" * 80)
print("{:^10}{:^10}{:^10}{:^10}".format(octets[0], octets[1], octets[2], octets[3]))
print("-" * 80)
print("{:^10}{:^10}{:^10}{:^10}".format(*octets))
print("-" * 80)
#print(ip_addr1, ip_addr2, ip_addr3)
print("\n")
