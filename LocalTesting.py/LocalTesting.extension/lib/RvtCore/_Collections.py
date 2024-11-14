# -*- coding: utf-8 -*-

# imports
import re

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ==================================================

def sort_panel_types_alphanumeric(p_type):
    match = re.match(r"([A-Za-z]+)(\d+)", p_type)
    if match:
        alpha, numeric = match.groups()
        return (alpha.isdigit(), alpha, int(numeric))
    return (p_type,)

