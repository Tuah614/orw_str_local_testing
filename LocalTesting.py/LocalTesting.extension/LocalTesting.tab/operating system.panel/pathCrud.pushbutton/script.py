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
DISCIPLINE_CODE_PARAM = "ACM - Discipline Code" # sample value: D, P
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
REV_4_ESC_PARAM = "ACM - Rev.4 Description"
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
for key, sheet in selected_sheets.items():
    drawing_type = get_param_value(sheet, DRAWING_TYPE_PARAM)
    drawing_location = get_param_value(sheet, DRAWING_LOCATION_PARAM)
    sheet_name = sheet.Name
    drawing_title_2 = get_param_value(sheet, DRAWING_TITLE_2)
    sheet_status = get_param_value(sheet, STATUS_PARAM)
    current_revision = doc.GetElement(sheet.GetCurrentRevision()).RevisionNumber
    sheet_number = sheet.SheetNumber
    a1_scale = get_param_value(sheet, A1_SCALE_PARAM)
    a3_scale = get_param_value(sheet, A3_SCALE_PARAM)

    if drawing_type not in sheet_group:
        sheet_group[drawing_type] = {}
    sheet_group[drawing_type][key] = (drawing_location, 
                                        sheet_name, 
                                        drawing_title_2,  
                                        sheet_status, 
                                        current_revision,
                                        sheet_number,
                                        a1_scale,
                                        a3_scale)

for key, val in sheet_group.items():
    print("{} - {}".format(key, val))

# get Sheet Number, Current Revision from Sheets
sheet_numbers = [] 
current_revisions = []

# # generate rows NO. data
# sheet_counts = len(sheets_by_type)
# row_counts = list(range(1, sheet_counts + 1)) + (series_type_count * 2) # reserve two rows for each header

# for sheet in sheets_by_type:
#     rev_element = doc.GetElement(sheet.GetCurrentRevision()) # type: Revision
#     current_revisions.append(rev_element)
#     try:
#         print(rev_element.RevisionNumber)
#     except:
#         print("NOT FOUND: {}  Type: {} Sheet: {}".format(Element.Name.__get__(rev_element), type(rev_element), sheet.Name))
        
    


# drawing number is a label with suffix and prefix of parameter values
# sample as follows
# 1-SE-0R07-1461-001-A
# {WBS CODE}-{WBS SYSTEM CODE}-{ACM - Discipline Code}-{ACM - Location Code}-{Sheet Number}-{SHEETNUMBER}-{Current Revision}
# SHEETNUMBER IS ALWAYS 001, based on BEP



# prompt user to select Excel file to dump data
# excel_path = forms.pick_excel_file()

