# -*- coding: utf-8 -*-
__title__ = "Generate Coupler Schedule" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit, forms
from collections import OrderedDict
import json

# ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
# ║  ║ ║║║║╚═╗ ║ ╠═╣║║║ ║ ╚═╗
# ╚═╝╚═╝╝╚╝╚═╝ ╩ ╩ ╩╝╚╝ ╩ ╚═╝ CONSTANTS
# ==================================================

PANELTYPEPARAMETERNAME = "ACM_DWALL_Panel Type"
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
PARAMNAMES = ["Layer 1", "Layer 2", "Layer 3", "Layer 4", "Layer 5", "Layer 6"]

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
selection = uidoc.Selection #type: Selection

# ===============================================================================
# 👩‍👩‍👧   FAMILY SYMBOLS MAPPER
# ===============================================================================

annotation_symbol_collector = FilteredElementCollector(doc).\
                                OfCategory(BuiltInCategory.OST_GenericAnnotation).\
                                OfClass(FamilySymbol).\
                                WhereElementIsElementType().\
                                ToElements()
rl_symbols = []
lp_symbols = []

for ele in annotation_symbol_collector:
    ele_name = Element.Name.__get__(ele)
    for n in REBARLAYERTYPES:
        if n == ele_name:
            rl_symbols.append(ele)
    for m in LAYERPROPERTYTYPES:
        if m == ele_name:
            lp_symbols.append(ele)

# sort symbol lists due to mapper behavior
rl_symbols.sort(key=lambda x: Element.Name.__get__(x)) 
lp_symbols.sort(key=lambda x: Element.Name.__get__(x))

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ==================================================

def pick_single_element(doc, uidoc):
    selection_reference = uidoc.Selection.PickObject(ObjectType.Element)
    element = doc.GetElement(selection_reference)
    return element

def get_endpoint_as_xyz(detail_line):
    end_point = detail_line.GeometryCurve.GetEndPoint(1)
    return end_point

def convert_internal_to_millimeter(internal_unit_value):
    converted_unit = UnitUtils.ConvertFromInternalUnits(internal_unit_value, UnitTypeId.Millimeters)
    return converted_unit

def convert_millimeter_to_internal(project_unit_value):
    converted_unit = UnitUtils.ConvertToInternalUnits(project_unit_value, UnitTypeId.Millimeters)
    return converted_unit

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

def pick_single_element(doc, uidoc):
    selection_reference = uidoc.Selection.PickObject(ObjectType.Element)
    element = doc.GetElement(selection_reference)
    return element

def get_builtin_param(element, bip):
    param = element.get_Parameter(bip)
    return param

def get_shared_param(element, param_name):
    param = element.LookupParameter(param_name)
    return param

def get_elements_by_category_from_view(doc, category, view_id):
    from Autodesk.Revit.DB import FilteredElementCollector
    collector = FilteredElementCollector(doc, view_id)\
                .OfCategory(category)\
                .WhereElementIsNotElementType()\
                .ToElements()
    return collector

# ===============================================================================
# ✅   CHECK IF FAMILY IS LOADED IN PROJECT
# ===============================================================================

#check for required family exist in the project
family_type_collector = FilteredElementCollector(doc)\
                        .OfCategory(BuiltInCategory.OST_GenericAnnotation)\
                        .OfClass(FamilySymbol)\
                        .WhereElementIsElementType()\
                        .ToElementIds()

project_family_type_name = []

for id in family_type_collector:
    element = doc.GetElement(id)
    type_name = Element.Name.__get__(element)
    project_family_type_name.append(type_name)

missing_types = []

for rebar_type in REBARLAYERTYPES:
    if rebar_type not in project_family_type_name:
        missing_types.append(rebar_type)

for layer_type in LAYERPROPERTYTYPES:
    if layer_type not in project_family_type_name:
        missing_types.append(layer_type)

if missing_types:
    alert_message = forms.alert("Please ensure required families are loaded in the project\
                                Author: Tuah Hamid",
                                exitscript=True)


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

# ===============================================================================
# 👓   PROMPT JSON FILE
# ===============================================================================

source_file = forms.pick_file(file_ext='json')
with open(source_file, 'r') as schema:
    schema_data_ordered = json.load(schema, object_pairs_hook=OrderedDict)
schema_data_standard = dict(schema_data_ordered)

# count level occurences in each panel type, terminate if more than one unique values
panel_data_as_list = schema_data_ordered.values()
panel_data_counts = []
for panel in panel_data_as_list:
    panel_data_counts.append(len(panel))

panel_unique_counts_set = list(set(panel_data_counts))
panel_unique_count = len(panel_unique_counts_set)

if panel_unique_count != 1:
    forms.alert("Count error in levels", exitscript=True)
else:
    LEVELCOUNT = panel_unique_counts_set[0]

# ===============================================================================
# GENERATE BOOLEANS FOR HEADER VISIBILITY, LEVEL NAMES, LAYER NAMES, LAYER VALUES
# ===============================================================================

level_names = []
layers_per_level = []
layer_values = []
for level, prop in panel_data_as_list[0].items():
    level_names.append(level)
    layers_per_level.append(prop['Number of layers'])
    layer_values.append(prop['Layer values'])

allow_header_bool_values = []
for i in range(LEVELCOUNT):
    if i == 0:
        allow_header_bool_values.append(1)
    else:
        allow_header_bool_values.append(0)

# ==================================================
# GENERATE POINTS FOR LEVEL NAME FAMILY PLACEMENT
# ==================================================

selected_detail_line = pick_single_element(doc, uidoc)
original_point = get_endpoint_as_xyz(selected_detail_line)
rl_first_instance_distance = convert_millimeter_to_internal(40)
rl_first_instance_point = XYZ(original_point.X - rl_first_instance_distance,
                              original_point.Y, original_point.Z)
ln_first_instance_distance = convert_millimeter_to_internal(30)
ln_first_instance_point = XYZ(original_point.X - rl_first_instance_distance - ln_first_instance_distance,
                              original_point.Y, original_point.Z)

# ln points
ln_points = []
ln_Y_subtotal_points = XYZ.Zero.Y
for i, j in zip(range(LEVELCOUNT), layers_per_level):
    if i == 0:
        ln_points.append(ln_first_instance_point)
    else:
        multiplier = layers_per_level[i-1]
        ln_Y_subtotal_points = ln_Y_subtotal_points + convert_millimeter_to_internal(6 * multiplier)
        ln_new_point = XYZ(ln_first_instance_point.X,
                    ln_first_instance_point.Y - ln_Y_subtotal_points,
                    ln_first_instance_point.Z)
        ln_points.append(ln_new_point)

# ==================================================
# 👩‍👩‍👧   GET LEVEL NAME FAMILY SYMBOL
# ==================================================

ln_fs = get_family_symbols_by_names(doc, ["Levels"])

# ==================================================
# ✨   GENERATE POINTS FOR REBAR LAYER FAMILY PLACEMENT
# ==================================================
rl_points = []
rl_Y_subtotal_points = XYZ.Zero.Y
for i, j in zip(range(LEVELCOUNT), layers_per_level):
    if i == 0:
        rl_points.append(rl_first_instance_point)
    else:
        multiplier = layers_per_level[i-1]
        rl_Y_subtotal_points = rl_Y_subtotal_points + convert_millimeter_to_internal(6 * multiplier)
        rl_new_point = XYZ(rl_first_instance_point.X,
                    rl_first_instance_point.Y - rl_Y_subtotal_points,
                    rl_first_instance_point.Z)
        rl_points.append(rl_new_point)

# ==================================================
# ✨  GENERATE POINTS FOR LAYER PROPERTIES FAMILY PLACEMENT
# ==================================================

panel_lengths = []
panel_types = []
panel_marks = []

for i in sorted(selected_dwall_info.keys()):
    panel_marks.append(i)
    panel_lengths.append(selected_dwall_info[i][1])
    panel_types.append(selected_dwall_info[i][2])

lp_points = []
X_distance = 0
Y_distance = 0
for m, length in zip(range(len(panel_marks)), panel_lengths):
    if m == 0:
        lp_X = original_point.X
    else:
        X_distance = X_distance + convert_millimeter_to_internal(panel_lengths[m -1]/100)
        lp_X = original_point.X + X_distance
    lp_header_point = XYZ(lp_X, original_point.Y, original_point.Z)

    lp_columns = []
    for i, j in zip(range(LEVELCOUNT), layers_per_level):
        if i == 0:
            lp_columns.append(lp_header_point)
        else:
            Y_multiplier = layers_per_level[i-1]
            Y_distance = Y_distance + convert_millimeter_to_internal(6 * Y_multiplier)
            lp_new_point = XYZ(lp_header_point.X, 
                               lp_header_point.Y - Y_distance,
                               lp_header_point.Z)
            lp_columns.append(lp_new_point)
    lp_points.append(lp_columns)
    Y_distance = 0


# ==================================================
# 👩‍👩‍👧   PLACE ALL FAMILY INTANCES
# ==================================================

main_key = next(iter(schema_data_standard))
sub_key = next(iter(schema_data_standard[main_key]))

with Transaction(doc, __title__) as t:
    t.Start()
    try:
        # PLACE LN FAMILY
        for point, header_val, layer_val, level_name in zip(ln_points, allow_header_bool_values, layers_per_level, level_names):
            try:
                new_ln_fam_instance = doc.Create.NewFamilyInstance(point, ln_fs[0], doc.ActiveView)
                new_ln_fam_instance.LookupParameter("Allow Header").Set(header_val)
                new_ln_fam_instance.LookupParameter("Dwall Length").Set(convert_millimeter_to_internal(3000))
                new_ln_fam_instance.LookupParameter("Layers per Level").Set(layer_val)
                new_ln_fam_instance.LookupParameter("Level Name").Set(level_name.upper())
            except:
                print("Error placing LN family at {0}".format(level_name))

        # PLACE RL FAMILY
        for point, header_val, level_name, layer_val in zip(rl_points, allow_header_bool_values, level_names, layers_per_level):
            if 1 <= layer_val <= 6:
                symbol = rl_symbols[layer_val - 1]
                try:
                    new_rl_fam_instance = doc.Create.NewFamilyInstance(point, symbol, doc.ActiveView)
                    new_rl_fam_instance.LookupParameter("Allow Header").Set(header_val)
                    new_rl_fam_instance.LookupParameter("Level Ownership").Set(level_name.upper())

                    layer_names = schema_data_standard[main_key][level_name]["Layer names"]
                    for i in range(len(layer_names)):
                        layer_param_name = "Layer {}".format(i + 1)
                        if i < len(layer_names):
                            layer_param_value = layer_names[i]
                        else:
                            layer_param_value = "-"
                        new_rl_fam_instance.LookupParameter(layer_param_name).Set(layer_param_value)
                except:
                    print("Error placing RL family at {0}".format(level_name))
        # PLACE LP FAMILY
        for mark, length, typ, pt_list in zip(panel_marks, panel_lengths, panel_types, lp_points):
            for pt, header_val, level_name, layer_val in zip(pt_list, allow_header_bool_values, level_names, layers_per_level):
                if 1 <= layer_val <= 6:
                    symbol = lp_symbols[layer_val - 1]
                    try:
                        new_lp_fam_instance = doc.Create.NewFamilyInstance(pt, symbol, doc.ActiveView)
                        new_lp_fam_instance.LookupParameter("Allow Header").Set(header_val)
                        new_lp_fam_instance.LookupParameter("Level Ownership").Set(level_name.upper())
                        new_lp_fam_instance.LookupParameter("Dwall Mark").Set(mark)
                        new_lp_fam_instance.LookupParameter("Dwall Coupler Type").Set(typ)
                        new_lp_fam_instance.LookupParameter("Dwall Length").Set(convert_millimeter_to_internal(length))

                        if typ in schema_data_standard.keys():
                            layer_properties = schema_data_standard[typ][level_name]["Layer values"]
                        for i in range(len(layer_properties)):
                            layer_param_name = "Layer {}".format(i + 1)
                            if i < len(layer_properties):
                                layer_param_value = layer_properties[i]
                            else:
                                layer_param_value = "-"
                            new_lp_fam_instance.LookupParameter(layer_param_name).Set(layer_param_value)
                    except:
                        print("Error placing LP family at {0}".format(mark))


        t.Commit()
    except:
        print("Something went wrong")
        t.Rollback()