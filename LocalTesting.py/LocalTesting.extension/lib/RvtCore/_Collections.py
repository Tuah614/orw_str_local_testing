# -*- coding: utf-8 -*-

# imports
import re
from Autodesk.Revit.DB import Document, BindingMap, DefinitionBindingMapIterator

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ==================================================

def sort_panel_types_alphanumeric(p_type):
    '''
    Custom alphanumeric sorting logic
    '''
    match = re.match(r"([A-Za-z]+)(\d+)", p_type)
    if match:
        alpha, numeric = match.groups()
        return (alpha.isdigit(), alpha, int(numeric))
    return (p_type,)

def find_duplicate_parameters(doc): # type: (Document) -> (set[str], bool)
    '''
    Find duplicate parameters by accessing definition names
    '''
    binding_map = doc.ParameterBindings # type: BindingMap
    iterator = binding_map.ForwardIterator() # type: DefinitionBindingMapIterator
    iterator.Reset()

    parameter_names = []

    while iterator.MoveNext():
        definition_name = iterator.Key.Name
        parameter_names.append(definition_name)

    duplicates, has_duplicates = find_duplicate_strings(parameter_names)
    return duplicates, has_duplicates

def find_duplicate_strings(str_list):
    '''
    Find duplicate in a given list of strings
    Returns a list of duplicates and return true if indeed there is a duplicate
    '''
    seen = set()
    duplicates = set()
    
    for str in str_list:
        if str in seen:
            duplicates.add(str)
        else:
            seen.add(str)

    has_duplicates = len(duplicates) > 0

    return duplicates, has_duplicates