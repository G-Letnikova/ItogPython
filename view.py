import text_fields
from datetime import datetime

def main_menu() -> int:
    print(text_fields.main_menu)
    length_menu = len(text_fields.main_menu.split('\n'))-1

    while True:
        choice = input('Выберете пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            return int(choice)
        else:
            print(f'Введите число от 1 до {length_menu}')


def show_notes(book: list[dict]):
    print(f"{'Дата ':<12} "
          f"{'ID ':<5} "
          f"{'Заголовок ':<15} "
          f"{'Заметка'} ")
    for note in book:
        print(f"{note.get('date'):<12} "
              f"{note.get('id'):<5} "
              f"{note.get('title'):<15} "
              f"{note.get('body')} ")


def add_note(book):
    title = input('Заголовок: ')
    body = input('Заметка: ')
    date = datetime.now().date().strftime('%d-%m-%Y')

    arr_id = []
    for note in book:
        arr_id.append(int(note.get('id')))

    id = 1
    for i in range(len(arr_id)):
        if id in arr_id:
            id += 1
    id = str(id)

    return {'id': id, 'title': title, 'body': body, 'date': date}


def input_index(massage: str):
    return int(input(massage))


def input_id(massage: str):
    return input(massage)


def change_note(book: list[dict], id_note: str):
    for note in book:
        if note.get('id') == id_note:
            title = input('Введите заголовок заметки: ')
            body = input('Введите текст заметки: ')
            note = {'id': id_note, 'title': title, 'body': body, 'date': datetime.now().date().strftime('%d-%m-%Y')}
            return note
    return None


def show_massage(massage: str):
    print('->->->',massage)


def input_serch(massage):
    return input(massage)


def input_yn(massage):
    return input(massage).lower()


def input_del(massage: str, len_del_list) -> int:
    num = input(massage)
    if num == '':
        return 0
    while True:
        if num.isdigit() and 0 < int(num) <= len_del_list:
            return int(num)
        else:
            num = input(massage)


def find_notes(book: list[dict]):
    date_note = input("введите дату (дд-мм-гг): ")
    flag = True
    print(f"{'Дата ':<12} "
          f"{'ID ':<5} "
          f"{'Заголовок ':<15} "
          f"{'Заметка'} ")
    for note in book:
        if date_note == note.get('date'):
            print(f"{note.get('date'):<12} "
                  f"{note.get('id'):<5} "
                  f"{note.get('title'):<15} "
                  f"{note.get('body')} ")
            flag = False
    if flag:
        print(f'за {date_note} заметок нет')

