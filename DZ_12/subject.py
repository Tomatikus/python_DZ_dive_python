import csv

subjects = ["Informatics","Mathematics", "Physics", "Chemistry", "History"]

csv_file_path = "subjects.csv"
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Subjects"])
    for subject in subjects:
        writer.writerow([subject])

csv_file_path