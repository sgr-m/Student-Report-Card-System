from PythonFunctions.studentOperations import addStudent, updateStudent, viewAllStudents, deleteStudent
from PythonFunctions.marksOperations import addMarks, updateMarks, viewAllMarks
from PythonFunctions.reportCardOperations import generateReportCard, viewReportCard, viewAllReportCards
from PythonFunctions.utilities import exportToCSV

def displayMainMenu():
    print("\n--- Student Report Card System ---")
    print("1. Add Student")
    print("2. Update Student")
    print("3. View All Students")
    print("4. Add Marks")
    print("5. Update Marks")
    print("6. View All Marks")
    print("7. Generate Report Card")
    print("8. View Report Card")
    print("9. Export All Report Cards to CSV")
    print("10. Delete Student Record")
    print("11. Exit")

def run():
    while True:
        displayMainMenu()
        try:
            choice = int(input("Please select an option (1-11): "))
            
            if choice == 1:  # Add Student
                studentID = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                class_ = input("Enter Class (e.g., 12): ")
                section = input("Enter Section (e.g., A): ")
                addStudent(studentID, name, class_, section)
            
            elif choice == 2:  # Update Student
                studentID = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                class_ = input("Enter Class (e.g., 12): ")
                section = input("Enter Section (e.g., A): ")
                updateStudent(studentID, name, class_, section)
            
            elif choice == 3:  # View All Students
                viewAllStudents()
            
            elif choice == 4:  # Add Marks
                studentID = int(input("Enter Student ID: "))
                subject = input("Enter Subject: ")
                marks = int(input("Enter Marks: "))
                addMarks(studentID, subject, marks)
            
            elif choice == 5:  # Update Marks
                studentID = int(input("Enter Student ID: "))
                subject = input("Enter Subject: ")
                marks = int(input("Enter Marks: "))
                updateMarks(studentID, subject, marks)
            
            elif choice == 6:  # View All Marks
                viewAllMarks()
            
            elif choice == 7:  # Generate Report Card
                studentID = int(input("Enter Student ID: "))
                generateReportCard(studentID)
            
            elif choice == 8:  # View Report Card
                studentID = int(input("Enter Student ID: "))
                viewReportCard(studentID)
            
            elif choice == 9:  # Export All Report Cards to CSV
                report_cards = viewAllReportCards()
                exportToCSV(report_cards)
            
            elif choice == 10:  # Delete Student Record
                studentID = int(input("Enter Student ID to delete: "))
                deleteStudent(studentID)
            
            elif choice == 11:  # Exit Program
                exitProgram()
            
            else:
                print("Invalid choice, please select between 1 and 11.")
        except ValueError:
            print("Invalid input, please enter a number between 1 and 11.")

def exitProgram():
    print("Exiting the program.")
    exit()

#"__main__":
run()
