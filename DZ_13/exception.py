# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода.


class StudentNameException(Exception):
    def __init__(self, message="Имя студента введено неверно. Оно должно содержать только буквы и начинаться с заглавной буквы."):
        self.message = message
        super().__init__(self.message)    
    
class InvalidSubjectException(Exception):
    def __init__(self,subject_name):
        self.massage = f"Предмет '{subject_name}' не найден в файле CSV"
        super().__init__(self.massage)
    
class InvalidScoreException(Exception):
    def __init__(self, score, score_type = 'Оценка'):
        self.massage = f"{score_type} '{score}'. Результаты тестов от 0 до 100,а оценки должны быть от 2 до 5"
        super().__init__(self.massage)