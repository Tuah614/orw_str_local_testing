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

def get_all_generic_annotation_symbols():
    '''Generic annotation collector'''
    annotion_symbol_collector = FilteredElementCollector(doc).\
                            OfCategory(BuiltInCategory.OST_GenericAnnotation).\
                            OfClass(FamilySymbol).\
                            ToElements()  # type: AnnotationSymbolType
    return annotion_symbol_collector

def get_annotation_symbol_by_names(family_names):
    '''Generic annotation collector, filtered by names'''
    annotion_symbol_collector = FilteredElementCollector(doc).\
                                OfCategory(BuiltInCategory.OST_GenericAnnotation).\
                                OfClass(FamilySymbol).\
                                ToElements() #AnnotationSymbolType
    valid_family = []
    for symbol in annotion_symbol_collector:
        fam_name = symbol.FamilyName
        for n in family_names:
            if n == fam_name:
                valid_family.append(symbol)
    return  valid_family

def family_exist_by_names(collected_family, family_names):
    '''Check if the family names exists in the family collector'''
    collected_family_names = []
    checks = []
    missing_names = []
    for fam in collected_family:
        collected_family_names.append(fam.FamilyName)
    for name in family_names:
        if name not in collected_family_names:
            checks.append(False)
            missing_names.append(name)
        else:
            checks.append(True)

    res = all(checks)
    return res, missing_names

def get_elements_by_category_from_view(doc, category, view_id):
    from Autodesk.Revit.DB import FilteredElementCollector
    collector = FilteredElementCollector(doc, view_id)\
                .OfCategory(category)\
                .WhereElementIsNotElementType()\
                .ToElements()
    return collector