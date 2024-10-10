from Autodesk.Revit.DB import *
from pyrevit import revit, forms

### CONSTANTS ###
PANELTYPEPARAMETERNAME = "Panel Type"
DWALLLENGTHPARAM = BuiltInParameter.STRUCTURAL_FOUNDATION_LENGTH

### MAIN VARIABLES ###
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
selection = uidoc.Selection

### FUNCTIONS ###

def family_symbol_by_name(doc, cat):
    collector = FilteredElementCollector(doc).OfCategory(cat).WhereElementIsElementType()
    
    family_symbols = []
    for element in collector:
        if isinstance(element, FamilySymbol):
            eName = Element.Name.__get__(element)  
            fName = ElementType.FamilyName.__get__(element)  
            id = element.Id  
            family_symbols.append((eName, fName, id)) 

    return family_symbols

### MAIN SCRIPT ###

res = family_symbol_by_name(doc, BuiltInCategory.OST_GenericAnnotation)

# Iterate over the returned list of tuples
for eName, fName, id in res:
    print("{0} - {1} - {2}".format(eName, fName, id))
