import keyboard
from logg import logging
from operation import create_note


def start_menu():
    while True:
        logging.info("Главное меню")
        print("Главное меню !!!")
        type_numbers = input("Выберите действие из списка\n"
                             "1 - Операции\n"
                             "2 - Выход\n"
                             ).strip()
        match type_numbers:
            case "1":
                logging.info("Вход в меню Операции")
                menu_notes(type_numbers)
            case "2":
                logging.info("Окончание работы")
                print("Досвидания!!!")
                exit()
            case _:
                logging.info("Некорректый ввод")
                print("Вы выбрали неправилиную команду!!!! Повторите ввод!")


def menu_notes(type_numbers):
    while True:
        if type_numbers == "1":
            print("Меню операций")
            type_operation = input("Выберите операцию\n"
                                   "1 - Добавление новой заметки\n"
                                   "2 - Показать все заметки\n"
                                   "3 - Удаление заметки\n"
                                   "4 - Редактирование заметки\n"
                                   "5 - Поиск заметки по дате\n"
                                   "6 - Поиск заметки по номеру\n"
                                   "0 - Возврат в стартовое меню\n"
                                   ).strip()
            match type_operation:
                case "1":
                    logging.info("Выбор операции - Добавление новой заметки")
                    create_note()
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "2":
                    logging.info("Выбор операции - Показать все заметки")
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "3":
                    logging.info("Выбор операции - Удаление заметки")
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "4":
                    logging.info("Выбор операции - Редактирование заметки")
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "5":
                    logging.info("Выбор операции - Поиск заметки по дате")
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "6":
                    logging.info("Выбор операции - Поиск заметки по номеру")
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "0":
                    logging.info("Выход в главное меню")
                    break
                case _:
                    logging.info("Некорректый ввод")
                    print("Неправильный выбор!!! Повторите выбор!!!")


def pause():
    while True:
        if keyboard.read_key() == 'space':
            break


start_menu()