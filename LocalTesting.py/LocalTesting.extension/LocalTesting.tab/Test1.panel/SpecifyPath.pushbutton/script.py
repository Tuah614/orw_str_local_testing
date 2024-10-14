# -*- coding: utf-8 -*-
__title__ = "Specify JSON Path" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

import os
import json
from pyrevit import forms
from pathlib import Path

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument #type: UIDocument 
app = __revit__.Application #type: Application
selection = uidoc.Selection #type: Selection

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ==================================================

def get_appdata_dir():
    dir = os.getenv('APPDATA')
    return dir

def orw_str_exist():
    appdata_dir = get_appdata_dir()
    orw_str_dir = Path(appdata_dir) / 'orw_str'
    if not orw_str_dir.exists():
        orw_str_dir.mkdir()
    return orw_str_dir

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================

panel_type_source = forms.pick_file(file_ext='json')
orw_str_dir = orw_str_exist()
json_file_path = str(orw_str_dir / 'schema_directory.json')
directory_data = {'directory' : panel_type_source}

with open(json_file_path, 'w') as json_file:
    json.dump(directory_data, json_file)

user_appdata = get_appdata_dir()
print(json_file_path, type(json_file_path))