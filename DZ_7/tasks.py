from os import listdir, rename, path

# ЗАДАЧА 2: Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из 
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и 
# расширение.
# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv

__all__ = ['rename_files']


def rename_files(wanted_name, count_nums, extension_old, extension_new, diapazon):
    directory = "test_dir"  # Укажите путь к каталогу, в котором нужно переименовать файлы
    
    for filename in listdir(directory):
        if filename.endswith(extension_old):
            base_name = filename[:-len(extension_old)]
            extension = extension_new
            
            if diapazon:
                start, end = diapazon
                original_part = base_name[start - 1:end]
                new_name = f"{original_part}{wanted_name}"
            else:
                new_name = wanted_name
            
            num = len([name for name in listdir(directory) if name.startswith(new_name)]) + 1
            num_str = str(num).zfill(count_nums)
            
            new_filename = f"{new_name}{num_str}{extension}"
            rename(path.join(directory, filename), path.join(directory, new_filename))

# Пример использования
rename_files(wanted_name="video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
