import mysql.connector
from Database.databaseConnection import createConnection, closeConnection
from marksOperations import viewMarks
from utilities import calculatePercentage

def generateReportCard(studentID):
    connection = createConnection()
    
    if connection:
        cursor = connection.cursor()
        
        # Retrieve the marks for the student
        cursor.execute("SELECT Subject, Marks FROM Marks WHERE StudentID = %s", (studentID,))
        marks = cursor.fetchall()
        
        if not marks:
            print(f"No marks found for student {studentID}.")
            closeConnection(connection)
            return
        
        # Calculate the total marks
        total_marks = sum(mark[1] for mark in marks)
        
        # Assuming the maximum marks for each subject is 100 and the student has 5 subjects
        max_marks = len(marks) * 100  # Adjust this value if there are more/less subjects
        percentage = calculatePercentage(total_marks, max_marks)
        
        # Insert or update the report card
        cursor.execute("""
            INSERT INTO ReportCard (StudentID, TotalMarks, Percentage)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE TotalMarks = %s, Percentage = %s
        """, (studentID, total_marks, percentage, total_marks, percentage))
        
        connection.commit()
        print(f"Report card generated for student {studentID} with Total Marks: {total_marks} and Percentage: {percentage}%")
        closeConnection(connection)

def viewReportCard(studentID):
    connection = createConnection()
    if connection:
        cursor = connection.cursor()
        
        # SQL query to retrieve the report card for a specific student
        query = "SELECT TotalMarks, Percentage FROM ReportCard WHERE StudentID = %s"
        cursor.execute(query, (studentID,))
        report_card = cursor.fetchone()
        
        if report_card:
            print("\nReport Card for Student ID:", studentID)
            print(f"Total Marks: {report_card[0]}")
            print(f"Percentage: {report_card[1]}%")
        else:
            print(f"Report card not found for student {studentID}.")
        
        closeConnection(connection)

def viewAllReportCards():
    connection = createConnection()
    all_report_cards = []
    
    if connection:
        cursor = connection.cursor()
        
        # SQL query to retrieve all report cards, student names, and subject names with marks
        query = """
        SELECT Students.Name, Marks.Subject, Marks.Marks, ReportCard.StudentID, ReportCard.TotalMarks, ReportCard.Percentage
        FROM ReportCard
        JOIN Students ON ReportCard.StudentID = Students.StudentID
        JOIN Marks ON ReportCard.StudentID = Marks.StudentID
        """
        
        cursor.execute(query)
        report_cards = cursor.fetchall()
        
        # Debugging: Print the fetched report cards
        print("Fetched Report Cards:", report_cards)
        
        if report_cards:
            print("\nAll Report Cards:")
            for name, subject, marks, studentID, totalMarks, percentage in report_cards:
                print(f"Student Name: {name}, Subject: {subject}, Marks: {marks}, Student ID: {studentID}, Total Marks: {totalMarks}, Percentage: {percentage}%")
                # Adding to the list to return for CSV export
                all_report_cards.append((name, subject, marks, studentID, totalMarks, percentage))
        else:
            print("No report cards found.")
        
        closeConnection(connection)
    
    # Debugging: Print the final list of report cards to be returned
    # print("All Report Cards to export:", all_report_cards)
    return all_report_cards

