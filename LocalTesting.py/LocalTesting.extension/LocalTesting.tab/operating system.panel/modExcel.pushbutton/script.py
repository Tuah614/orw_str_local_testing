# -*- coding: utf-8 -*-
__title__ = "OS" 
__author__ = "Tuah Hamid  - AECOM KL" 
__helpurl__ = "https://teams.microsoft.com/l/chat/0/0?users=tuah.hamid@aecom.com"

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
import clr
import os
from pyrevit import forms
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import Selection, UIDocument
from Autodesk.Revit.ApplicationServices import *

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

# ╦═╗╔═╗╦  ╦╦╔╦╗  ╦  ╦╔═╗╦═╗
# ╠╦╝║╣ ╚╗╔╝║ ║   ╚╗╔╝╠═╣╠╦╝
# ╩╚═╚═╝ ╚╝ ╩ ╩    ╚╝ ╩ ╩╩╚═

doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument # type: UIDocument
app = __revit__.Application #type: Application
selection = uidoc.Selection #type: Selection

# ╔═╗═╗ ╦╔═╗╔═╗╦    ╦  ╦╔═╗╦═╗
# ║╣ ╔╩╦╝║  ║╣ ║    ╚╗╔╝╠═╣╠╦╝
# ╚═╝╩ ╚═╚═╝╚═╝╩═╝   ╚╝ ╩ ╩╩╚═

clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c' )
from Microsoft.Office.Interop import Excel
from Microsoft.Office.Interop.Excel import ApplicationClass
from System.Runtime.InteropServices import Marshal

xlDirecDown = System.Enum.Parse(Excel.XlDirection, "xlDown")
xlDirecRight = System.Enum.Parse(Excel.XlDirection, "xlToRight")

# ╔═╗╔═╗╔╦╗╔═╗╦  ╔═╗  ╔╦╗╔═╗╔╦╗╔═╗
# ╚═╗╠═╣║║║╠═╝║  ║╣    ║║╠═╣ ║ ╠═╣
# ╚═╝╩ ╩╩ ╩╩  ╩═╝╚═╝  ═╩╝╩ ╩ ╩ ╩ ╩

headers = [
    "Drawing Location", "Sheet Name", "Drawing Title 2", "Status", "Sheet Number",
    "A1 Scale", "A3 Scale", "Issue Date", "Designed By", "Checked By", "Current Revision", "Approved By"
]

data = [['2000_SKELETON'], 
        ['OR06: LAN LUANG STATION', 'MULTIPURPOSE LEVEL LAYOUT PLAN', 'TEMPORARY STAGE (SHEET 1/2)', 'P', '2020', '200', '400', '20-12-2024', 'LCY', 'CKC', 'A', 'LCC'], 
        [], 
        ['4000_DWALL ENTRANCES'], 
        ['OR06: LAN LUANG STATION', 'ENTRANCE 3 - CROSS SECTIONS', '', 'P', '4330', '100', '200', '20-12-2024', 'LCY', 'CKC', 'A', 'LCC'], 
        ['OR06: LAN LUANG STATION', 'ENTRANCE 4 - D-WALL & BARRETTE PILE LAYOUT PLAN', '', 'P', '4410', '200', '400', '20-12-2024', 'LCY', 'CKC', 'A', 'LCC']]
data2 = [['1000_DWALL'], 
         ['OR06: LAN LUANG STATION', 'DIAPHRAGM WALL NOTES AND TYPICAL DETAILS', '(SHEET 4/4)', 'D', '1014', 'AS SHOWN', 'AS SHOWN', '28-01-2025', 'LCY', 'CKC', 'A', 'LCC'], 
         ['OR06: LAN LUANG STATION', 'DIAPHRAGM WALL NOTES AND TYPICAL DETAILS', '(SHEET 2/4)', 'D', '1012', '25', '50', '28-01-2025', 'LCY', 'CKC', 'A', 'LCC'], 
         ['OR06: LAN LUANG STATION', 'DIAPHRAGM WALL NOTES AND TYPICAL DETAILS', '(SHEET 3/4)', 'D', '1013', '25', '50', '28-01-2025', 'LCY', 'CKC', 'A', 'LCC'], 
         ['OR06: LAN LUANG STATION', 'DIAPHRAGM WALL NOTES AND TYPICAL DETAILS', '(SHEET 1/4)', 'D', '1011', 'N.T.S', 'N.T.S', '28-01-2025', 'LCY', 'CKC', 'A', 'LCC'], 
         [], 
         ['5000_ENTRANCES SKELETON'], 
         ['OR06: LAN LUANG STATION', 'ENTRANCE 3 - LAYOUT PLAN', 'STATION ROOF LEVEL (TEMPORARY STAGE)', 'P', '5500', '100', '200', '20-12-2024', 'LCY', 'CKC', 'A', 'LCC'], 
         ['OR06: LAN LUANG STATION', 'ENTRANCE 3 - CROSS SECTIONS', 'TEMPORARY STAGE', 'P', '5510', '100', '200', '20-12-2024', 'LCY', 'CKC', 'A', 'LCC'], 
         ['OR06: LAN LUANG STATION', 'ENTRANCE 3 - LAYOUT PLAN', 'MULTIPURPOSE LEVEL (TEMPORARY STAGE)', 'P', '5501', '100', '200', '20-12-2024', 'LCY', 'CKC', 'A', 'LCC'], 
         ['OR06: LAN LUANG STATION', 'ENTRANCE 4 - LAYOUT PLAN', 'STATION ROOF LEVEL (TEMPORARY STAGE)', 'P', '5700', '100', '200', '20-12-2024', 'LCY', 'CKC', 'A', 'LCC']]

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
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

        #dummy values
        for col_idx, header in enumerate(headers, start=1):
            worksheet.Cells[1, col_idx].Value2 = header
        
        for row_idx, data_row in enumerate(data2, start=2):
            for col_idx, value in enumerate(data_row, start=1):
                worksheet.Cells[row_idx, col_idx].Value2 = value

        # format 
        header_range = worksheet.Range["A1:C1"]
        header_range.Font.FontStyle = "Bold"
        print("Succesfully written data")
    except:
        pass
    finally:
        workbook.Close()
        excel.Quit()

    


