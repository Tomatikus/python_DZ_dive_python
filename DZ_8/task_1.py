# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов 
# и директорий.

# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# "size": 4096
# }

import os
import json
import csv
import pickle

def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def traverse_and_save_info(directory):
    result = []

    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            dir_info = {
                "name": dirname,
                "parent": os.path.relpath(dirpath, directory),
                "type": "directory",
                "size": get_directory_size(os.path.join(dirpath, dirname))
            }
            result.append(dir_info)

        for filename in filenames:
            file_info = {
                "name": filename,
                "parent": os.path.relpath(dirpath, directory),
                "type": "file",
                "size": os.path.getsize(os.path.join(dirpath, filename))
            }
            result.append(file_info)

    return result

def save_to_json(data, filename):
    with open(f'{filename}.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, filename):
    with open(f'{filename}.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(data)

def save_to_pickle(data, filename):
    with open(f'{filename}.pkl', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

if __name__ == "__main__":
    input_directory = "Desktop\studing"
    output_json = "output.json"
    output_csv = "output.csv"
    output_pickle = "output.pkl"

    traversal_results = traverse_and_save_info(input_directory)

    save_to_json(traversal_results, output_json)
    save_to_csv(traversal_results, output_csv)
    save_to_pickle(traversal_results, output_pickle)
