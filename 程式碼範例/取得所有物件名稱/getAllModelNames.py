# for HFSS, Q3D, Maxwell, Mechanical which use "3D Modeler" as Editor

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")

totalobjects = oEditor.GetNumObjects()
for i in range(totalobjects):
    objectname = oEditor.GetObjectName(i)
    AddWarningMessage(objectname)
