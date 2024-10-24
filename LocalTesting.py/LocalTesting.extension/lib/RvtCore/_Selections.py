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

def pick_single_element(doc: Document, uidoc: UIDocument) -> Element:
    '''Pick a single Revit element'''
    selection_reference = uidoc.Selection.PickObject(ObjectType.Element)
    element = doc.GetElement(selection_reference)
    return element

def get_endpoint_as_xyz(detail_line: DetailLine) -> XYZ:
    end_point = detail_line.GeometryCurve.GetEndPoint(1)
    return end_point

def get_builtin_param(element: Element, bip: str) -> Parameter:
    param = element.get_Parameter(bip)
    return param

def get_shared_parameter(element: Element, param_name: str) -> Parameter:
    param = element.LookupParameter(param_name) 
    return param