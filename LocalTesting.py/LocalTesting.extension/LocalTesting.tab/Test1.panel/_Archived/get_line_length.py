from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
from pyrevit import revit
import clr
clr.AddReference("System")
from System.Collections.Generic import List 

#knowns for testing, use current active sheet
SHEETNAME = "1450-003 ELEVATION OF COUPLER ARRANGEMENT AT DWALL"
FAMILYNAME = ["ACM_DET_Rebar Layer", "ACM_DET_Layer Properties"]
VIEWNAMETOPLACE = "1000_DWALL COUPLER ELE TABLE_1600 - PART 5"

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application

selection = uidoc.Selection

ref_selection = selection.PickObject(ObjectType.Element)
picked_element = doc.GetElement(ref_selection)
end_point_1 = picked_element.GeometryCurve.GetEndPoint(1).Y
end_point_0 = picked_element.GeometryCurve.GetEndPoint(0).Y
diff = end_point_0 - end_point_1
convert_diff = UnitUtils.ConvertFromInternalUnits(diff, UnitTypeId.Millimeters)
line_length_in_mm = convert_diff
print(line_length_in_mm)
