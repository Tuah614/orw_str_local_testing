# -*- coding: utf-8 -*-

# imports
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from Autodesk.Revit.ApplicationServices import Application
from Autodesk.Revit.UI import UIDocument

# variables
doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument #type: UIDocument
app = __revit__.Application #type: Application

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ==================================================

def pick_single_element(doc, uidoc): # type: (Document, UIDocument) -> Element
    '''Pick a single Revit element'''
    selection_reference = uidoc.Selection.PickObject(ObjectType.Element)
    element = doc.GetElement(selection_reference)
    return element

def get_endpoint_as_xyz(detail_line): # type: (DetailLine) -> XYZ
    end_point = detail_line.GeometryCurve.GetEndPoint(1)
    return end_point

def get_builtin_param(element, bip): # type: (Element, str) -> Parameter
    param = element.get_Parameter(bip) #type: Parameter
    return param

def get_shared_parameter(element, param_name): # type: (Element, str) -> Parameter
    param = element.LookupParameter(param_name) 
    return param