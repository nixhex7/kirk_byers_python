#!/usr/bin/env python
from __future__ import print_function, unicode_literals
'''This is an example script that I created as part of 
Kirk Byers' Python for Network Engineering Class - Week 1 for the CiscoConfParse module.
This script demonstrates how to load a Fortinet Config file into the CiscoConfParse Library/Class and search for objects, child/parent relationships, etc.
This script assumes you have already installed the CiscoConfParse library with "pip install ciscoconfparse"
'''
from ciscoconfparse import CiscoConfParse
'Next line assumes you have a file called "fortinet_test.conf" file in your local directory'
fortinet_cfg = CiscoConfParse("fortinet_test.conf")
'Next line prints out the variable type for the "fortinet_cfg" variable'
print(type(fortinet_cfg))
'Search Fortinet config for all instances of the word "interface"'
intf = fortinet_cfg.find_objects(r"interface")
print ("\n", "\n")
print(type(intf))
print ("\n", "\n")
print ("-" * 80)
print("\n", "\n")
print(intf)
print ("-" * 80)
print("\n", "\n")
for i in intf:
    print(i.text)
print ("-" * 80)
'Now we will move on to search children, parent and child/parent relationships'
'Set a new variable to the 2nd item in the intf list (config system interface)'
sys_int = intf[1]
print("The variable sys_int is type:")
print(type(sys_int))
print("\n")
print("The contents of variable sys_int is set to:")
print(sys_int)
print("-" * 80)
print(sys_int.text)
print("-" * 80)
print("\n")
'Print out all the direct "children" of the sys_int object'
for child in sys_int.children:
    print(child.text)
'Print out ALL of the "children" of the sys_int object'
for child in sys_int.all_children:
    print(child.text)
