from main import Student

stud1 = Student('Alan Rickman', 'subjects.csv')
stud2 = Student('Vova Chester', 'subjects.csv')
#stud1.add_score("Информатика",7) # exception.InvalidScoreException: Оценка '7'. Результаты тестов от 0 до 100,а оценки должны быть от 2 до 5
stud1.add_test_result("Математика",80)
stud2.add_score("Математика", 4)
stud2.add_test_result("Информатика", 66)
#stud2.add_score("Литература", 5) # exception.InvalidSubjectException: Предмет 'Литература' не найден в файле CSV
print(stud1.average_test_score("Математика"))
print(stud2.average_score())