#!/usr/bin/env python
#from __future__ import print_function, unicode_literals
'''
This script shows how to query a router via SNMPv3
It relies on Kirk's snmp_helper function for the 
SNMP polling and the data parsing components
'''

from snmp_helper import snmp_get_oid_v3, snmp_extract
pynet_rtr1 = ('184.105.247.70', 161)
pynet_rtr2 = ('184.105.247.71', 161)
username = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
oid = '1.3.6.1.2.1.1.3.0'

snmp_oids = (
    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
    ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
    ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5', True)
)

snmp_user = (username, auth_key, encrypt_key)
#print(snmp_user)
#print(pynet_rtr1)
#print(pynet_rtr2)

for desc,an_oid,is_count in snmp_oids:
    snmp_data = snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=an_oid)
    output = snmp_extract(snmp_data)
    print "%s %s" % (desc, output)
snmp_data = snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=snmp_oids[1][1])
printable_snmp_data = snmp_extract(snmp_data)
print(printable_snmp_data)
#uptime_days=int(printable_snmp_data)/8640000
#print(uptime_days)
#print(type(snmp_data))
