import mysql.connector
from Database.databaseConnection import createConnection, closeConnection

def addStudent(studentID, name, student_class, section):
    connection = createConnection()
    if connection:
        cursor = connection.cursor()
        
        # SQL query to insert a new student into the Students table
        query = "INSERT INTO Students (StudentID, Name, Class, Section) VALUES (%s, %s, %s, %s)"
        values = (studentID, name, student_class, section)
        
        cursor.execute(query, values)
        connection.commit()
        
        print(f"Student {name} added successfully.")
        closeConnection(connection)

def updateStudent(studentID, name, student_class, section):
    connection = createConnection()
    if connection:
        cursor = connection.cursor()
        
        # SQL query to update student information in the Students table
        query = "UPDATE Students SET Name = %s, Class = %s, Section = %s WHERE StudentID = %s"
        values = (name, student_class, section, studentID)
        
        cursor.execute(query, values)
        connection.commit()
        
        if cursor.rowcount > 0:
            print(f"Student {studentID} updated successfully.")
        else:
            print(f"Student {studentID} not found.")
        
        closeConnection(connection)

def viewStudent(studentID):
    connection = createConnection()
    if connection:
        cursor = connection.cursor()
        
        # SQL query to retrieve details of a specific student from the Students table
        query = "SELECT * FROM Students WHERE StudentID = %s"
        cursor.execute(query, (studentID,))
        student = cursor.fetchone()
        
        if student:
            print("\nStudent Details:")
            print(f"Student ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Class: {student[2]}")
            print(f"Section: {student[3]}")
        else:
            print(f"Student with ID {studentID} not found.")
        
        closeConnection(connection)

def viewAllStudents():
    connection = createConnection()
    if connection:
        cursor = connection.cursor()
        
        # SQL query to retrieve all students from the Students table
        query = "SELECT * FROM Students"
        cursor.execute(query)
        students = cursor.fetchall()
        
        if students:
            print("\nAll Students:")
            for student in students:
                print(f"Student ID: {student[0]}, Name: {student[1]}, Class: {student[2]}, Section: {student[3]}")
        else:
            print("No students found.")
        
        closeConnection(connection)

def deleteStudent(studentID):
    connection = createConnection()
    
    if connection:
        cursor = connection.cursor()
        
        try:
            # Delete student's report card
            cursor.execute("DELETE FROM ReportCard WHERE StudentID = %s", (studentID,))
            print(f"Report card for student {studentID} deleted.")
            
            # Delete student's marks
            cursor.execute("DELETE FROM Marks WHERE StudentID = %s", (studentID,))
            print(f"Marks for student {studentID} deleted.")
            
            # Delete student's details
            cursor.execute("DELETE FROM Students WHERE StudentID = %s", (studentID,))
            print(f"Student record for student {studentID} deleted.")
            
            connection.commit()
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
        finally:
            closeConnection(connection)