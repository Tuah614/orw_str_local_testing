# -*- coding: utf-8 -*-
__title__ = "Generate Elevation Information" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit, forms
from RvtCore import _Collectors, _Selections, _UnitHandler

# ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
# ║  ║ ║║║║╚═╗ ║ ╠═╣║║║ ║ ╚═╗
# ╚═╝╚═╝╝╚╝╚═╝ ╩ ╩ ╩╝╚╝ ╩ ╚═╝ CONSTANTS

SCHEDULE_HEADER_200_FAMNAME = "ACM_DET_Dwall Schedule Header_Scale 200"
ELEVATION_HEADER_200_FAMNAME = "ACM_DET_Elevation Header_Scale 200"
ELEVATION_INFORMATION_200_FAMNAME = "ACM_DET_Elevation Information_Scale 200"
REQUIRED_FAMILY_NAMES = [SCHEDULE_HEADER_200_FAMNAME, 
                         ELEVATION_HEADER_200_FAMNAME, 
                         ELEVATION_INFORMATION_200_FAMNAME]
SH1 = "Standard Header"

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
selection = uidoc.Selection #type: Selection

# ╔═╗╔═╗╔╦╗╔═╗
# ║ ╦╠═╣ ║ ║╣ 
# ╚═╝╩ ╩ ╩ ╚═╝ GATE
# ==================================================

#check if the require families exist in the current document
all_generic_annotations = _Collectors.get_all_generic_annotation_symbols()
family_is_exist, missing_families = _Collectors.family_exist_by_names(all_generic_annotations, REQUIRED_FAMILY_NAMES)
if not family_is_exist:
    missing_family_termination = forms.alert("Missing families: {}".format(str.join(", ", missing_families)),
                                             exitscript=True)
    
# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================