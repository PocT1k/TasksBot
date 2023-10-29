from aiogram import executor

from dpHand  import *
from database import *


def readBD():
    rows = DB_readTable()
    for row in rows:
        #print(row)

        if users.get(row[0]) is None:  # Если первая задача
            users[row[0]] = User(row[0])
        users[row[0]].counter = row[1]
        users[row[0]].tasks.append(Task(row[2], row[3]))
        users[row[0]].tasks[row[2]].timeAdd = TimeAdd(f'{row[4]}-{row[5]}-{row[6]} {row[7]}:{row[8]}')
pass

# number = users[user_id].counter
# number += 1
# users[user_id].counter = number
# users[user_id].tasks.append(Task(number, name))

if __name__ == '__main__':
    readBD()

    # users[854903492] = User(854903492)
    #
    # number = users[854903492].counter
    # number += 1
    # users[854903492].counter = number
    # users[854903492].tasks.append(Task(number, "Полить цветы"))
    #
    # number = users[854903492].counter
    # number += 1
    # users[854903492].counter = number
    # users[854903492].tasks.append(Task(number, "Прополоть картошку"))

    executor.start_polling(dp, skip_updates=True)
