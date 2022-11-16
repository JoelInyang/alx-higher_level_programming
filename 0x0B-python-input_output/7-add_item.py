#!/usr/bin/python3
"""
script that adds all arguments to a 
Python list, and then save them to a file
"""


import sys

save_to_json_file= __import__('5-save_to_json_file').save_to_json_file
load_from_json_file=__import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    new_list = load_from_json_file(filename)
except:
    new_list = []

for i in range(1, len(sys.argv)):
    new_list.append(i)

save_to_json_file(new_list, filename)
