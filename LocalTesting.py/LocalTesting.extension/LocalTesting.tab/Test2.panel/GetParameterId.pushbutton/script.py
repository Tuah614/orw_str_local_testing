# -*- coding: utf-8 -*-
__title__ = "Collect Coupler Schedule Family" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import UIDocument
from Autodesk.Revit.ApplicationServices import Application

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument #type: UIDocument
app = __revit__.Application #type: Application

# ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
# ║  ║ ║║║║╚═╗ ║ ╠═╣║║║ ║ ╚═╗
# ╚═╝╚═╝╝╚╝╚═╝ ╩ ╩ ╩╝╚╝ ╩ ╚═╝ CONSTANTS
# ==================================================

PARAM_NAME_1 = "Object ID Number"

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================

collectors = set(FilteredElementCollector(doc)\
            .OfClass(ParameterElement)\
            .ToElements())
sorted_param = sorted(collectors, key=lambda param:param.Name)
print(len(collectors))
for param in sorted(sorted_param):
    print("{} : {}".format(Element.Name.__get__(param), param.Id))