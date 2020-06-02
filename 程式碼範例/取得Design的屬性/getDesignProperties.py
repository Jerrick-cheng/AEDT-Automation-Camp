oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()

p = oDesign.GetProperties("DefinitionParameterTab", "Instance:{}".format(oDesign.GetName()))
AddWarningMessage(str(p))
