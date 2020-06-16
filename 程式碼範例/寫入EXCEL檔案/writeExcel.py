#color index: https://docs.microsoft.com/zh-tw/office/vba/api/excel.colorindex

import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')

import Microsoft.Office.Interop.Excel as Excel
excel = Excel.ApplicationClass()
excel.Visible = True

workbook = excel.Workbooks.Add()
ws = workbook.Worksheets.Add()
ws.Range["A1"]= "Hello World"
ws.Range["A1"].Interior.ColorIndex = 4
usedrange = ws.UsedRange
usedrange.Columns.AutoFit()
