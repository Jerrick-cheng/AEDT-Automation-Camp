# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.1.0
# 20:37:40  Jun 11, 2020
# ----------------------------------------------
import clr, sys
sys.path.append('C:/Program Files/AnsysEM/AnsysEM19.5/Win64/common/IronPython/DLLs')
sys.path.append('C:/Program Files/AnsysEM/AnsysEM20.1/Win64/common/IronPython/DLLs')
clr.AddReference('IronPython.Wpf')

from System.Windows.Forms import FolderBrowserDialog, DialogResult

dialog = FolderBrowserDialog()
dialog.SelectedPath = 'c:\\'

if dialog.ShowDialog() == DialogResult.OK:
    selected_folder = dialog.SelectedPath
    AddWarningMessage(selected_folder)
    
else:
    pass

