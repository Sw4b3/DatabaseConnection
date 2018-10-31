import mysql.connector

class DatabaseController(object):
 
    def getConnection(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="StudentDB"
            )
        return connection

    def viewStudent(self):
        connection=self.getConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Students")
        result = cursor.fetchall()

        for x in result:
            print(x)

    def insertStudent(self):
       print("Enter First Name")
       name=input();
       print("Enter Last Name")
       surname=input();
       print("Enter Age Name")
       age=input();
       print("Enter Course Name")
       course=input();
       connection=self.getConnection()
       cursor = connection.cursor()
       sql = "INSERT INTO Students (studentName, studentSurname,studentAge, studentCourse) VALUES (%s, %s,%s,%s)"
       val = (name, surname,age,course)
       cursor.execute(sql, val)
       connection.commit()
       print(cursor.rowcount, "record inserted.")

    def updateStudent(self):
       print("Enter full name of student")
       fullname=input();
       oldname,oldsurname=fullname.split(" ")
       print("Enter First Name")
       name=input();
       print("Enter Last Name")
       surname=input();
       print("Enter Age Name")
       age=input();
       print("Enter Course Name")
       course=input();
       connection=self.getConnection()
       cursor = connection.cursor()
       sql = "UPDATE Students SET studentName=%s, studentSurname=%s,studentAge=%s, studentCourse=%s WHERE studentName=%s AND studentSurname= %s"
       val = (name, surname,age,course,oldname,oldsurname)
       cursor.execute(sql, val)
       connection.commit()
       print(cursor.rowcount, "record inserted.")

    def deleteStudent(self):
        print("Enter full name of student")
        fullname=input();
        name,surname=fullname.split(" ")
        connection=self.getConnection()
        cursor=connection.cursor();
        sql="DELETE FROM students WHERE studentName=%s AND studentSurname= %s"
        val = (name, surname)
        cursor.execute(sql,val)
        connection.commit()
        print("Record deleted.")


