import sys
import clr
clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import DialogResult, SaveFileDialog
dialog = SaveFileDialog()
dialog.Filter = "text files (*.txt)|*.txt"

if dialog.ShowDialog() == DialogResult.OK:
    txt_path = dialog.FileName
    AddWarningMessage(txt_path)
else:
    sys.exit()
