# -*- coding: utf-8 -*-
__title__ = "Generate Object Id" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from RvtCore import _Collections, _Collectors, _UnitHandler

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

# collect elements from general model
# categories in order CableTray, Ducts, Pipes

# check for duplicate parameters
# param_result = _Collections.find_duplicate_parameters(doc)
# if param_result[1]:
#     print("Warning! Duplicates found.")
#     for p in param_result[0]:
#         print(p)
# else:
#     print("All good")

cable_trays = _Collectors.get_elements_by_category(doc, BuiltInCategory.OST_CableTray)
ducts = _Collectors.get_elements_by_category(doc, BuiltInCategory.OST_DuctCurves)
pipes = _Collectors.get_elements_by_category(doc, BuiltInCategory.OST_PipeCurves)

# filter pipes only with diameter >= 100mm
valid_pipes = []
for p in pipes:
    mm_dim = _UnitHandler.convert_internal_to_millimeter(p.Diameter)
    if mm_dim >= 100:
        valid_pipes.append(p)

# project parameters using internal definition
binding_map_iterator = doc.ParameterBindings.ForwardIterator()
binding_map_iterator.Reset()

parameters = [] #type : Definition


while binding_map_iterator.MoveNext():
    parameters.append(binding_map_iterator.Key)

for param in parameters:
    print(param.GetDataType().TypeId)
    print(param.Name)
