from Autodesk.Revit.DB import BuiltInCategory
import clr
clr.AddReference("System")  # Make sure this is included before the import
from System import Enum

bic_values = Enum.GetValues(BuiltInCategory)

for bic in bic_values:
    print("{0} = {1}".format(bic.ToString(), int(bic)))  