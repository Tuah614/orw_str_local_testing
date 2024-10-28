from pathlib import Path

x = Path.joinpath("seasea")

from pyrevit import forms

message = forms.alert("Ttest", exitscript=True)
forms.Autodesk.Internal
from Autodesk.Revit.DB import FilteredE