import csv

def validateInput(input):
    # Placeholder function for validating input
    pass

def formatData(data):
    # Placeholder function for formatting data
    pass

def calculatePercentage(totalMarks, maxMarks):
    # Calculate the percentage based on total and maximum marks
    return (totalMarks / maxMarks) * 100

def exportToCSV(report_cards):
    if report_cards:
        try:
            with open("ReportCards.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                
                # Writing headers to the CSV file
                writer.writerow(["Student Name", "Subject", "Marks", "Student ID", "Total Marks", "Percentage"])
                
                # Writing data rows to the CSV file
                for record in report_cards:
                    writer.writerow(record)
                
            print("Report cards exported successfully to ReportCards.csv.")
        
        except Exception as e:
            print(f"Error exporting report cards to CSV: {e}")
    else:
        print("No report cards available to export.")

