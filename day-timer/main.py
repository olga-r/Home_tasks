import sys
from day_timer import storage
from day_timer.check import check_date
from day_timer.check import check_string

conn = storage.connect('tasks.db')
storage.initialize(conn)

def check_id(pk):
    note = storage.find_note_by_pk(conn, pk)
    if not note:
        print('ID "{}" не существует в БД'.format(pk))
    else:
        return pk, note
    
    
def action_find_all():
    notes = storage.find_all(conn)
    for note in notes:
        print('{note[task_name]} - {note[task_descr]} - {note[task_date]} - {note[task_status]}'.format(note=note))

def action_edit():
    pk = int(input('Введите ID редактируемой записи: '))
    if check_id(pk):
        pk, note = check_id(pk)
        print('Под данным ID существует запись: {note[task_name]} - {note[task_descr]} - {note[task_date]}'.format(note=note))
        answer = input('Вы хотите изменить название задачи Y/N?: ')
        name = check_string(task = "название") if answer == "Y" else note['task_name']
        answer = input('Вы хотите изменить описание задачи Y/N?: ')
        descr = check_string(task = "описание") if answer == "Y" else note['task_descr']
        answer = input('Вы хотите изменить время выполнения задачи Y/N?: ')
        date = check_date() if answer == "Y" else note['task_date'] 
        storage.update_table(conn, pk, name, descr, date, note['task_status']) 

def action_add():
    name = check_string(task = "название")
    description = check_string(task = "описание")
    task_date = check_date(check_for_time = True)
    status = "Не выполнено"
    idx = storage.add_note(conn, name, description, task_date, status )
    print(idx)

def action_finish():
    pk = int(input('Введите ID редактируемой записи: '))
    if check_id(pk):
        pk, note = check_id(pk)
        print('Под данным ID существует запись: {note[task_name]} - {note[task_descr]} - {note[task_date]} - {note[task_status]}'.format(note=note))
        answer = input(' Изменить ее статус на выполнено? Y/N: ')
        status = "Выполнено" if answer == "Y" else "Не выполнено" 
        storage.update_table(conn, pk, note['task_name'], note['task_descr'], note['task_date'], status)
    
def action_start_again():
    pk = int(input('Введите ID редактируемой записи: '))
    if check_id(pk):
        pk, note = check_id(pk)
        print('Под данным ID существует запись: {note[task_name]} - {note[task_descr]} - {note[task_date]} - {note[task_status]}'.format(note=note))
        answer = input(' Изменить ее статус на не выполнено? Y/N: ')
        status = "Не выполнено" if answer == "Y" else "Выполнено" 
        storage.update_table(conn, pk, note['task_name'], note['task_descr'], note['task_date'], status)  
    
def action_show_menu():
    print("""Ежедневник. Выберите действие:
                  
1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
m. Показать меню
q. Выход
              
""")

    
def action_exit():
    conn.close()
    sys.exit(0)

actions = {
    '1': action_find_all,
    '2': action_add,
    '3': action_edit,
    '4': action_finish,
    '5': action_start_again,
    'm': action_show_menu,
    'q': action_exit
}

if __name__ == '__main__':
    action_show_menu()
    while True:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)
        if action:
            action()
        else:
            print('Неизвестная команда')
