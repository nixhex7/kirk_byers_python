#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract
from pprint import pprint

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IP = '184.105.247.70'
#OID = '.1.3.6.1.2.1.31.1.1.0'
OID = '.1.3.6.1.2.1.2.2.1.2.5'

print(type(COMMUNITY_STRING))
print(type(SNMP_PORT))



a_device = (IP, COMMUNITY_STRING, SNMP_PORT)
print("*" *80)
print("*" *20, 'The Type of Variable "a_device" is:', "*" * 20)
print("*" *80)
print(type(a_device))
print(a_device)

print("*" *80, '\n')

snmp_data = snmp_get_oid(a_device, oid=OID)
print(snmp_data)
print("-" * 80, '\n\n')
print(type(snmp_data))
print(len(snmp_data))
print("-" * 80)
print(snmp_data[0][1])
print("-" * 80)
output_pretty = (snmp_data[0][1].prettyPrint())
print(output_pretty)
print("-" * 80, '\n')
output = snmp_extract(snmp_data)
print(output)
