# -*- coding: utf-8 -*-
__title__ = "Get Unique Panel Types" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
import clr

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

def sort_panel_types(p_type):
    if len(p_type) == 1:
        alpha = p_type[0]
        numeric1 = p_type[0]
        numeric2 = p_type[0]
    else:
        if p_type[0].isalpha():
            alpha = p_type[0]
            numeric1 = int(p_type[1])
            numeric2 = None
        else:
            alpha = p_type[0]
            numeric1 = int(p_type[0])
            numeric2 = p_type[0]
    return(alpha, numeric1, numeric2)

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

sorted_by_numeric = sorted(panel_set, key=sort_panel_types)

for t in sorted_by_numeric:
    print(t)