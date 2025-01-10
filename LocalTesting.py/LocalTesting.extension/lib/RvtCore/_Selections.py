# -*- coding: utf-8 -*-

# imports
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from Autodesk.Revit.ApplicationServices import Application
from Autodesk.Revit.UI import UIDocument
from Autodesk.Revit.UI.Selection import Selection, ISelectionFilter

# variables
doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument #type: UIDocument
app = __revit__.Application #type: Application

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ==================================================

class CustomISelectionFilter_Category(ISelectionFilter):
    """Filter selection by category name"""
    def __init__(self, category_name):
        self.category_name = category_name

    def AllowElement(self, elem): # type: (Element) -> bool
        selected_elem_id = elem.Category.Id
        if elem.Category and str(selected_elem_id) == str(self.category_name):
            return True
        return False
    
    def AllowReference(self, reference, position):
        """Not used"""
        return False
    
class CustomISelectionFilter_Class(ISelectionFilter):
    """Filter selection by class"""
    def __init__(self, allowed_class): 
        self.allowed_class = allowed_class
    
    def AllowElement(self, elem):
        if type(elem) == self.allowed_class:
            return True
        return False

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