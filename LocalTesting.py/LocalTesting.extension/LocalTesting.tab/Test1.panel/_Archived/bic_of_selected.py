from Autodesk.Revit.DB import BuiltInCategory
import clr
clr.AddReference("System")  # Make sure this is included before the import
from System import Enum
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application

selection = uidoc.Selection

ref_selection = selection.PickObject(ObjectType.Element)
picked_element = doc.GetElement(ref_selection)
cat_id = picked_element.Category.Id.IntegerValue

bic_enum = Enum.GetValues(BuiltInCategory)

bics = []
bics_as_int = []

for bic in bic_enum:
    try:
        bics.append(bic.ToString())
        bics_as_int.append(int(bic))
    except:
        pass  

selected_bic = "Not found!"
for i, j in zip(bics, bics_as_int):
    try:
        if cat_id == j:
            selected_bic = i
    except:
        break

# OUTPUT
print(selected_bic)