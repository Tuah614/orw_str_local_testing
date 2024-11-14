# -*- coding: utf-8 -*-
__title__ = "Get Unique Panel Types" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from RvtCore import _Collections

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument #type: UIDocument 
app = __revit__.Application #type: Application
selection = uidoc.Selection #type: Selection

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================

str_found_collector = FilteredElementCollector(doc)\
                        .OfCategory(BuiltInCategory.OST_StructuralFoundation)\
                        .WhereElementIsNotElementType()\
                        .ToElements()

panel_set = set()

for ele in str_found_collector:
    param_value = ele.LookupParameter("ACM_DWALL_Panel Type").AsString() 
    if param_value is not None:
        panel_set.add(param_value)

sorted_by_numeric = sorted(panel_set, key=_Collections.sort_panel_types_alphanumeric)

for t in sorted_by_numeric:
    print(t)