# -*- coding: utf-8 -*-
__title__ = "Get Family by Name" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from RvtCore._Collectors import get_family_by_names
import clr

# ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
# ║  ║ ║║║║╚═╗ ║ ╠═╣║║║ ║ ╚═╗
# ╚═╝╚═╝╝╚╝╚═╝ ╩ ╩ ╩╝╚╝ ╩ ╚═╝ CONSTANTS
# ==================================================

SCHEDULE_HEADER_200_FAMNAME = "ACM_DET_Dwall Schedule Header_Scale 200"
ELEVATION_HEADER_200_FAMNAME = "ACM_DET_Elevation Header_Scale 200"
ELEVATION_INFORMATION_200_FAMNAME = "ACM_DET_Elevation Information_Scale 200"
REQUIRED_FAMILY_NAMES = [SCHEDULE_HEADER_200_FAMNAME, 
                         ELEVATION_HEADER_200_FAMNAME, 
                         ELEVATION_INFORMATION_200_FAMNAME]

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
families = get_family_by_names(doc, REQUIRED_FAMILY_NAMES) # type : List[Family]
for family in families:
    print(family.Name)
    symbolsids = family.GetFamilySymbolIds() # type: List[FamilySymbol]
    for id in symbolsids:
        element = Document.GetElement(doc, id)
        print(Element.Name.__get__(element))
