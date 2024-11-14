# -*- coding: utf-8 -*-
__title__ = "Unpack Json Keys" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from RvtCore import _Utility
from collections import OrderedDict
import json

schema_path = _Utility.get_saved_schema_path()
with open(schema_path, 'r') as local_path:
    path_data = json.load(local_path).values()
    path_value = path_data[0]

with open(path_value,'r') as schema:
    schema_data_ordered = json.load(schema, object_pairs_hook=OrderedDict) #type: OrderedDict
    schema_data_standard = dict(schema_data_ordered)

for panel, panel_prop in schema_data_ordered.items():
    print(panel)
    for level, level_prop in panel_prop.items():
        print(len(level), level)
        for key in level_prop.values():
            print(key)
    print("\n ")