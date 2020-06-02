oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.GetActiveEditor()

p = oDesign.GetProperties("DefinitionParameterTab", "Instance:{}".format(oDesign.GetName()))
for i in p:
    v = oEditor.GetPropertyValue("DefinitionParameterTab", "Instance:{}".format(oDesign.GetName()), i)
    AddWarningMessage("{}:{}".format(i, v))
