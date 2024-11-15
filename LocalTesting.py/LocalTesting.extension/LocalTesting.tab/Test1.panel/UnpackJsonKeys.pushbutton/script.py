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

# for panel, panel_prop in schema_data_ordered.items():
#     print(panel)
#     for level, level_prop in panel_prop.items():
#         print(len(level), level)
#         for key in level_prop.values():
#             print(key)
#     print("\n ")

panel_data_as_list = schema_data_ordered.values()
level_names = []
allow_offset_values = []
for level, level_prop in panel_data_as_list[0].items():
    level_names.append(level)

for level in level_names:
    if len(level) < 10:
        allow_offset_values.append(0)
    else:
        allow_offset_values.append(1)

print(allow_offset_values)

panel_data_as_list = schema_data_ordered.values()
panel_data_counts = []
for panel in panel_data_as_list:
    panel_data_counts.append(len(panel))

panel_unique_counts_set = list(set(panel_data_counts))
panel_unique_count = len(panel_unique_counts_set)

LEVELCOUNT = panel_unique_counts_set[0]

allow_header_bool_values = []
for i in range(LEVELCOUNT):
    if i == 0:
        allow_header_bool_values.append(1)
    else:
        allow_header_bool_values.append(0)
print(allow_header_bool_values)