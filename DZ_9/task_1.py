


import math
import json
import csv
import random
import csv


def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # Корней нет
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return print(root1, root2)


def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.random() for _ in range(3)]
            writer.writerow(row)


def quadratic_solver_decorator(func):
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(float, row)
                roots = func(a, b, c)
                print(f"For coefficients {a}, {b}, {c}: Roots = {roots}")
    return wrapper


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "parameters": args,
                "result": result
            }
            with open(f'{filename}.json', 'a') as file:
                json.dump(data, file)
                file.write('\n')
            return result
        return wrapper
    return decorator



@save_to_json("results.json")
@quadratic_solver_decorator
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # Корней нет
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    
if __name__=="__main__":
    print(solve_quadratic())