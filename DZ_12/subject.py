import csv

subjects = ["Информатика","Математика", "Физика", "Химия", "История"]

csv_file_path = "subjects.csv"
with open(csv_file_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Subjects"])
    for subject in subjects:
        writer.writerow([subject])

csv_file_path