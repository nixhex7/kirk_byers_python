#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from ciscoconfparse import CiscoConfParse

def main():
    """
    Find all crypto map entires that use PFS Group 2.
    """
    cisco_file = "cisco_ipsec.txt"

    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO",childspec=r"pfs group2")
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
