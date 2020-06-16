# HFSS 3D Layout

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.GetActiveEditor()
layer_names = oEditor.GetStackupLayerNames()
AddWarningMessage(str(layer_names))
