class mlops:
    def __init__(self,totalStudents):
        self.totalStudents = totalStudents

    def getTotalStudents(self):
        return self.totalStudents
    
    def addStudent(self):
        self.totalStudents = self.totalStudents + 1
        return self.totalStudents
    
    def removeStudent(self):
        self.totalStudents = self.totalStudents - 1
        return self.totalStudents
    
    def getClassName(self):
        return "Machine Learning Operations (CS-B)"
    
# mlops_object = mlops(5)
# print(mlops_object.getTotalStudents())
# print(mlops_object.addStudent())
# print(mlops_object.removeStudent())
# print(mlops_object.getClassName())
    