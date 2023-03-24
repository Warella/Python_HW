from os.path import exists
from creating import creating
from writing import writing_txt, get_info
from model import read_phone_book


def view():
    print(read_phone_book('Phonebook.txt'))


def record_info():
    info = get_info()
    writing_txt(info)


def choice():
    flag = input(
        'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    while (flag.lower() == 'да'):
        path = 'Phonebook.txt'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            'Введите \'да\', если хотите записать новые данные, или любой другой символ, если хотите просмотреть справочник в консоли: ')
        if choice_action.lower() == 'да':
            record_info()
        else:
            view()
        flag = input(
            'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    print('Программа завершена.')