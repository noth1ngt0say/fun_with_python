# Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from datetime import datetime
import random

CONFIG_FILE = 'loger.conf'
LOG_FILE = 'debug.log'


class SomeMethod: # Пытаемся в ООП
    @staticmethod
    def get_count(func_name): # Получение счетчика
        with open(CONFIG_FILE, 'r') as cf:
            for line in cf:
                key, value = line.strip().split('=')
                if key == f'{func_name}_count':
                    return int(value)

    @staticmethod
    def update_count(func_name, new_count): # Обновление счетчика после выполнения
        counters = {}
        with open(CONFIG_FILE, 'r') as cf:
            for line in cf:
                key, value = line.strip().split('=')
                counters[key] = value
        counters[f'{func_name}_count'] = new_count
        with open(CONFIG_FILE, 'w') as cf:
            for key, value in counters.items():
                cf.write(f'{key}={value}\n')

    @staticmethod
    def update_log(func_name, count): # Обновление лог-файла
        last_time = datetime.now().strftime("%d.%m.%Y %H:%M")
        with open(LOG_FILE, 'a') as lf:
            lf.write(f'{func_name}, {count}, {last_time}\n')


def SomeClass(func): # Декоратор
    def wrapper(*args, **kwargs):
        func_name = func.__name__ # Получение имени функции
        count = SomeMethod.get_count(func_name)
        count += 1
        SomeMethod.update_count(func_name, count)
        SomeMethod.update_log(func_name, count)
        return func(*args, **kwargs)

    return wrapper


class Execute: # Декоратор для методов
    @SomeClass
    def say_no(self):
        print('NO!')

    @SomeClass
    def render(self):
        print('Что такое рендер?!')

    @SomeClass
    def show(self, show):
        print(f'Мы смотрим: {show}')


exe = Execute()

tv_show = ["Monty Python's Flying Circus", "Die hard", "Мужское/Женское", "Дом 2"]

exe.render()
exe.say_no()
exe.show(random.choice(tv_show))
exe.say_no()
exe.show(tv_show[random.randint(0, len(tv_show) - 1)])
exe.say_no()
exe.say_no()
exe.show(tv_show[random.randint(0, len(tv_show) - 1)])
exe.render()
