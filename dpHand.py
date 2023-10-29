from config import *
from structs import *
from database import *


markup = types.ReplyKeyboardRemove() #Пустая клавиатура

@dp.message_handler(commands=['myid']) # Обработчик команды /myid
async def myid(message: types.Message):
    await message.answer(message.from_user.id,
                         reply_markup=markup)
#myid

@dp.message_handler(commands=['help']) # Обработчик команды /help
async def help(message: types.Message):
    await message.answer("/task - работа с задачами",
                         reply_markup=markup)
#help

@dp.message_handler(commands=['start']) # Обработчик команды /start
async def start(message: types.Message):
    # Отправляем приветственное сообщение с клавиатурой
    await message.answer("Здравсвуйте, я - ваш бот-помощник.\n"
                         "Я помогу запомнить ваши задачи.\n"
                         "/task - работа с задачами",
                         reply_markup=markup)

    user_id = message.from_user.id

    #Проверка на то, что у юзера уже есть задачи
    if users.get(user_id) is None:
        await message.answer("Похоже у вас нет никаких задач, как насчёт их создать?",
                             reply_markup=markup)
#start

@dp.message_handler(commands=['task']) # Обработчик команды /task
async def task(message: types.Message):
    user_id = message.from_user.id

    #Если у пользователя нет задач
    if users.get(user_id) is None:
        await message.answer("Список задач пуст",
                             reply_markup=markup)
        return
    #Принт задач пользователя
    else:
        answ = ''
        #Перебор задач пользователя
        for task in users[user_id].tasks:
            if task.number == 0:
                continue
            answ += task.to_string()

        if answ == '':
            await message.answer("Список задач пуст",
                                 reply_markup=markup)
            return
        else:
            await message.answer(answ, reply_markup=markup)

    #Как пользоваться ботом
    await message.answer("/tn Название\n"
                         "- новая задача\n"
                         "/tr Номер НовоеИмя\n"
                         "- изменить задачу\n"
                         "/td Номер\n"
                         "- удалить задачу",
                         reply_markup=markup)
#task

@dp.message_handler(commands=['tn']) # Обработчик команды /tn
async def tn(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    name = text[4:]

    # Если введено название
    if name != '':
        if users.get(user_id) is None: #Если первая задача
            users[user_id] = User(user_id)
            users[user_id].tasks.insert(0, Task(0, name='fake'))

        number = users[user_id].counter
        number += 1
        users[user_id].counter = number
        users[user_id].tasks.append(Task(number, name))

        await message.answer(f"Задача №{number}:\n{name}\n"
                             f"Успешно добавлена",
                             reply_markup=markup)

    else:
        await message.answer("Не введено название",
                             reply_markup=markup)
#tn

@dp.message_handler(commands=['tr']) # Обработчик команды /tr
async def tr(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    text = text[4:]
    array = text.split()

    if (len(array) == 0):
        await message.answer("Не введён номер",
                             reply_markup=markup)
        return

    # Если введено не число
    if (array[0].isdigit() == False) or (array[0] == '0'):
        await message.answer("Не корректно введён номер",
                             reply_markup=markup)
        return

    number = int(array.pop(0))
    newName = ' '.join(array)
    #Ищем нужную задачу
    if newName == '':
        await message.answer("Не введено название",
                             reply_markup=markup)
        return
    try:
        users[user_id].tasks[number].name = newName

        await message.answer("Задача изменена",
                             reply_markup=markup)
    except IndexError:
        await message.answer(f"Задачи с номером {number} нет",
                             reply_markup=markup)
#tr

@dp.message_handler(commands=['td']) # Обработчик команды /td
async def td(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    text = text[4:]
    array = text.split()

    if (len(array) == 0):
        await message.answer("Не введён номер",
                             reply_markup=markup)
        return

    # Если введено не число
    if (array[0].isdigit() == False) or (array[0] == '0'):
        await message.answer("Не корректно введён номер",
                             reply_markup=markup)
        return

    delNumber = int(array.pop(0))
    #Ищем нужную задачу
    try:
        del users[user_id].tasks[delNumber]

        users[user_id].counter = users[user_id].counter - 1
        # Перебор задач пользователя
        number = 0
        for task in users[user_id].tasks:
            print(number, task.name)
            task.number = number
            number += 1

        await message.answer("Задача удалена",
                             reply_markup=markup)
    except IndexError:
        await message.answer(f"Задачи с номером {delNumber} нет",
                             reply_markup=markup)
#td

@dp.message_handler(commands=['save']) # Обработчик команды /save
async def save(message: types.Message):
    DB_delete()
    DB_create()

    for user in users:
        for task in users[user].tasks:
            DB_writeTask(users[user], task)

    await message.answer(f"Изменения сохранены",
                         reply_markup=markup)
#save

@dp.message_handler(commands=['end']) # Обработчик команды /end
async def end(message: types.Message):
    user_id = message.from_user.id

    if user_id == 854903492:
        await message.answer(f"Остановка бота",
                             reply_markup=markup)
        exit(0)
#end
