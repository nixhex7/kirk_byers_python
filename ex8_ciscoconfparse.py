#!/usr/bin/env python
"""
Write a Python program using ciscoconfparse that parses the 'cisco_ipsec.txt'
config file. Note, this config file is not fully valid (i.e. parts of the
configuration are missing).
The script should find all of the crypto map entries in the file (lines that
begin with 'crypto map CRYPTO') and print out the children of each crypto map.
"""
from __future__ import unicode_literals, print_function
from ciscoconfparse import CiscoConfParse

def main():
    """
    Find all of the crypto map entries in the file (lines that begin with
    'crypto map CRYPTO') and print out the children of each crypto map.
    """
    cisco_file = "cisco_ipsec.txt"

    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")
    print("Printing crypto_maps content")
    print(crypto_maps)
    print('\n\n')
    print ("#" * 3)
    print ("#" * 3, 'crypto_maps Type:')
    print ("#" * 3)
    print(type(crypto_maps))
    for c_map in crypto_maps:
        print ("#" * 3)
        print ("#" * 3, 'c_map Type:')
        print ("#" * 3)
        print(type(c_map))
        print()
        print(c_map.text)
        for child in c_map.children:
            print(child.text)
        print()


if __name__ == "__main__":
    main()
