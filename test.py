from main import mlops
 
mlops_object = mlops(5)
def test_getTotalStudents():
    assert mlops_object.getTotalStudents() == 5

def test_addStudent():
    assert mlops_object.addStudent() == 6

def test_removeStudent():
    assert mlops_object.removeStudent() == 5

def test_getClassName():
    assert mlops_object.getClassName() == "Machine Learning Operations (CS-B)"