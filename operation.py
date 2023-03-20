from datetime import date
import uuid
from os import path


def create_note():
    id_note = str(uuid.uuid1())[0:3]
    title_note = input("Введите название заметки: ")
    body_note = input("Введите содержание заметки: ")
    date_note = str(date.today())
    str_note = (id_note + ";" + title_note + ";" + body_note + ";" + date_note + "\n")
    create_file_notes(str_note)
    return print("Заметка сохранена")


def create_file_notes(text):
    with open('notes.cvs', 'a', encoding='utf-8') as data:
        data.write(text)


def read_notes_from_file():
    array_notes = []
    if path.exists('notes.cvs'):
        with open('notes.cvs', 'r', encoding='utf-8') as data:
            notes = data.read().strip().split('\n')
            for note in notes:
                split_note = note.split(';')

                array_notes.append(split_note)
        return array_notes


def show_notes():
    input_array = read_notes_from_file()
    for arr in input_array:
        print('ID - ' + arr[0] + '\n' +
              'Назавание заметки - ' + arr[1] + '\n' +
              'Содержание заметки - ' + arr[2] + '\n' +
              'Дата создания - ' + arr[3]
              )



