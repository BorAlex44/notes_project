from datetime import datetime, date
import uuid


def create_note():
    id_note = str(uuid.uuid1())[0:3]
    title_note = input("Введите название заметки: ")
    body_note = input("Введите содержание заметки: ")
    date_note = str(date.today())
    str_note = (id_note + ";" + title_note + ";" + body_note + ";" + date_note + "\n")
    return print(str_note)

