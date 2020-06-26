import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oDesktop.ClearMessages("","",2)

oModule = oDesign.GetModule("ReportSetup")
arr = oModule.GetSolutionDataPerVariation(  
"Modal Solution Data", 
"Setup1 : Sweep", 
['Domain:=', 'Sweep'],
['Freq:=', ['All']], 
["dB(S(1,1))"])

AddWarningMessage(str(arr[0].GetRealDataValues("dB(S(1,1))")))
