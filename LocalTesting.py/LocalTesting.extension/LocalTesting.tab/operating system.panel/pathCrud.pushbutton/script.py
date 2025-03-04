# -*- coding: utf-8 -*-
__title__ = "OS" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
import os
from pyrevit import forms
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import Selection, UIDocument
from Autodesk.Revit.ApplicationServices import *

# ╦═╗╔═╗╦  ╦╦╔╦╗  ╦  ╦╔═╗╦═╗
# ╠╦╝║╣ ╚╗╔╝║ ║   ╚╗╔╝╠═╣╠╦╝
# ╩╚═╚═╝ ╚╝ ╩ ╩    ╚╝ ╩ ╩╩╚═

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument # type: UIDocument
app = __revit__.Application #type: Application
selection = uidoc.Selection #type: Selection

# ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
# ║  ║ ║║║║╚═╗ ║ ╠═╣║║║ ║ ╚═╗
# ╚═╝╚═╝╝╚╝╚═╝ ╩ ╩ ╩╝╚╝ ╩ ╚═╝

# HARDCODED 
MODEL_WBS_CODE = "1-"
PROJECT_UNITS = "mm."

# PARAM NAMES TO FILTER SHEETS IN MAIN
TRADE_DISCIPLINE_PARAM = "ACM - Trade Discipline / Service Type" # sample value: SE - Strucutral

# FROM PROJECT INFORMATION CAT
DISCIPLINE_CODE_PARAM = "ACM - Discipline Code" # sample value: SE
LOCATION_CODE_PARAM = "ACM - Location Code" # sample value: OR06, OR07

# SHEET REVISIONS INFORMATIONS
REV_1_NAME_PARAM = "ACM - Rev.1 Name"
REV_2_NAME_PARAM = "ACM - Rev.2 Name"
REV_3_NAME_PARAM = "ACM - Rev.3 Name"
REV_4_NAME_PARAM = "ACM - Rev.4 Name"
REV_5_NAME_PARAM = "ACM - Rev.5 Name"
REV_6_NAME_PARAM = "ACM - Rev.6 Name"
REV_7_NAME_PARAM = "ACM - Rev.7 Name"

REV_1_DATE_PARAM = "ACM - Rev.1 Date"
REV_2_DATE_PARAM = "ACM - Rev.2 Date"
REV_3_DATE_PARAM = "ACM - Rev.3 Date"
REV_4_DATE_PARAM = "ACM - Rev.4 Date"
REV_5_DATE_PARAM = "ACM - Rev.5 Date"
REV_6_DATE_PARAM = "ACM - Rev.6 Date"
REV_7_DATE_PARAM = "ACM - Rev.7 Date"

REV_1_DESC_PARAM = "ACM - Rev.1 Description"
REV_2_DESC_PARAM = "ACM - Rev.2 Description"
REV_3_DESC_PARAM = "ACM - Rev.3 Description"
REV_4_DESC_PARAM = "ACM - Rev.4 Description"
REV_5_DESC_PARAM = "ACM - Rev.5 Description"
REV_6_DESC_PARAM = "ACM - Rev.6 Description"
REV_7_DESC_PARAM = "ACM - Rev.7 Description"

REV_1_DWG_PARAM = "ACM - Rev.1 DWG"
REV_2_DWG_PARAM = "ACM - Rev.2 DWG"
REV_3_DWG_PARAM = "ACM - Rev.3 DWG"
REV_4_DWG_PARAM = "ACM - Rev.4 DWG"
REV_5_DWG_PARAM = "ACM - Rev.5 DWG"
REV_6_DWG_PARAM = "ACM - Rev.6 DWG"
REV_7_DWG_PARAM = "ACM - Rev.7 DWG"

REV_1_CHK_PARAM = "ACM - Rev.1 CHK"
REV_2_CHK_PARAM = "ACM - Rev.2 CHK"
REV_3_CHK_PARAM = "ACM - Rev.3 CHK"
REV_4_CHK_PARAM = "ACM - Rev.4 CHK"
REV_5_CHK_PARAM = "ACM - Rev.5 CHK"
REV_6_CHK_PARAM = "ACM - Rev.6 CHK"
REV_7_CHK_PARAM = "ACM - Rev.7 CHK"

REV_1_APP_PARAM = "ACM - Rev.1 APP"
REV_2_APP_PARAM = "ACM - Rev.2 APP"
REV_3_APP_PARAM = "ACM - Rev.3 APP"
REV_4_APP_PARAM = "ACM - Rev.4 APP"
REV_5_APP_PARAM = "ACM - Rev.5 APP"
REV_6_APP_PARAM = "ACM - Rev.6 APP"
REV_7_APP_PARAM = "ACM - Rev.7 APP"


# FROM SHEETS CAT, IN ORDER FOR HEADERS
STATUS_PARAM = "ACM - Project Status Abb." # sample value: D, P
DRAWING_TYPE_PARAM = "ACM - Type Drawing" # sample value: 1000_DWALL
DRAWING_LOCATION_PARAM = "ACM - Drawing Location" # sample value: OR06: LAN LUANG STATION
A1_SCALE_PARAM = "ACM - Scale A1"
A3_SCALE_PARAM = "ACM - Scale A3"
DRAWING_TITLE_2 = "ACM - Drawing Title Line 2" # sample value: (SHEET 5/5)
LOGO = "C:\Users\HamidT\OneDrive - AECOM\02. AECOM Brand Template\AECOM logo + taglines_EN\AECOM logo + taglines_EN\RGB ΓÇö Digital\Logo"

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝

def get_param_value(sheet, param_name): # type: (Element, str) -> str
    discipline = sheet.LookupParameter(param_name).AsString()
    return discipline

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝

# get project constants from project information
project_info_collector = FilteredElementCollector(doc).\
                        OfClass(ProjectInfo).\
                        WhereElementIsNotElementType().\
                        ToElements()

project_info_element = project_info_collector[0] #type: Element
PROJECT_LOCATION_CODE = project_info_element.LookupParameter(LOCATION_CODE_PARAM).AsString()
PROJECT_DISCIPLINE_CODE = project_info_element.LookupParameter(DISCIPLINE_CODE_PARAM).AsString()

# get all sheets in current document
sheet_collector = FilteredElementCollector(doc).\
                OfClass(ViewSheet).\
                WhereElementIsNotElementType().\
                ToElements()

# filter by drawing types
all_drawing_types = set()
for sheet in sheet_collector:
    drawing_type = get_param_value(sheet, DRAWING_TYPE_PARAM)
    if drawing_type:
        try:
            all_drawing_types.add(drawing_type)
        except:
            pass

# prompt user to select drawing types
type_res = forms.SelectFromList.show(sorted(all_drawing_types), 
                                "Filter by drawing trades", 
                                width=450, 
                                height=450,
                                multiselect=True, 
                                button_name= 'Select')


# filter sheets based on drawing type selection value
sheets_by_type = [] # type: list
for sheet in sheet_collector:
    drawing_type = get_param_value(sheet, DRAWING_TYPE_PARAM)
    if drawing_type in type_res:
        sheets_by_type.append(sheet)

# generate drawing series header information
series_type_count = len(type_res)

# display sheets list by sheet number format
sheets_by_number = {}
for sheet in sheets_by_type:
    sheet_number = sheet.SheetNumber
    sheet_name = sheet.Name
    combined_key = "{}-{}".format(sheet_number, sheet_name)
    sheets_by_number[combined_key] = sheet

# prompt user to select sheets
sheet_res = forms.SelectFromList.show(sorted(sheets_by_number.keys()), 
                                "Select sheets to export", 
                                width=450, 
                                height=700,
                                multiselect=True, 
                                button_name= 'Select')

# filter by selected sheets
selected_sheets = {}
for key in sheet_res:
    if key in sheets_by_number:
        selected_sheets[key] = sheets_by_number[key]

# group sheets by drawing series
# for example, dict[1000_DWALL] = [sheet_objects]
sheet_group = {}
for key, sheet in (selected_sheets.items()):
    # get core informations
    drawing_type = get_param_value(sheet, DRAWING_TYPE_PARAM)
    drawing_location = get_param_value(sheet, DRAWING_LOCATION_PARAM)
    sheet_name = sheet.Name
    drawing_title_2 = get_param_value(sheet, DRAWING_TITLE_2)
    sheet_status = get_param_value(sheet, STATUS_PARAM)
    current_revision = doc.GetElement(sheet.GetCurrentRevision()).RevisionNumber
    sheet_number = sheet.SheetNumber
    a1_scale = get_param_value(sheet, A1_SCALE_PARAM)
    a3_scale = get_param_value(sheet, A3_SCALE_PARAM)
    sheet_issue_date = sheet.get_Parameter(BuiltInParameter.SHEET_ISSUE_DATE).AsString()
    designed_by = sheet.get_Parameter(BuiltInParameter.SHEET_DESIGNED_BY).AsString()
    checked_by = sheet.get_Parameter(BuiltInParameter.SHEET_CHECKED_BY).AsString()
    approved_by = sheet.get_Parameter(BuiltInParameter.SHEET_APPROVED_BY).AsString()

    # get past revisions
    
    
    # generate dwg name string
    dwg_string = "{}-1-{}-{}-{}-001-{}".format(sheet_status, 
                                               PROJECT_DISCIPLINE_CODE, 
                                               PROJECT_LOCATION_CODE, 
                                               sheet_number, 
                                               current_revision)

    # generate drawing no
    dwg_number = "1-{}-{}-{}-001".format(PROJECT_DISCIPLINE_CODE, 
                                        PROJECT_LOCATION_CODE, 
                                        sheet_number)

    if drawing_type not in sheet_group:
        sheet_group[drawing_type] = {}
        index = 1 # reset for every new series

    sheet_group[drawing_type][key] = (index,
                                      dwg_string,
                                      dwg_number,
                                      drawing_location, 
                                      sheet_name, 
                                      drawing_title_2,  
                                      sheet_status, 
                                      sheet_number,
                                      a1_scale,
                                      a3_scale,
                                      sheet_issue_date,
                                      designed_by,
                                      checked_by,
                                      current_revision,
                                      approved_by)
    
    index += 1 
    

# statement for checking
# for key, val in sorted(sheet_group.items()):
#     print("{} - {}".format(key, val))

#hardcoded headers for now
headers = [
    "Drawing Location", "Sheet Name", "Drawing Title 2", "Status", "Sheet Number",
    "A1 Scale", "A3 Scale", "Issue Date", "Designed By", "Checked By", "Current Revision", "Approved By"
]

# prepare data in the form of list to write in excel
data = []
for drawing_type, sheets in sorted(sheet_group.items()):
    print(drawing_type)
    data.append([drawing_type]) 
    for key, values in sheets.items():
        print(key)
        print(list(values))
        data.append(list(values))
    data.append([])
    
# double check to remove empty list at the end of data set
if data[-1] == []:
    data.pop()

print("\n \n")
for d in data:
    print(d)
print("\n\n")
# ╦ ╦╦═╗╦╔╦╗╔═╗  ╔╦╗╔═╗  ╔═╗═╗ ╦╔═╗╔═╗╦  
# ║║║╠╦╝║ ║ ║╣    ║ ║ ║  ║╣ ╔╩╦╝║  ║╣ ║  
# ╚╩╝╩╚═╩ ╩ ╚═╝   ╩ ╚═╝  ╚═╝╩ ╚═╚═╝╚═╝╩═╝

# import System
# import time
# from System import Array
# from System.Collections.Generic import *

# t= System.Type.GetTypeFromProgID("Excel.Application")
# excel = System.Activator.CreateInstance(t)

# excelTypeLibGuid = System.Guid("00020813-0000-0000-C000-000000000046")
# clr.AddReferenceToTypeLibrary(excelTypeLibGuid)
# from Excel import Application
# from Excel import *
# excel = Application()

# clr.AddReferenceByName('Microsoft.Office.Interop.Excel,Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c' )
# from Microsoft.Office.Interop import Excel
# from Microsoft.Office.Interop.Excel import ApplicationClass
# from System.Runtime.InteropServices import Marshal

# xlDirecDown = System.Enum.Parse(Excel.XlDirection, "xlDown")
# xlDirecRight = System.Enum.Parse(Excel.XlDirection, "xlToRight")

# prompt file path
# excel_file_path = forms.pick_excel_file(False, "Excel file")
# if excel_file_path:
#     try:
#         wb = excel.Workbooks.Open(excel_file_path)
#         worksheets = wb.Worksheets
#         exists = False

#         sheets = {}
#         for s in worksheets:
#             sheets[s.Name] = s

#         singular_sheet_res = forms.SelectFromList.show(sorted(sheets.keys()), 
#                                                        title="Select a sheet", 
#                                                        button_name="Select",
#                                                        width= 450,
#                                                        height=450)
        
#         if singular_sheet_res:
#             ws = wb.Sheets[singular_sheet_res]

#     except:
#         print("Something went wrong")
#         pass
#     finally:
#         workbook.Close()
#         excel.Quit()
