# -*- coding: utf-8 -*-
__title__ = "Get Affected Elements" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from Autodesk.Revit.UI import UIDocument
from RvtCore import _Collections, _Collectors, _UnitHandler
from Autodesk.Revit.DB import Document
from Autodesk.Revit.ApplicationServices import Application, ControlledApplication
from pyrevit import forms

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument # type: UIDocument
app = __revit__.Application #type: Application
selection = uidoc.Selection #type: Selection

'''Allow user to select parameter from SH file to compare with active document'''
# create dict data for existing parameters
sp_file = app.OpenSharedParameterFile() # type: DefinitionFile
dict_sp = {}
sp_groups = sp_file.Groups # type: DefinitionGroups
for group in sp_groups:
    for param_def in group.Definitions:
        param_names = '[{0}] - {1}'.format(group.Name, param_def.Name)
        dict_sp[param_names] = param_def

# allow selection based on dict data
selection_result = forms.SelectFromList.show(sorted(dict_sp.keys()),
                                    multiselect = True,
                                    button_name = 'Select parameters')

selected_param = {}
for result in selection_result:
    if result in dict_sp:
        selected_param[result] = dict_sp[result]

# get guid values for main parameters to check
param_guid = {}
for name, param in selected_param.items():
    guid = str(param.GUID)
    param_guid[guid] = selected_param[name]

'''Get all parameter bindings and get duplicates if any'''
# get all project parameters in the current project

has_duplicates, dict_duplicates = _Collections.find_duplicate_parameters(doc) # 
# existing_param_bindings = doc.ParameterBindings
# bindings_iterator = existing_param_bindings.ForwardIterator()
# bindings_iterator.Reset()
# while bindings_iterator.MoveNext():
#     current = doc.GetElement(bindings_iterator.Key.Id)
#     if isinstance(current, SharedParameterElement):
#         param_name = current.Name
#         if param_name not in dict_duplicates:
#             dict_duplicates[param_name] = []
#         dict_duplicates[param_name].append(current)

print(has_duplicates)  

for key, values in dict_duplicates.items():
    print("NAME: {}".format(key))
    for v in values:
        print("GUID: {}".format(v.GuidValue))
    print("\n ")

'''This is for parameter binding checking only'''
for key, values in dict_duplicates.items():
    if len(values) > 1:
        print("Parameter Key Name -- {0}".format(key))
        for v in values:
            print("GUIDS - {0} --- {1}".format(v.GuidValue, key))
        print("\n ")

'''check parameter duplicates in family instances and curve driven elements'''
# get all family instance
all_family_instances = FilteredElementCollector(doc).\
                        OfClass(FamilyInstance).\
                        WhereElementIsNotElementType().\
                        ToElements()
print(len(all_family_instances))

sample_instance1 = all_family_instances[1000]
family_symbol = sample_instance1.Symbol
symbol_name = Element.Name.__get__(family_symbol)
family_name = family_symbol.FamilyName
category_name = sample_instance1.Category.Name
print("SYMBOL: {0} -- FAMNAME: {1} -- CAT: {2}".format(symbol_name, family_name, category_name))
instance_parameter_iterator = sample_instance1.Parameters.ForwardIterator()
instance_parameter_iterator.Reset()
while instance_parameter_iterator.MoveNext():
    current = instance_parameter_iterator.Current
    if current.IsShared:
        param_name = current.Definition.Name
        param_guid = current.GUID

        print("Name: {0} -- GUID: {1}".format(param_name, param_guid))

    


# unique_cats_fam = set()
# for ele in all_family_instances:
#     unique_cats_fam.add(ele.Category.Name)
#     parameters_iterator = ele.Parameters.ForwardIterator()
#     parameters_iterator.Reset()
#     while parameters_iterator.MoveNext():
#         parameters_iterator.Current.Key


#get all curve drivent elements
all_other_instances = FilteredElementCollector(doc).WhereElementIsCurveDriven().ToElements()
print(len(all_other_instances))

unique_cats_other = set()
for ele in all_other_instances:
    unique_cats_other.add(ele.Category.Name)
