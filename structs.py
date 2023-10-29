import datetime


#Пользователь
class User:

    def __init__(self, id):
        self.id = id
        self.counter = 0;
        self.tasks = []
#User


#Задача
class Task:

    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.timeAdd = TimeAdd()
        #self.deadline  = 'а будет?'

    def to_string(self):
        return f'Задача #{self.number}\n' \
                f'{self.name}\n' \
                f'({self.timeAdd.to_string()})\n\n'

    def print(self):
        print(f'{self.name}')
#Task


class TimeAdd:
    months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря', }

    def __init__(self, time=''):
        date = ''
        if (time == ''):
            date = str(datetime.datetime.now())
        else:
            date = time
        # 2021-09-29 22:04:34.851520
        self.year = date[:4]
        self.month = date[5:7]
        self.day = date[8:10]

        self.hour = date[11:13]
        self.minute = date[14:16]

    def to_string(self):
        return f"{self.day} {self.months[self.month]} {self.year} в {self.hour}:{self.minute}"

#TimeAdd
