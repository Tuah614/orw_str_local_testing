# -*- coding: utf-8 -*-
__title__ = "QAQC Family Parameters" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from Autodesk.Revit.UI import UIDocument
from RvtCore import _Collections, _Collectors, _UnitHandler
from System import Guid
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝

from Autodesk.Revit.DB import Document
from Autodesk.Revit.ApplicationServices import Application

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument # type: UIDocument
app = __revit__.Application #type: Application
selection = uidoc.Selection #type: Selection

PARAMNAME1 = "Object ID Number"

app.OpenSharedParameterFile()

binding_map = doc.ParameterBindings
binding_map_iterator = binding_map.ForwardIterator()
binding_map_iterator.Reset()

shared_parameters = []

selected_element_reference = uidoc.Selection.PickObject(ObjectType.Element, "Select a single element")
selected_element = doc.GetElement(selected_element_reference)

print("Element name: {0} -- Category: {1} -- ID {2}".format(selected_element.Name, 
                                                            selected_element.Category.Name, 
                                                            selected_element.Id))

element_param_set = selected_element.Parameters
param_map_iterator = element_param_set.ForwardIterator()
param_map_iterator.Reset()

shared_param_in_instance = [] # type: (List[Parameter])
while param_map_iterator.MoveNext():
    if param_map_iterator.Current.IsShared:
        shared_param_in_instance.append(param_map_iterator.Current)

for param in sorted(shared_param_in_instance, key=lambda param: param.Definition.Name):
    print("Name: {0} --- GUID: {1}".format(param.Definition.Name, param.GUID))
