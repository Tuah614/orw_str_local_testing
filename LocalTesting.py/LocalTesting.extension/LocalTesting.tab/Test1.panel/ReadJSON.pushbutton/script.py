# -*- coding: utf-8 -*-
__title__ = "Generate Coupler Schedule" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit, forms
from collections import OrderedDict
import json

PANELTYPEPARAMETERNAME = "Panel Type"
DWALLLENGTHPARAM = BuiltInParameter.STRUCTURAL_FOUNDATION_LENGTH
LEVELNAMEFAMNAME = "ACM_DET_Level Names"
LN1 = "Levels"
REBARLAYERFAMNAME = "ACN_DET_Rebar Layer"
RL1 = "1 - One Row"
RL2 = "2 - Two Row"
RL3 = "3 - Three Row"
RL4 = "4 - Four Row"
RL5 = "5 - Five Row"
RL6 = "6 - Six Row"
REBARLAYERTYPES = [RL1, RL2, RL3, RL4, RL5, RL6]
LAYERPROPERTYFAMNAME = "ACM_DET_Layer Properties"
LP1 = "1 - One Layer"
LP2 = "2 - Two Layers"
LP3 = "3 - Three Layers"
LP4 = "4 - Four Layers"
LP5 = "5 - Five Layers"
LP6 = "6 - Six Layers"
LAYERPROPERTYTYPES = [LP1, LP2, LP3, LP4, LP5, LP6]
ROWHEIGHT = 6 #in mm

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
selection = uidoc.Selection

def pick_single_element(doc, uidoc):
    selection_reference = uidoc.Selection.PickObject(ObjectType.Element)
    element = doc.GetElement(selection_reference)
    return element

def get_endpoint_as_xyz(detail_line):
    end_point = detail_line.GeometryCurve.GetEndPoint(1)
    return end_point

def get_elements_by_category_from_view(doc, category, view_id):
    from Autodesk.Revit.DB import FilteredElementCollector
    collector = FilteredElementCollector(doc, view_id)\
                .OfCategory(category)\
                .WhereElementIsNotElementType()\
                .ToElements()
    return collector

def get_builtin_param(element, bip):
    param = element.get_Parameter(bip)
    return param

def get_shared_param(element, param_name):
    param = element.LookupParameter(param_name)
    return param

def convert_internal_to_millimeter(internal_unit_value):
    converted_unit = UnitUtils.ConvertFromInternalUnits(internal_unit_value, UnitTypeId.Millimeters)
    return converted_unit

def convert_millimeter_to_internal(project_unit_value):
    converted_unit = UnitUtils.ConvertToInternalUnits(project_unit_value, UnitTypeId.Millimeters)
    return converted_unit

def convert_to_one_one_hundred(length_mm):
    scaled_unit = length_mm / 100
    return scaled_unit

def get_family_symbols_by_names(doc, symbol_names):
    collector = FilteredElementCollector(doc).\
                OfCategory(BuiltInCategory.OST_GenericAnnotation).\
                OfClass(FamilySymbol).\
                WhereElementIsElementType().\
                ToElements()
    family_symbols = []
    for element in collector:
        if Element.Name.__get__(element) in symbol_names:
            family_symbols.append(element)
    family_symbols.sort(key=lambda x: symbol_names.index(Element.Name.__get__(x)))
    return family_symbols

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================

#get dwall from selected viewport
selected_viewport = pick_single_element(doc, uidoc)
elements = get_elements_by_category_from_view(doc, 
                                              BuiltInCategory.OST_StructuralFoundation, 
                                              selected_viewport.ViewId)

# generate dwall mark and dwall element mapping

valid_dwall = {}

for e in elements:
    param = e.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).AsString()
    if param is not None:
        try:
            valid_dwall[param] = e
        except:
            pass

#filter dwall based on user selection

res = forms.SelectFromList.show(sorted(valid_dwall.keys()), 
                                multiselect=True, 
                                button_name='Select Type')

selected_dwall = {}
for key in res:
    if key in valid_dwall:
        selected_dwall[key] = valid_dwall[key]

# refine dwall data by adding length and panel type values NOTEz that panel type parameter may varies from project

selected_dwall_info = {}

for key, dwall in selected_dwall.items():
    length_param = get_builtin_param(dwall, DWALLLENGTHPARAM)
    panel_type_param = get_shared_param(dwall, PANELTYPEPARAMETERNAME)

    length_value = None
    panel_type_value = None

    if length_param is not None:
        length_value = convert_internal_to_millimeter(length_param.AsDouble()) 

    if panel_type_param is not None:
        panel_type_value = panel_type_param.AsString()

    selected_dwall_info[key] = [dwall, length_value, panel_type_value]

source_file = forms.pick_file(file_ext='json')
with open(source_file, 'r') as schema:
    schema_data_ordered = json.load(schema, object_pairs_hook=OrderedDict)
schema_data_standard = dict(schema_data_ordered)

# count level occurences in each panel type, terminate if more than one unique values
panel_data_as_list = schema_data_ordered.values()
print("Number of panels in JSON: {0}".format(len(panel_data_as_list)))
panel_data_counts = []
for panel in panel_data_as_list:
    panel_data_counts.append(len(panel))
print("Number of levels in each panel type: {0}".format(panel_data_counts))

panel_unique_counts_set = list(set(panel_data_counts))
panel_unique_count = len(panel_unique_counts_set)

if panel_unique_count != 1:
    forms.alert("Level count error in one of the panel types", exitscript=True)
else:
    LEVELCOUNT = panel_unique_counts_set[0]

# ==================================================
# GENERATE LEVEL NAME DATA FOR FAMILY PLACEMENT
# ==================================================

main_key = next(iter(schema_data_standard))
sub_key = next(iter(schema_data_standard[main_key]))

level_names = []
layers_per_level = []
layer_values = []
for level, prop in panel_data_as_list[0].items():
    level_names.append(level)
    layers_per_level.append(prop['Number of layers'])
    # print("{0} - {1} - {2} - {3}".format(level, 
    #                          prop['Number of layers'], 
    #                          prop['Layer names'], 
    #                          prop['Layer values']))

# for i in sorted(selected_dwall_info.keys()):
#     print(selected_dwall_info[i])

typ = ["B2", "C1"]
print(schema_data_standard.keys())
for t in typ:
    for level_name in level_names:
        layer_properties = schema_data_standard[t][level_name]["Layer values"]
        print("{0} - {1} - {2}".format(t, level_name, layer_properties))