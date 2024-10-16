# -*- coding: utf-8 -*-
__title__ = "Update Layer Values" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
import clr

# ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
# ║  ║ ║║║║╚═╗ ║ ╠═╣║║║ ║ ╚═╗
# ╚═╝╚═╝╝╚╝╚═╝ ╩ ╩ ╩╝╚╝ ╩ ╚═╝ CONSTANTS
# ==================================================

REBARLAYERFAMNAME = "ACM_DET_Rebar Layer"
LAYERPROPERTYFAMNAME = "ACM_DET_Layer Properties"
FAMNAMES = [REBARLAYERFAMNAME, LAYERPROPERTYFAMNAME]

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

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================

annotations_collector = FilteredElementCollector(doc).\
                        OfCategory(BuiltInCategory.OST_GenericAnnotation).\
                        WhereElementIsNotElementType().\
                        ToElements()

rl_valid_instances = []
lp_valid_instances = []

for ele in annotations_collector:
    fam_name = ele.Symbol.FamilyName 
    if fam_name == REBARLAYERFAMNAME:
        rl_valid_instances.append(ele)
        # print(ele.LookupParameter("Level Ownership").AsString())
    if fam_name == LAYERPROPERTYFAMNAME:
        lp_valid_instances.append(ele)
        # print(ele.LookupParameter("Dwall Coupler Type").AsString())

for ele in rl_valid_instances:
    print(ele.LookupParameter("Level Ownership").AsString())



# for ele in lp_valid_instances:
#     print(ele.LookupParameter("Dwall Coupler Type").AsString())