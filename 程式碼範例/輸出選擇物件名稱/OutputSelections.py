oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")

s = oEditor.GetSelections()

AddWarningMessage(str(s))
