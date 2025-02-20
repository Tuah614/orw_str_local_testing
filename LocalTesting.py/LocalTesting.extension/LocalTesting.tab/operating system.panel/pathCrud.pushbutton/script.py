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
MODEL_WBS_CODE = "1-"
# FROM PROJECT INFORMATION CAT
DISCIPLINE_CODE_PARAM = "ACM - Discipline Code" 
LOCATION_CODE_PARAM = "ACM - Location Code"
# FROM SHEETS CAT
STATUS_PARAM = "ACM - Project Status Abb."
TRADE_DISCIPLINE_PARAM = "ACM - Trade Discipline / Service Type"
DRAWING_TYPE_PARAM = "ACM - Type Drawing"
LOGO = "C:\Users\HamidT\OneDrive - AECOM\02. AECOM Brand Template\AECOM logo + taglines_EN\AECOM logo + taglines_EN\RGB ΓÇö Digital\Logo"

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝
def get_sheet_trade(sheet, param_name): # type: (Element, str) -> str
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

all_trades = set()
for sheet in sheet_collector:
    discipline = get_sheet_trade(sheet, TRADE_DISCIPLINE_PARAM)
    all_trades.add(discipline)
# for trade in all_trades:
#     print(trade)
trade_res = forms.SelectFromList.show(all_trades, 
                                "Filter by drawing trades", 
                                width=300, 
                                height=300, 
                                button_name= 'Select')

# filter sheets based on trade selection value
sheets_by_trade = [] # type: list
for sheet in sheet_collector:
    discipline = get_sheet_trade(sheet, TRADE_DISCIPLINE_PARAM)
    if discipline == trade_res:
        sheets_by_trade.append(sheet)

# get Sheet Number, Current Revision from Sheets
sheet_numbers = []
current_revisions = []
sheet_counts = len(sheets_by_trade)
for sheet in sheets_by_trade:
    sheet_numbers.append(sheet.LookupParameter())





# drawing number is a label with suffix and prefix of parameter values
# sample as follows
# 1-SE-0R07-1461-001-A
# {WBS CODE}-{WBS SYSTEM CODE}-{ACM - Discipline Code}-{ACM - Location Code}-{Sheet Number}-{SHEETNUMBER}-{Current Revision}
# SHEETNUMBER IS ALWAYS 001, based on BEP



# prompt user to select Excel file to dump data
# excel_path = forms.pick_excel_file()

