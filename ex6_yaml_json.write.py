#!/usr/bin/env python
"""
Write a Python program that creates a list. One of the elements of the list
should be a dictionary with at least two keys. Write this list out to a file
using both YAML and JSON formats. The YAML file should be in the expanded form.
"""
from __future__ import print_function, unicode_literals
import json
import yaml


def main():
    """
    Write a Python program that creates a list. One of the elements of the list
    should be a dictionary with at least two keys. Write this list out to a file
    using both YAML and JSON formats. The YAML file should be in the expanded
    form.
    """
    my_list = range(10)
    my_list.append("Hello")
    my_list.append("Another Word")
    my_list.append({})
    my_list[-1]["ip.addr"] = "10.10.10.240"
    my_list[-1]['attribs'] = range(5)
    my_list[-1]['attribs2'] = 'more attribs'
    print(my_list)
    print("-" * 80)
    print(json.dumps(my_list))
    print("-" * 80)
    print("\n")
    yaml_file = 'yaml_test.yml'
    json_file = 'json_test.json'

    with open(json_file, "w") as f:
        json.dump(my_list, f)
    print("-" * 80)
    print(yaml.dump(my_list, default_flow_style=True))
    print("-" * 80)
    print(yaml.dump(my_list, default_flow_style=False))
    print("-" * 80)
    print("\n")
    with open(yaml_file, "w") as f:
        f.write(yaml.dump(my_list, default_flow_style=False))


if __name__ == "__main__":
    main()
