oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.GetActiveEditor()

p = oDesign.GetProperties("DefinitionParameterTab", "Instance:{}".format(oDesign.GetName()))
result = {}
for i in p:
    v = oEditor.GetPropertyValue("DefinitionParameterTab", "Instance:{}".format(oDesign.GetName()), i)
    result[i] = v

AddWarningMessage(str(result))
