#!/usr/bin/env python

from snmp_helper import snmp_get_oid_v3, snmp_get_oid, snmp_extract

snmp_oids = (
    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
    ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
    ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5', True)
)

print(snmp_oids[2][2])
