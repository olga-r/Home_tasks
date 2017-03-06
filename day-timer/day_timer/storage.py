import sqlite3

SQL_SELECT = '''
      SELECT 
          id, task_name, task_descr, task_date, task_status
      FROM
          dairy
'''
def dict_factory(cursor, row):
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    return d
        
        
def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'   
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn

def initialize(conn):
    with conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS dairy (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                task_name TEXT NOT NULL DEFAULT '',
                task_descr TEXT NOT NULL DEFAULT '',
                task_date DATETIME NOT NULL,
                task_status TEXT NOT NULL
               )
            ''')
def add_note(conn, task_name, task_descr, task_date, task_status ):
    with conn:
        cursor = conn.execute('''
            INSERT INTO dairy (
            task_name, task_descr, task_date, task_status
            ) VALUES (
            ?, ?, ?, ?
            ) 
            ''', (task_name, task_descr, task_date, task_status))  
        pk = cursor.lastrowid
    idx = 'Task is created. Unique ID is {}'.format(pk)
    return idx

def update_table(conn, pk, task_name, task_descr, task_date, task_status, ):
    with conn:
        conn.execute('''
        UPDATE dairy SET task_name=?, task_descr=?, task_date=?, task_status=? WHERE id=? 
         ''', (task_name, task_descr, task_date, task_status, pk))
    print('Задача обновлена')

def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT)
        return cursor.fetchall()
        
def find_note_by_pk(conn, pk):
    with conn:
        cursor = conn.execute(SQL_SELECT + ' WHERE id = ?', (pk,))
        return cursor.fetchone()


__all__ = [
    'initialize', 'add_note', 'find_all', 'find_note_by_pk', 'update_table'
]



