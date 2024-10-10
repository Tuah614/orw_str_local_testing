from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit, forms

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
selection = uidoc.Selection
active_view = doc.ActiveView

name = active_view.SheetNumber
print(name)

