oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")
import math
import time
def printf(x):
    AddWarningMessage(str(x))

class face():
    def __init__(self, id, object=None):
        self.object = object
        self.id = id
        self.method = { 'area':self.__getArea,
                        'center':self.__getCenter,
                        'normal_vector':self.__getNormalVector,
                        'edgecount':self.__getEdgeCount,}
                        
    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False
            
    def __ne__(self, other):
        return not self.__eq__(other)
            
    def __str__(self):
        return str(self.id)     
        
    def __repr__(self):
        return str(self.id)
    
    def __getattr__(self, x):
        try:
            return self.method[x]()
        except:
            raise Exception('{} does not exist!'.format(x))
        
    def __getArea(self):
        self.area = oEditor.GetFaceArea(self.id)
        return self.area
            
    def __getCenter(self):
        self.center = tuple(map(float, oEditor.GetFaceCenter(self.id)))
        return self.center
    
    def __getNormalVector(self):
        vids = oEditor.GetVertexIDsFromFace(self.id)
        locations = []
        for v in vids:
            locations.append([float(i) for i in oEditor.GetVertexPosition(v)])

        pt0, pt1, pt2 = locations[0:3]
        u = [j-i for i,j in zip(pt1, pt0)]
        v = [j-i for i,j in zip(pt2, pt1)]
        s1 = u[1]*v[2] - u[2]*v[1]
        s2 = u[2]*v[0] - u[0]*v[2]
        s3 = u[0]*v[1] - u[1]*v[0]
        x = math.sqrt(s1*s1 + s2*s2 + s3*s3)
        self.normal_vector = (s1/x, s2/x, s3/x)
        return self.normal_vector
   
    def __getEdgeCount(self):
        self.edgecount = len(oEditor.GetEdgeIDsFromFace(self.id))
        return self.edgecount

    def getAngle(self, other):
        x0, y0, z0 = self.normal_vector
        x1, y1, z1 = other.normal_vector
        
        return round(math.degrees(math.acos(x0*x1+y0*y1+z0*z1)),1)
    
    def getCenterGap(self, other):
        x0, y0, z0 = self.center
        x1, y1, z1 = other.center        
        
        return math.sqrt(pow(x0-x1, 2)+pow(y0-y1, 2)+pow(z0-z1, 2))

    def getCommonEdges(self, other):
        self_edges = oEditor.GetEdgeIDsFromFace(self.id)
        other_edges = oEditor.GetEdgeIDsFromFace(other.id)
        return list(set(self_edges).intersection(other_edges))
        
def getModelFaces(objectname):
    result = []
    for faceid in oEditor.GetFaceIDs(objectname):
        x = face(faceid, objectname)
        result.append(x)
    return result

if __name__ == '__main__':
    faces = getModelFaces('RegularPolyhedron1')

    for i in faces:
        printf(i.center)
        printf(i.edgecount)
        printf(i.area)
        printf(i.normal_vector)
