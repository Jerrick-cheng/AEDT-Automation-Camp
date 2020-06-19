# Set Design Properties (HFSS Only)
# if _myproperty exists, value is shown. if not, it will be added.
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
p = oDesign.GetProperties('LocalVariableTab', "LocalVariables")
result = {}

if '_myproperty' in p:
    v = oDesign.GetPropertyValue("LocalVariableTab", 'LocalVariables', '_myproperty')
    AddWarningMessage(str(v))

else:
    oDesign.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:LocalVariableTab",
                [
                    "NAME:PropServers", 
                    "LocalVariables"
                ],
                [
                    "NAME:NewProps",
                    [
                        "NAME:_myproperty",
                        "PropType:="		, "VariableProp",
                        "UserDef:="		, True,
                        "Value:="		, "1"
                    ]
                ]
            ]
        ])
    AddWarningMessage("_myproperty is added.")
    
