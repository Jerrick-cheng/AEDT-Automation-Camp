import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oModule = oDesign.GetModule("BoundarySetup")

def getExcitationTerminal():
    result={}

    excitations = oModule.GetExcitationsOfType("Terminal")
    
    x = oModule.GetPortExcitationCounts()
    names = x[0::2]
    values = [int(i) for i in x[1::2]]
    index=0
    for n, v in zip(names, values):
        result[n] = excitations[index:index+v]
        index+=v
        
    return result    
        
AddWarningMessage(str(getExcitationTerminal()))
