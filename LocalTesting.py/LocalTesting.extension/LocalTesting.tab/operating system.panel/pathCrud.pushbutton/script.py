# -*- coding: utf-8 -*-
__title__ = "OS" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
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
    try:
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
        rev_name_1 = get_param_value(sheet, REV_1_NAME_PARAM)
        rev_date_1 = get_param_value(sheet, REV_1_DATE_PARAM)
        rev_desc_1 = get_param_value(sheet, REV_1_DESC_PARAM)
        rev_dwg_1 = get_param_value(sheet, REV_1_DWG_PARAM)
        rev_chk_1 = get_param_value(sheet, REV_1_CHK_PARAM)
        rev_app_1 = get_param_value(sheet, REV_1_APP_PARAM)
        
        rev_name_2 = get_param_value(sheet, REV_2_NAME_PARAM)
        rev_date_2 = get_param_value(sheet, REV_2_DATE_PARAM)
        rev_desc_2 = get_param_value(sheet, REV_2_DESC_PARAM)
        rev_dwg_2 = get_param_value(sheet, REV_2_DWG_PARAM)
        rev_chk_2 = get_param_value(sheet, REV_2_CHK_PARAM)
        rev_app_2 = get_param_value(sheet, REV_2_APP_PARAM)

        rev_name_3 = get_param_value(sheet, REV_3_NAME_PARAM)
        rev_date_3 = get_param_value(sheet, REV_3_DATE_PARAM)
        rev_desc_3 = get_param_value(sheet, REV_3_DESC_PARAM)
        rev_dwg_3 = get_param_value(sheet, REV_3_DWG_PARAM)
        rev_chk_3 = get_param_value(sheet, REV_3_CHK_PARAM)
        rev_app_3 = get_param_value(sheet, REV_3_APP_PARAM)
        
        rev_name_4 = get_param_value(sheet, REV_4_NAME_PARAM)
        rev_date_4 = get_param_value(sheet, REV_4_DATE_PARAM)
        rev_desc_4 = get_param_value(sheet, REV_4_DESC_PARAM)
        rev_dwg_4 = get_param_value(sheet, REV_4_DWG_PARAM)
        rev_chk_4 = get_param_value(sheet, REV_4_CHK_PARAM)
        rev_app_4 = get_param_value(sheet, REV_4_APP_PARAM)

        rev_name_5 = get_param_value(sheet, REV_5_NAME_PARAM)
        rev_date_5 = get_param_value(sheet, REV_5_DATE_PARAM)
        rev_desc_5 = get_param_value(sheet, REV_5_DESC_PARAM)
        rev_dwg_5 = get_param_value(sheet, REV_5_DWG_PARAM)
        rev_chk_5 = get_param_value(sheet, REV_5_CHK_PARAM)
        rev_app_5 = get_param_value(sheet, REV_5_APP_PARAM)

        rev_name_6 = get_param_value(sheet, REV_6_NAME_PARAM)
        rev_date_6 = get_param_value(sheet, REV_6_DATE_PARAM)
        rev_desc_6 = get_param_value(sheet, REV_6_DESC_PARAM)
        rev_dwg_6 = get_param_value(sheet, REV_6_DWG_PARAM)
        rev_chk_6 = get_param_value(sheet, REV_6_CHK_PARAM)
        rev_app_6 = get_param_value(sheet, REV_6_APP_PARAM)

        rev_name_7 = get_param_value(sheet, REV_7_NAME_PARAM)
        rev_date_7 = get_param_value(sheet, REV_7_DATE_PARAM)
        rev_desc_7 = get_param_value(sheet, REV_7_DESC_PARAM)
        rev_dwg_7 = get_param_value(sheet, REV_7_DWG_PARAM)
        rev_chk_7 = get_param_value(sheet, REV_7_CHK_PARAM)
        rev_app_7 = get_param_value(sheet, REV_7_APP_PARAM)

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

        sheet_group[drawing_type][key] = [dwg_string,
                                        dwg_number,
                                        drawing_location, 
                                        sheet_name, 
                                        drawing_title_2,  
                                        sheet_status,
                                        dwg_number,
                                        current_revision, 
                                        sheet_number,
                                        a3_scale,
                                        a1_scale,
                                        PROJECT_UNITS,
                                        sheet_issue_date,
                                        designed_by,
                                        checked_by,
                                        approved_by,
                                        current_revision,
                                        rev_name_1,
                                        rev_date_1,
                                        rev_desc_1,
                                        rev_dwg_1,
                                        rev_chk_1,
                                        rev_app_1,
                                        rev_name_2,
                                        rev_date_2,
                                        rev_desc_2,
                                        rev_dwg_2,
                                        rev_chk_2,
                                        rev_app_2,
                                        rev_name_3,
                                        rev_date_3,
                                        rev_desc_3,
                                        rev_dwg_3,
                                        rev_chk_3,
                                        rev_app_3,
                                        rev_name_4,
                                        rev_date_4,
                                        rev_desc_4,
                                        rev_dwg_4,
                                        rev_chk_4,
                                        rev_app_4,
                                        rev_name_5,
                                        rev_date_5,
                                        rev_desc_5,
                                        rev_dwg_5,
                                        rev_chk_5,
                                        rev_app_5,
                                        rev_name_6,
                                        rev_date_6,
                                        rev_desc_6,
                                        rev_dwg_6,
                                        rev_chk_6,
                                        rev_app_6,
                                        rev_name_7,
                                        rev_date_7,
                                        rev_desc_7,
                                        rev_dwg_7,
                                        rev_chk_7,
                                        rev_app_7
                                        ]
    except:
        print("Error at {} - {}".format(sheet.Name, sheet.SheetNumber))
# generate index values
for drawing_type, sheets in sorted(sheet_group.items()):
    indx = 1
    for key, values in sorted(sheets.items()):
        sheet_group[drawing_type][key].insert(0, indx)
        print(key)
        print(values)
        indx = indx + 1

    
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
    # print(drawing_type)
    data.append([drawing_type]) 
    for key, values in sorted(sheets.items()):
        print(key)
        print(list(values))
        data.append(list(values))
    data.append([])
    print("\n \n")
    
# double check to remove empty list at the end of data set
if data[-1] == []:
    data.pop()

# print("\n \n")
# for d in data:
#     print(d)
# print("\n\n")

# ╦╔╗╔╔╦╗╔═╗╦═╗╔═╗╔═╗  ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║ ║ ║╣ ╠╦╝║ ║╠═╝  ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╝╚╝ ╩ ╚═╝╩╚═╚═╝╩    ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝

import clr
import os
import System
import time
from System import Array
from System.Collections.Generic import *

t= System.Type.GetTypeFromProgID("Excel.Application")
excel = System.Activator.CreateInstance(t)

excelTypeLibGuid = System.Guid("00020813-0000-0000-C000-000000000046")
clr.AddReferenceToTypeLibrary(excelTypeLibGuid)
from Excel import Application
from Excel import *
excel = Application()

clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c' )
from Microsoft.Office.Interop import Excel
from Microsoft.Office.Interop.Excel import ApplicationClass
from System.Runtime.InteropServices import Marshal

xlDirecDown = System.Enum.Parse(Excel.XlDirection, "xlDown")
xlDirecRight = System.Enum.Parse(Excel.XlDirection, "xlToRight")


# ╦ ╦╦═╗╦╔╦╗╔═╗  ╔╦╗╔═╗  ╔═╗═╗ ╦╔═╗╔═╗╦  
# ║║║╠╦╝║ ║ ║╣    ║ ║ ║  ║╣ ╔╩╦╝║  ║╣ ║  
# ╚╩╝╩╚═╩ ╩ ╚═╝   ╩ ╚═╝  ╚═╝╩ ╚═╚═╝╚═╝╩═╝

excel_file_path = forms.pick_excel_file(False, "Excel file")

if excel_file_path:
    try:
        workbook = excel.Workbooks.Open(excel_file_path)
        worksheets = workbook.Worksheets
        exists = False
        
        sheets = {}
        for s in worksheets:
            sheets[s.Name] = s

        singular_sheet = forms.SelectFromList.show(sorted(sheets.keys()), 
                                                title="Select a sheet", 
                                                button_name = "Select",
                                                width=450,
                                                height=450)
        
        if singular_sheet:
            worksheet = workbook.Sheets[singular_sheet]

        # write header values
        # for col_idx, header in enumerate(headers, start=1):
        #     worksheet.Cells[1, col_idx].Value2 = header
        
        # write row values
        for row_idx, data_row in enumerate(data, start=3):
            for col_idx, value in enumerate(data_row, start=1):
                worksheet.Cells[row_idx, col_idx].Value2 = value

        # format 
        # header_range = worksheet.Range["A1:C1"]
        # header_range.Font.FontStyle = "Bold"
        print("Succesfully written data")
    except:
        pass
    finally:
        workbook.Close(SaveChanges=True)
        excel.Quit()