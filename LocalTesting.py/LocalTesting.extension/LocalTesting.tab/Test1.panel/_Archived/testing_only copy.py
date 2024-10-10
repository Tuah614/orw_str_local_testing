from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application

selection = uidoc.Selection

ref_seletion = selection.PickObject(ObjectType.Element)
picked_element = doc.GetElement(ref_seletion)

print(picked_element)