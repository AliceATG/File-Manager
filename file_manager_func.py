import os
import shutil
from set_path import work_direct
begin_working_direct = work_direct

def create_folder():
    name_folder = str(input("Название новой папки: "))
    folder_path = os.path.join(work_direct, name_folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f'Папка "{name_folder}" успешно создана')   
    else:
        print(f'Папка "{name_folder}" уже существует')
        
def delete_folder():
    name_folder = str(input("Название папки для удаления: "))
    folder_path = os.path.join(work_direct, name_folder)
    try:
        shutil.rmtree(folder_path)
        print(f"Папка '{name_folder}' успешно удалена.")
    except FileNotFoundError:
        print(f"Папка '{name_folder}' не найдена.")
        
def move_to_folder():
    global work_direct
    print('Вы находитесь в данной директории: ',work_direct)
    name_folder = str(input("Название папки для прехода: "))
    if name_folder in work_direct:
        k = work_direct.split('\\')
        number = k.index(name_folder)
        work_direct = '\\'.join(k[:number])
    check_directory(work_direct)
    new_path = os.path.join(work_direct, name_folder)
    if os.path.exists(new_path):
        work_direct = new_path
        print(f"Перемещение в папку '{name_folder}' произошло успешно.")
    else:
        print(f"Папка '{name_folder}' не найдена в текущей директории.")
        
        
def create_file():
    file_name = str(input("Название файла для создания: "))
    file_path = os.path.join(work_direct, file_name)
    if not os.path.exists(file_path):
        open(file_path, 'w').close()
        print(f'Файл "{file_name}" успешно создан')
    else:
        print(f'Файл "{file_name}" уже существует')
        
def write_to_file():
    file_name = str(input("Название файла для записи текста: "))  
    txt = str(input('Введите текст для записи'))
    file_path = os.path.join(work_direct, file_name)
    if os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                file.write(txt)
                print('Текст успешно записан в файл')
        except IsADirectoryError:
            print('Это директория')
    else:
        print(f'Файл "{file_name}" не найден')
        
def read_file():
    file_name = str(input("Название файла для чтения текста: ")) 
    file_path = os.path.join(work_direct, file_name)
    try:
        with open(file_path, 'r') as file:
            txt = file.read()
            print(f"Содержимое файла '{file_name}':\n{txt}")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
        
def delete_file():
    file_name = str(input("Название файла для удаления: ")) 
    file_path = os.path.join(work_direct, file_name)
    try:
        os.remove(file_path)
        print(f"Файл '{file_name}' успешно удален.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")

def copy_file():
    begin_path = str(input("Путь файла: "))
    final_path = str(input("Путь скопированного файла: "))
    check_directory(work_direct = work_direct, begin_path = begin_path, final_path = final_path)
    try:
        shutil.copy2(begin_path, final_path)
        print(f"Файл '{begin_path}' скопирован в '{final_path}'.")
    except FileNotFoundError:
        print(f"Файл '{begin_path}' не найден.")
        
def move_file():
    begin_path = str(input("Путь начальной директории: "))
    final_path = str(input("Путь конечной директории: "))
    check_directory(work_direct = work_direct, begin_path = begin_path, final_path = final_path)
    try:
        shutil.move(begin_path, final_path)
        print(f"Файл '{begin_path}' перемещен в '{final_path}'.")
    except FileNotFoundError:
        print(f"Файл '{begin_path}' не найден.")


def rename_file():
    print('Вы находитесь в данной директории: ',work_direct)
    old_path = str(input('Укажите путь старого файла: '))
    new_name = str(input('Укажите новое название файла: '))
    k = old_path.split('\\')
    new_path = '\\'.join(k[:len(k)-1]) + f'\\{new_name}'
    check_directory(work_direct = work_direct, begin_path = old_path, final_path = new_path)
#     #new_path = os.path.join(work_direct, new_name)
#     opd_path = os.path.join(old_path, '')
#     new_path = os.path.join(new_path, '')
    try:
        os.rename(old_path, new_path)
        print(f"Файл  успешно переименован на '{new_name}'.")
    except FileNotFoundError:
        print(f"Файл '{old_path}' не найден.")

def check_directory(work_direct=None, begin_path = None, final_path = None):
    if begin_working_direct not in work_direct:
        return ('Выход за рабочую директорию')
    if begin_path is not None and final_path is not None:
        if begin_working_direct not in begin_path or begin_working_direct not in final_path:
            return ('Выход за рабочую директорию')
    
command_list = 'Создание папку - create_folder\nУдаление папки - delete_folder\nПеремещение в папку - move_to_folder\nСоздание файл - create_file\nЗапись в файл - write_to_file\nПросмотр содержимого файла - read_file\nУдаление файла - delete_file\nКопирование файла - copy_file\nПеремещение файла - move_file\nПереименование файла - rename_file\nВыход - exit\n'