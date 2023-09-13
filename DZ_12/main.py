# Задание. Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра. 
# Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета 
# и по оценкам всех предметов вместе взятых.


from name_cheker import NameCheker
import csv


class Student:
    first_name = NameCheker()
    middel_name = NameCheker()
    last_name = NameCheker()
    
    def __init__(self, first_name: str, middel_name: str, last_name: str, csv_path: csv):
        self.first_name = first_name
        self.middel_name = middel_name
        self.last_name = last_name
        
        with open(csv_path, 'r') as l_lesson:
            reader = csv.reader(l_lesson)
            self.subjects = {row[0]:{"grades":[], "test_scores": []} for row in reader}
            
    def add_grade(self, subject: str, grade: int):
        if subject not in self.subjects:
            raise ValueError ("Предмет не найден в списке предметов")
        if grade < 2 or grade > 5:
            raise ValueError ("Оценка должна быть от '2' до '5'")
        self.subjects[subject]["grades"].append(grade)
        
    def add_test_score(self, subject: str, score: int):
        if subject not in self.subjects:
            raise ValueError ("Предмет не найден в списке предметов")
        if score < 0 or score > 100:
            raise ValueError ("Оценка за тест должна быть от '0' до '100' быллов.")
        self.subjects[subject]["test_scores"].append(score)
        
    def average_test_score(self, subject: str):
        if subject not in self.subjects:
            raise ValueError ("Предмет не найден в списке предметов")
        scores = self.subjects[subject]["test_scores"]
        return sum(scores) / len(scores) if scores else 0
    
    def averadge_grade(self):
        total_grades = [grade for subj in self.subjects.values() for grade in subj["grades"]]
        return sum(total_grades) / len(total_grades) if total_grades else 0


if __name__ == "__main__":
    stud1 = Student('Alan', 'Jamy', 'Rickman', 'subjects.csv')
    stud2 = Student('Vova', 'Chester', 'Missoury', 'subjects.csv')
    stud1.add_grade("Informatics",5)
    stud1.add_test_score("Chemistry",80)
    stud2.add_grade("Mathematics", 4)
    stud2.add_test_score("History", 66)
    
    print(f"Average grade: {stud1.averadge_grade()}")
    print(f"Average test score in History: {stud2.average_test_score('History')}")