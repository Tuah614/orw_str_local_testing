# -*- coding: utf-8 -*-

# imports
import re
from Autodesk.Revit.DB import *
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

def find_duplicate_parameters(doc): # type: (Document) -> (Dict, bool)
    '''
    Find duplicate shared parameters in the current project
    Return bool state of the operation and parameters in dictionary
    '''
    parameters_by_key = {}
    existing_parameter_bindings = doc.ParameterBindings
    param_bindings_iterator = existing_parameter_bindings.ForwardIterator()
    param_bindings_iterator.Reset()
    while param_bindings_iterator.MoveNext():
        current = doc.GetElement(param_bindings_iterator.Key.Id)
        if isinstance(current, SharedParameterElement):
            param_name = current.Name
            if param_name not in parameters_by_key:
                parameters_by_key[param_name] = []
            parameters_by_key[param_name].append(current)

    invalid_param_names = [] # invalid is for no duplicates
    for key, values in parameters_by_key.items():
        if len(values) <= 1:
            invalid_param_names.append(key)
    
    # remove invalid param from dictionary
    for name in invalid_param_names:
        del parameters_by_key[name]

    # bool flag for duplicate status
    has_duplicates = False
    if len(invalid_param_names) > 0:
        has_duplicates = True

    return has_duplicates, parameters_by_key

def find_duplicate_parameter_names(doc): # type: (Document) -> (set(str), bool)
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