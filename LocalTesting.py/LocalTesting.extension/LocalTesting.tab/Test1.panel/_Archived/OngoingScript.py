from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit, forms

### CONSTANST ###

PANELTYPEPARAMETERNAME = "Panel Type"
DWALLLENGTHPARAM = BuiltInParameter.STRUCTURAL_FOUNDATION_LENGTH

### MAIN VARIABLES ###

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
selection = uidoc.Selection

### FUNCTIONS ###

def pick_single_element(doc, uidoc):
    selection_reference = uidoc.Selection.PickObject(ObjectType.Element)
    element = doc.GetElement(selection_reference)
    return element

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

def convert_to_one_one_hundred(length_mm):
    scaled_unit = length_mm / 100
    return scaled_unit

### MAIN SCRIPT ###

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

selected_dwall_info = {}
# refine dwall data by adding length and panel type values NOTEz that panel type parameter may varies from project
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

for key in sorted(selected_dwall_info.keys()):
    val = selected_dwall_info[key]
    print("{0}-{1}".format(key, val))
