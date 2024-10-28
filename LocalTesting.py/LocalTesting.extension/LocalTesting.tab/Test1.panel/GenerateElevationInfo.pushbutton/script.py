# -*- coding: utf-8 -*-
__title__ = "Generate Elevation Information" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit, forms
from RvtCore import _Collectors, _Selections, _UnitHandler

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

# place elevation header family
eh_family_collector = _Collectors.get_family_by_names(doc ,[ELEVATION_HEADER_200_FAMNAME]) # type: Family
if len(eh_family_collector) == 1:
    eh_family = eh_family_collector[0]

print(eh_family)
print(eh_family.GetTypeId())
print(eh_family.GetValidTypes()[0])
# print(type(eh_symbol))