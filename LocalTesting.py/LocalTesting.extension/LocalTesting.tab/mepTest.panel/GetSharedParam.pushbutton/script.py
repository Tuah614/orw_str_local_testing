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

collectors = FilteredElementCollector(doc).\
            OfClass(SharedParameterElement).\
            WhereElementIsNotElementType().\
            ToElements() # type: FilteredElementCollector

parameter_dict = {}
for ele in collectors:
    param_name = ele.Name
    if param_name not in parameter_dict:
        parameter_dict[param_name] = []
    parameter_dict[param_name].append(ele)

no_duplicate_names = []
for key, values in parameter_dict.items():
    if len(values) <= 1:
        no_duplicate_names.append(key)

for name in no_duplicate_names:
    del parameter_dict[name]

project_param = {}
param_bindings = doc.ParameterBindings
iterator = param_bindings.ForwardIterator()
iterator.Reset()
while iterator.MoveNext():
    project_param[iterator.Key.Name] = iterator.Key

for key, values in sorted(project_param.items()):
    print(key)