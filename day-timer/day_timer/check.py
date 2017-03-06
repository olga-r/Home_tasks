from datetime import datetime
from .storage import find_note_by_pk

def check_date(check_for_time = False):
    while True:
        try:
            year, month, date, hour, minutes, seconds = map(int, input(""" 
Введите время выполнения задачи в формате год/месяц/день/час/минуты/секунды задачи: """).strip().split('/'))
            task_date = datetime(year, month, date, hour, minutes, seconds)
        except ValueError:
            print("Введенное время некорректно")
            task_date = check_date(check_for_time = False)
            break
        else:
            break
    if check_for_time:
        while datetime.today() >= task_date:
            print("Задача может планироваться только на будущее.")
            task_date = check_date(check_for_time = True)
    return task_date

    
def check_string(task= ""):
    string = ""
    while True:
        if string:
            break
        else:
            string = input('Введите {} задачи: '.format(task))
            if task != "название":
                break 
    return string  

