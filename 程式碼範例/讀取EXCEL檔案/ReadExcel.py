import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel

ex = Excel.ApplicationClass()   
ex.Visible = True
ex.DisplayAlerts = False   

workbook = ex.Workbooks.Open('d:/demo/foo.xls')
ws = workbook.Worksheets[1]
data=ws.Rows[1].Value2[0,0]
AddWarningMessage(str(data))
