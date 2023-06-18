note_book = []
path = 'my_note_book.txt'

def open_file():
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for fields in data:
            fields = fields.strip().split(';')
            note = {'id': fields[0],
                    'title': fields[1],
                    'body': fields[2],
                    'date': fields[3]}
            note_book.append(note)
        note_book.sort(key=lambda x: x['date'], reverse=True)

    except FileNotFoundError:
        pass

def get_note_book():
    return note_book

def add_note(note):
    note_book.insert(0,note)


def change_note(note_change: dict, id_note: str):
    for note in note_book:
        if note.get('id') == id_note:

            note_book.remove(note)
            note_book.insert(0,note_change)


def save_file():
    data = []
    for note in note_book:
        data.append(';'.join(note.values()))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def del_note(delId: str):
    for note in note_book:
        if note.get('id') == delId:
            print(note.get('id'))
            note_book.remove(note)
            return True
    return False
