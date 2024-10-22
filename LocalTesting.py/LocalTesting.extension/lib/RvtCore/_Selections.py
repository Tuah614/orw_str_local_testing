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

def pick_single_element(doc, uidoc):
    '''Pick a single Revit element'''
    selection_reference = uidoc.Selection.PickObject(ObjectType.Element)
    element = doc.GetElement(selection_reference)
    return element