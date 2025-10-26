-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS ReportCards;

-- Use the created database
USE ReportCards;

-- Create Students table
CREATE TABLE IF NOT EXISTS Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Class VARCHAR(10),
    Section VARCHAR(10)
);

-- Create Marks table
CREATE TABLE IF NOT EXISTS Marks (
    StudentID INT,
    Subject VARCHAR(100),
    Marks INT,
    PRIMARY KEY (StudentID, Subject),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Create ReportCard table
CREATE TABLE IF NOT EXISTS ReportCard (
    StudentID INT PRIMARY KEY,
    TotalMarks INT,
    Percentage DECIMAL(5, 2),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Insert students 
INSERT INTO Students (Name, Class, Section) VALUES
('Ravi Kumar', '12', 'A'),
('Priya Sharma', '12', 'B'),
('Aman Verma', '12', 'B'),
('Shivani Gupta', '12', 'A'),
('Vikas Singh', '12', 'C'),
('Anjali Yadav', '12', 'C'),
('Pooja Mehta', '12', 'A'),
('Nikhil Raj', '12', 'B'),
('Deepak Joshi', '12', 'C');

-- Insert marks 
INSERT INTO Marks (StudentID, Subject, Marks) VALUES
(1, 'Physics', 85),(1, 'Chemistry', 88),(1, 'Biology', 78),(1, 'Mathematics', 92),(1, 'English', 89),
(2, 'Physics', 75),(2, 'Chemistry', 82),(2, 'Biology', 70),(2, 'Mathematics', 80),(2, 'English', 85),
(3, 'Physics', 88),(3, 'Chemistry', 79),(3, 'Biology', 81),(3, 'Mathematics', 90),(3, 'English', 92),
(4, 'Physics', 80),(4, 'Chemistry', 85),(4, 'Biology', 77),(4, 'Mathematics', 86),(4, 'English', 88),
(5, 'Physics', 91),(5, 'Chemistry', 84),(5, 'Biology', 79),(5, 'Mathematics', 89),(5, 'English', 90),
(6, 'Physics', 79),(6, 'Chemistry', 88),(6, 'Biology', 82),(6, 'Mathematics', 84),(6, 'English', 86),
(7, 'Physics', 82),(7, 'Chemistry', 79),(7, 'Biology', 75),(7, 'Mathematics', 87),(7, 'English', 80),
(8, 'Physics', 84),(8, 'Chemistry', 86),(8, 'Biology', 80),(8, 'Mathematics', 90),(8, 'English', 83),
(9, 'Physics', 90),(9, 'Chemistry', 82),(9, 'Biology', 78),(9, 'Mathematics', 85),(9, 'English', 87),

-- Insert report card
INSERT INTO ReportCard (StudentID, TotalMarks, Percentage) VALUES
(1, 434, 86.80),
(2, 402, 80.40),
(3, 430, 86.00),
(4, 416, 83.20),
(5, 433, 86.60),
(6, 418, 83.60),
(7, 413, 82.60),
(8, 434, 86.80),
(9, 423, 84.60),


