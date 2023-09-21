# Вариант 1: Возьмите любые 1-3 задания из прошлых домашних заданий. 
# Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров.


import argparse
import logging
from DZ_13.exception import StudentNameException, InvalidScoreException, InvalidSubjectException
from DZ_13.main import Student


logging.basicConfig(filename='student.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description='Process student information.')
    parser.add_argument('name', help='Student name')
    parser.add_argument('csv_filename', help='CSV filename')
    args = parser.parse_args()

    try:
        student = Student(args.name, args.csv_filename)
        
        # Вызываем ошибку класса Student 
        student.add_score('Math', 6)

    except StudentNameException:
        logging.error('Invalid student name format.')
    except InvalidSubjectException as e:
        logging.error(f'Invalid subject: {e.subject}')
    except InvalidScoreException as e:
        logging.error(f'Invalid score: {e.score}')

if __name__ == '__main__':
    main()

# python my_script.py John subjects.csv - запуск из командной строки
# Где my_script.py - имя файла со скриптом, John - имя студента, subjects.csv - имя CSV-файла с предметами."""








