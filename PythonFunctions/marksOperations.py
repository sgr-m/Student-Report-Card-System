import mysql.connector
from Database.databaseConnection import createConnection, closeConnection

def addMarks(studentID, subject, marks):
    connection = createConnection()
    if connection:
        cursor = connection.cursor()
        
        # SQL query to insert marks for a specific student and subject
        query = "INSERT INTO Marks (StudentID, Subject, Marks) VALUES (%s, %s, %s)"
        values = (studentID, subject, marks)
        
        cursor.execute(query, values)
        connection.commit()
        
        print(f"Marks for {subject} added successfully for student {studentID}.")
        closeConnection(connection)

def updateMarks(studentID, subject, marks):
    connection = createConnection()
    if connection:
        cursor = connection.cursor()
        
        # SQL query to update marks for a specific student and subject
        query = "UPDATE Marks SET Marks = %s WHERE StudentID = %s AND Subject = %s"
        values = (marks, studentID, subject)
        
        cursor.execute(query, values)
        connection.commit()
        
        if cursor.rowcount > 0:
            print(f"Marks for {subject} updated successfully for student {studentID}.")
        else:
            print(f"Marks for {subject} not found for student {studentID}.")
        
        closeConnection(connection)

def viewMarks(studentID):
    connection = createConnection()
    if connection:
        cursor = connection.cursor()
        
        # SQL query to retrieve marks for a specific student
        query = "SELECT Subject, Marks FROM Marks WHERE StudentID = %s"
        cursor.execute(query, (studentID,))
        marks = cursor.fetchall()
        
        if marks:
            print("\nMarks for Student ID:", studentID)
            for subject, marks_obtained in marks:
                print(f"Subject: {subject}, Marks: {marks_obtained}")
        else:
            print(f"No marks found for student {studentID}.")
        
        closeConnection(connection)

def viewAllMarks():
    connection = createConnection()
    if connection:
        cursor = connection.cursor()
        
        # SQL query to retrieve all marks from the Marks table
        query = "SELECT StudentID, Subject, Marks FROM Marks"
        cursor.execute(query)
        all_marks = cursor.fetchall()
        
        if all_marks:
            print("\nAll Marks:")
            for studentID, subject, marks in all_marks:
                print(f"Student ID: {studentID}, Subject: {subject}, Marks: {marks}")
        else:
            print("No marks found in the system.")
        
        closeConnection(connection)
