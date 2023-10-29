from aiogram import executor

from dpHand import *
from database import *


def readBD():
    rows = DB_readTable()
    for row in rows:
        if users.get(row[0]) is None:  # Если первая задача
            users[row[0]] = User(row[0])
        users[row[0]].counter = row[1]
        users[row[0]].tasks.append(Task(row[2], row[3]))
        users[row[0]].tasks[row[2]].timeAdd = TimeAdd(f'{row[4]}-{row[5]}-{row[6]} {row[7]}:{row[8]}')
pass

if __name__ == '__main__':
    readBD()
    executor.start_polling(dp, skip_updates=True)
