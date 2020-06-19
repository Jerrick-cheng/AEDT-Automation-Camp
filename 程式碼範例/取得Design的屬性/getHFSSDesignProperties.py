# Get Design Properties (HFSS Only)

oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
p = oDesign.GetProperties('LocalVariableTab', "LocalVariables")
result = {}
for i in p:
    v = oDesign.GetPropertyValue("LocalVariableTab", 'LocalVariables', i)
    result[i] = v

AddWarningMessage(str(result))
