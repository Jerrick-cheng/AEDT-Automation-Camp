# HFSS 3D Layout

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDefinitionManager = oProject.GetDefinitionManager()
oPadstackManager = oDefinitionManager.GetManager("Padstack")
padstack_names = oPadstackManager.GetNames()
AddWarningMessage(str(padstack_names))
