
import model
import view

def start():
    model.open_file()

    while True:
        nb = model.get_note_book()
        choice = view.main_menu()

        match choice:

            case 1:
                if not nb:
                    view.show_massage('->->-> Записная книжка пуста')
                else:
                    view.show_notes(nb)

            case 2:
                if not nb:
                    view.show_massage('->->-> Записная книжка пуста')
                else:
                    view.find_notes(nb)

            case 3:
                model.add_note(view.add_note(nb))
                view.show_massage('Заметка добавлена')

            case 4:
                if not nb:
                    view.show_massage('->->-> Записная книжка пуста')
                else:
                    id_note = view.input_id('Введите ID заметки, которую хотите изменить: ')
                    note = view.change_note(nb,id_note)
                    if note:
                        model.change_note(note,id_note)
                        view.show_massage(f'Заметка {id_note} изменена')
                    else:
                        view.show_massage('Заметка с таким ID не найдена')

            case 5:
                if not nb:
                    view.show_massage('->->-> Записная книжка пуста')
                else:
                    delNoteId = view.input_id('Введите ID заметки, которую хотите удалить: ')
                    if model.del_note(delNoteId):
                        view.show_massage('Заметка удалена')
                    else:
                        view.show_massage('Заметка с таким ID не найдена')

            case 6:
                yes_or_no = view.input_yn('Хотите сохранить изменения (Y/N) ? : ')
                if yes_or_no == 'y':
                    model.save_file()
                    view.show_massage('Записная книжка сохранена')
                view.show_massage('Конец работы')
                return






