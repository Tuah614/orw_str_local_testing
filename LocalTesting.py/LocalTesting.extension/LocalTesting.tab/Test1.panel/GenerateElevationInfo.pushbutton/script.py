# -*- coding: utf-8 -*-
__title__ = "Generate Elevation Information" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit, forms
from RvtCore import _Collectors, _Selections, _UnitHandler
# from typing import List, Tuple

# ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
# ║  ║ ║║║║╚═╗ ║ ╠═╣║║║ ║ ╚═╗
# ╚═╝╚═╝╝╚╝╚═╝ ╩ ╩ ╩╝╚╝ ╩ ╚═╝ CONSTANTS

SCHEDULE_HEADER_200_FAMNAME = "ACM_DET_Dwall Schedule Header_Scale 200"
ELEVATION_HEADER_200_FAMNAME = "ACM_DET_Elevation Header_Scale 200"
ELEVATION_INFORMATION_200_FAMNAME = "ACM_DET_Elevation Information_Scale 200"
REQUIRED_FAMILY_NAMES = [SCHEDULE_HEADER_200_FAMNAME, 
                         ELEVATION_HEADER_200_FAMNAME, 
                         ELEVATION_INFORMATION_200_FAMNAME]
SH1 = "Standard Header"

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
selection = uidoc.Selection #type: Selection

# ╔═╗╔═╗╔╦╗╔═╗
# ║ ╦╠═╣ ║ ║╣ 
# ╚═╝╩ ╩ ╩ ╚═╝ GATE
# ==================================================

#check if the require families exist in the current document
all_generic_annotations = _Collectors.get_all_generic_annotation_symbols(doc)
family_is_exist, missing_families = _Collectors.family_exist_by_names(all_generic_annotations, REQUIRED_FAMILY_NAMES)
if not family_is_exist:
    missing_family_termination = forms.alert("Missing families: {}".format(str.join(", ", missing_families)),
                                             exitscript=True)
    
# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================

# get dwall from selected viewport
selected_viewport = _Selections.pick_single_element(doc, uidoc)
dwalls_in_view = _Collectors.get_elements_by_category_from_view(doc, 
                                                                BuiltInCategory.OST_StructuralFoundation, 
                                                                selected_viewport.ViewId)
# generate mark mapping for all dwall. 
valid_dwalls = {}
for visible_dwall in dwalls_in_view:
    param = visible_dwall.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).AsString()
    if param is not None:
        try:
            valid_dwalls[param] = visible_dwall
        except:
            pass

# filter dwall based on user selection
mark_selection_res = forms.SelectFromList.show(sorted(valid_dwalls.keys()), multiselect=True, button_name = "Select panels")
selected_dwall = {}
for key in mark_selection_res:
    if key in valid_dwalls:
        selected_dwall[key] = valid_dwalls[key]

# add length and panel type values to dwall selection
selected_dwall_info = {}
for key, dwall in selected_dwall.items():
    length_param = dwall.get_Parameter(BuiltInParameter.STRUCTURAL_FOUNDATION_LENGTH) # type: Parameter
    panel_type_param = dwall.LookupParameter("ACM_DWALL_Panel Type") # type: Parameter
    
    length_value = None
    panel_type_value = None

    if length_param is not None:
        length_value = _UnitHandler.convert_internal_to_millimeter(length_param.AsDouble())
    if panel_type_param is not None:
        panel_type_value = panel_type_param.AsString()
    selected_dwall_info[key] = [dwall, length_value, panel_type_value]

# prompt detail line as reference point
selected_detail_line = _Selections.pick_single_element(doc, uidoc) # type: DetailLine
original_point = _Selections.get_endpoint_as_xyz(selected_detail_line)

# get elevation header family symbol
eh_symbol = None
eh_family_collector = _Collectors.get_family_by_names(doc ,[ELEVATION_HEADER_200_FAMNAME]) # type: List[Family]
for family in eh_family_collector:
    symbol_ids = family.GetFamilySymbolIds()
    for id in symbol_ids:
        symbol = doc.GetElement(id)
        symbol_name = Element.Name.__get__(symbol)
        if symbol_name == SH1:
            eh_symbol = symbol

# get elevation information family symbol
ei_symbol = None
ei_family_collector = _Collectors.get_family_by_names(doc, [ELEVATION_INFORMATION_200_FAMNAME])
for family in ei_family_collector:
    symbol_ids = family.GetFamilySymbolIds()
    for id in symbol_ids:
        symbol = doc.GetElement(id)
        symbol_name = Element.Name.__get__(symbol)
        if symbol_name == SH1:
            ei_symbol = symbol

# get schedule header family symbol
sh_symbol = None
sh_family_collector = _Collectors.get_family_by_names(doc, [SCHEDULE_HEADER_200_FAMNAME])
for family in sh_family_collector:
    symbol_ids = family.GetFamilySymbolIds()
    for id in symbol_ids:
        symbol = doc.GetElement(id)
        symbol_name = Element.Name.__get__(symbol)
        if symbol_name == SH1:
            sh_symbol = symbol

# generate parameters for schedule header family placement
panel_marks = []
panel_lengths = []
panel_types = []

for i in sorted(selected_dwall_info.keys()):
    panel_marks.append(i)
    panel_lengths.append(selected_dwall_info[i][1])
    panel_types.append(selected_dwall_info[i][2])

X_distance = 0
sh_points = []
for m, length in zip(range(len(panel_marks)), panel_lengths):
    if m == 0:
        sh_X = original_point.X
    else:
        X_distance = X_distance + _UnitHandler.convert_millimeter_to_internal(panel_lengths[m-1]/200)
        sh_X = original_point.X + X_distance
    sh_point = XYZ(sh_X, original_point.Y, original_point.Z)
    sh_points.append(sh_point)

# place annotation families
with Transaction(doc, __title__) as t:
    t.Start()
    try:
        for mark, length, typ, point in zip(panel_marks, panel_lengths, panel_types, sh_points):
            new_sh_fam_instance = doc.Create.NewFamilyInstance(point, sh_symbol, doc.ActiveView) # type: Element
            new_sh_fam_instance.LookupParameter("Dwall Mark").Set(mark)        
            new_sh_fam_instance.LookupParameter("Dwall Coupler Type").Set(typ)
            new_sh_fam_instance.LookupParameter("Dwall Length").Set(_UnitHandler.convert_millimeter_to_internal(length))
        new_eh_fam_instance = doc.Create.NewFamilyInstance(original_point, eh_symbol, doc.ActiveView)
        new_ei_fam_instance = doc.Create.NewFamilyInstance(original_point, ei_symbol, doc.ActiveView) # type: Element
        new_ei_fam_instance.LookupParameter("Column Width").Set(_UnitHandler.convert_millimeter_to_internal(sum(panel_lengths)/200))
        t.Commit()
    except:
        print("Error placing EH family")
        t.RollBack()