from Database.databaseConnection import createConnection, closeConnection
from config import DB_CONFIG

def createTables():
    connection = createConnection()
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(100),
            Class VARCHAR(10),
            Section VARCHAR(10)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Marks (
            StudentID INT,
            Subject VARCHAR(100),
            Marks INT,
            PRIMARY KEY (StudentID, Subject),
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ReportCard (
            StudentID INT,
            TotalMarks INT,
            Percentage DECIMAL(5,2),
            PRIMARY KEY (StudentID),
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
        )
    """)
    
    connection.commit()
    connection.close()

def initializeDatabase():
    createTables()
    print("Database and tables created successfully.")

#"__main__":
initializeDatabase()
