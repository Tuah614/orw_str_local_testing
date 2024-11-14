# -*- coding: utf-8 -*-

# imports
import json
import os
from pathlib import Path

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ==================================================

def get_appdata_path():
    path = os.getenv('APPDATA')
    return path # type: str

def get_saved_schema_path():
    appdata_path = get_appdata_path()
    orw_str_path = Path(appdata_path) / 'orw_str'
    json_file_path = orw_str_path / 'schema_directory.json'
    return str(json_file_path) # type: str

def orw_str_exists():
    appdata_path = get_appdata_path()
    orw_str_path = Path(appdata_path) / 'orw_str'
    if not orw_str_path.exists():
        orw_str_path.mkdir()
    return orw_str_path # type: str
