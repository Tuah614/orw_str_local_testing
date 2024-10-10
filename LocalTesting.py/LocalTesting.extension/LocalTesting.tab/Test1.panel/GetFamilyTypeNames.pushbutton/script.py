from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit, forms

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
selection = uidoc.Selection

LEVELNAMEFAMNAME = "ACM_DET_Level Names" # type = Levels
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
LAYERPROPERTYTYPES = [LP1, LP2, LP3, LP4, LP5 ,LP6]

collector = FilteredElementCollector(doc)\
            .OfCategory(BuiltInCategory.OST_GenericAnnotation)\
            .OfClass(FamilySymbol)\
            .WhereElementIsElementType()\
            .ToElements()

rl_symbols = []
lp_symbols = []

for ele in collector:
    ele_name = Element.Name.__get__(ele)
    for n in REBARLAYERTYPES:
        if n == ele_name:
            rl_symbols.append(ele)
    for m in LAYERPROPERTYTYPES:
        if m == ele_name:
            lp_symbols.append(ele)

# for rl in rl_symbols:
#     rl_name = Element.Name.__get__(rl)
    # print("{0}: {1}".format(rl_name, rl))

# for lp in lp_symbols:
#     lp_name = Element.Name.__get__(lp)
    # print("{0}: {1}".format(lp_name, lp))

layers_per_level = [3, 3, 3, 6]
rl_symbol_to_place = []

for nos in layers_per_level:
    if 1 <= nos <= 6:
        rl_symbol_to_place.append(rl_symbols[nos -1])
        print("{0}: {1}". format(nos, rl_symbols[nos -1]))
    else:
        rl_symbol_to_place.append(None)
        print("{0}: No matching symbol found".format(nos))

