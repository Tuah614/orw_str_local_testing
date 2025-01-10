# -*- coding: utf-8 -*-
__title__ = "Collect Coupler Schedule Family" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import Selection, ObjectType
from RvtCore import _Collectors, _Selections
from Autodesk.Revit.UI import UIDocument
from Autodesk.Revit.ApplicationServices import Application

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument #type: UIDocument
app = __revit__.Application #type: Application

# ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
# ║  ║ ║║║║╚═╗ ║ ╠═╣║║║ ║ ╚═╗
# ╚═╝╚═╝╝╚╝╚═╝ ╩ ╩ ╩╝╚╝ ╩ ╚═╝ CONSTANTS
# ==================================================

COUPLER_SCHEDULE_FAM_NAME = "ACM_DET_Layer Properties"
COUPLER_SCHEDULE_FAM_ID = 4633946

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================

class_filter = _Selections.CustomISelectionFilter_Class(Viewport)
selected_viewport =uidoc.Selection.PickObject(ObjectType.Element, class_filter, "Viewport test")
viewport = doc.GetElement(selected_viewport) # type: Viewport
sheet_id = viewport.SheetId
sheet = doc.GetElement(sheet_id)
print(sheet.SheetNumber)