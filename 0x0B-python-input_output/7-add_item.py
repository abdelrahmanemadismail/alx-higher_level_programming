#!/usr/bin/python3
"""
This script adds command line arguments to a Python list and saves them to
a file using JSON representation.

Usage:
- Ensure that this script has execution permissions
- Run the script with command line arguments to add them to the existing list
  and save to 'add_item.json'.

Dependencies:
- save_to_json_file_module: A module providing a function for saving
  an object to a text file using JSON representation.
- load_from_json_file_module: A module providing a function for loading
  an object from a JSON file.
"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    existing_items = load_from_json_file("add_item.json")
except Exception:
    existing_items = []

for arg in sys.argv[1:]:
    existing_items.append(arg)

save_to_json_file(existing_items, "add_item.json")
