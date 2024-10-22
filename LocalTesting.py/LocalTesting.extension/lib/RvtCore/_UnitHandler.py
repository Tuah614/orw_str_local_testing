# -*- coding: utf-8 -*-

# imports
from Autodesk.Revit.DB import *
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

def convert_internal_to_millimeter(internal_unit_value):
    '''Convert internal ft to mm'''
    converted_unit = UnitUtils.ConvertFromInternalUnits(internal_unit_value, UnitTypeId.Millimeters)
    return converted_unit

def convert_millimeter_to_internal(project_unit_value):
    '''Convert mm to internal ft'''
    converted_unit = UnitUtils.ConvertToInternalUnits(project_unit_value, UnitTypeId.Millimeters)
    return converted_unit