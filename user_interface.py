import keyboard


def start_menu():
    while True:
        print("Это приложение для работы с заметками !!!")
        type_numbers = input("Выберите действие из списка\n"
                             "1 - Начало работы\n"
                             "2 - Выход\n"
                             ).strip()
        match type_numbers:
            case "1":
                menu_notes(type_numbers)
            case "2":
                print("Досвидания!!!")
                exit()
            case _:
                print("Вы выбрали неправилиную команду!!!! Повторите ввод!")


def menu_notes(type_numbers):
    while True:
        if type_numbers == "1":
            print("Меню приложения")
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
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "2":
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "3":
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "4":
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "5":
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "6":
                    print("Для продолжения нажмите пробел!!!")
                    pause()
                case "0":
                    break
                case _:
                    print("Неправильный выбор!!! Повторите выбор!!!")


def pause():
    while True:
        if keyboard.read_key() == 'space':
            break


start_menu()