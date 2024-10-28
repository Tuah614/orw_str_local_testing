# -*- coding: utf-8 -*-
__title__ = "Read JSON" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from pyrevit import forms
from collections import OrderedDict
from pathlib import Path
import json
import os

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ==================================================

def sort_panel_types(p_type):
    alpha = p_type
    numeric = int(p_type[1:])
    return (alpha, numeric)

def get_appdata_dir():
    dir = os.getenv('APPDATA')
    return dir

def get_saved_schema_path():
    appdata_dir = get_appdata_dir() 
    orw_str_dir = Path(appdata_dir) / 'orw_str'
    json_file_path = orw_str_dir / 'schema_directory.json'
    return str(json_file_path)

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================

doc = __revit__.ActiveUIDocument.Document #Type: Document
uidoc = __revit__.ActiveUIDocument #Type: UIDocument
app = __revit__.Application #Type: Application
selection = uidoc.Selection #Type: Selection

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================

# get json schema directory
schema_path = get_saved_schema_path()
with open(schema_path, 'r') as local_path:
    try:
        directory_data = json.load(local_path)
        source_file = directory_data['directory']
        # print(source_file)
    except:
        forms.alert("JSON schema not found in user's machine\
                    Author: Tuah Hamid",
                    exitscript=True)

# load panel type schema
with open(source_file, 'r') as schema:
    try:
        schema_data_ordered = json.load(schema, object_pairs_hook=OrderedDict)
        schema_data_standard = dict(schema_data_ordered)
    except:
        print("Failed to load json")

# count level occurences in each panel type, terminate if more than one unique values
panel_data_as_list = schema_data_ordered.values()
print("\n Number of panels in JSON: {0}".format(len(panel_data_as_list)))
panel_data_counts = []
for panel in panel_data_as_list:
    panel_data_counts.append(len(panel))

panel_unique_counts_set = list(set(panel_data_counts))
panel_unique_count = len(panel_unique_counts_set)

if panel_unique_count != 1:
    forms.alert("Level count error in one of the panel types", exitscript=True)
else:
    LEVELCOUNT = panel_unique_counts_set[0]

# ==================================================
# GENERATE LEVEL NAME DATA FOR FAMILY PLACEMENT
# ==================================================

main_key = next(iter(schema_data_standard))
sub_key = next(iter(schema_data_standard[main_key]))

level_names = []
layers_per_level = []
layer_values = []
for level, prop in panel_data_as_list[0].items():
    level_names.append(level)
    layers_per_level.append(prop['Number of layers'])
typ = sorted(schema_data_standard.keys(), key=sort_panel_types)

max_length = max(len(level_name) for level_name in level_names)

for t in typ:
    print("\n Panel Type: {0}".format(t))
    for level_name in level_names:
        layer_properties = schema_data_standard[t][level_name]["Layer values"]
        # Adjust the alignment by setting the width of `level_name` to 12 characters
        print(" {0:<12}                  : {1}".format(level_name, layer_properties))