import DatabaseController

RUNNING=True;
while RUNNING==True:
    print("Do you want to view Students?")
    x=input()
    if(x=="yes"):
        controller= DatabaseController.DatabaseController()
        controller.viewStudent()
    print("Do you want to insert Students?")
    x=input()
    if(x=="yes"):
        controller= DatabaseController.DatabaseController()
        controller.insertStudent()

    print("Do you want to update a Student?")
    x=input()
    if(x=="yes"):
        controller= DatabaseController.DatabaseController()
        controller.updateStudent()

    print("Do you want to delete a Student?")
    x=input()
    if(x=="yes"):
        controller= DatabaseController.DatabaseController()
        controller.deleteStudent()
   
    print("Do you want to exit?")
    x=input()
    if(x=="yes"):
        RUNNING=False

