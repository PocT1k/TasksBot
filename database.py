import sqlite3

from config import DATA_BASE
from structs import *


conn = sqlite3.connect(DATA_BASE)
cur = conn.cursor()

def DB_delete():
    cur.execute('DROP TABLE IF EXISTS tasks')
    conn.commit()
pass

def DB_create():
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS tasks

            (user_id        INTEGER,
            user_counter    INTEGER,

            task_number     INTEGER,
            task_name       TEXT,

            task_year       TEXT,
            task_month      TEXT,
            task_day        TEXT,
            task_hour       TEXT,
            task_minute     TEXT
            );'''
    )
    conn.commit()
pass

def DB_writeTask(user, task):
    DB_create()
    cur.execute(
        f'''INSERT INTO tasks (user_id, user_counter, task_number, task_name, task_year, task_month, task_day, task_hour, task_minute)
            VALUES ({user.id}, {user.counter}, {task.number}, "{task.name}", {task.timeAdd.year}, {task.timeAdd.month}, {task.timeAdd.day},
            {task.timeAdd.hour}, {task.timeAdd.minute});'''
    )
    conn.commit()
pass

def DB_readTable():
    DB_create()
    cur.execute("SELECT * FROM tasks")
    return cur.fetchall()
pass
