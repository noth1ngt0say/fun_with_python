import psycopg2
import config_db
from abc import ABC, abstractmethod


# Singleton

class DB:
    __instance__ = None

    def __init__(self, host, port, user, password, dbname):
        if DB.__instance__ is None:
            self.host = host
            self.port = port
            self.user = user
            self.passwd = password
            self.db = dbname
            # self.conn = self.connect()
            DB.__instance__ = self
        else:
            raise Exception("Мы не можем создать новый класс!")

    def connect(self):
        try:

            return psycopg2.connect(
                user=self.user,
                password=self.passwd,
                host=self.host,
                port=self.port,
                database=self.db
            )

        except psycopg2.OperationalError as e:
            print(f"Ошибка подключения к базе данных: {e}")

    @staticmethod
    def get_instance():
        if DB.__instance__ is None:
            DB(config_db.host, config_db.port, config_db.user, config_db.password,
               config_db.dbname)  # Создание первого экземпляра
        return DB.__instance__

    # def execute(self):
    #     sql = "SELECT employee_name FROM employee e WHERE e.employee_name ILIKE '%Garcia%'"
    #     try:
    #         cur = self.conn.cursor()
    #         cur.execute(sql)
    #         results = cur.fetchall()
    #         for row in results:
    #             print(*row)
    #     except Exception as e:
    #         raise Exception(f"Ошибка выполнения SQL-запроса: {e}")
    #     finally:
    #         cur.close()


#  2. Реализовать фабрику которая создает модели различных производителей

class AbsCar(ABC):
    @abstractmethod
    def sold(self):
        """Автомобиль продан"""
        pass

    @abstractmethod
    def discount(self):
        """Скидка на автомобиль"""
        pass


class Car(AbsCar):
    def __init__(self, brand, model):
        """Инициализируйте атрибуты brand и model"""
        self.brand = brand
        self.model = model

    def __repr__(self):
        "Реализуйте логику дандера"
        return f'Brand={self.brand} Model={self.model}'

    def sold(self):
        """Автомобиль продан"""
        print(f"Автомобиль {self.brand} {self.model} продан ")

    def discount(self):
        """Скидка на автомобиль"""
        print(f"На автомобиль {self.brand} {self.model} скидка 5%")

    @staticmethod
    def make_lada():
        "реализуйте метод для создания  автомобиля Lada"
        return Car(brand='Lada', model='2108')

    @staticmethod
    def make_mercedes():
        "реализуйте метод для создания  автомобиля Mercedes"
        return Car(brand='Mercedes', model='G-Classe')

    @staticmethod
    def make_toyota():
        "реализуйте метод для создания создания Toyota"
        return Car(brand='Toyota', model='Celica')



home_task_menu = """
    1. Задание Singleton
    2. Реализация класса Car и абстрактного класса
"""
print(home_task_menu)
home_task_menu_point = int(input('Введите номер части для проверки задания: '))

match home_task_menu_point:
    case 1:
        print(f'Выполняется запрос: \n'
              f'"mongo = DB(config_db.host, config_db.port, config_db.user, config_db.password, config_db.dbname\n'
              f'print(mongo)""')
        mongo = DB(config_db.host, config_db.port, config_db.user, config_db.password, config_db.dbname)
        print(mongo)
        print()
        print(f'Выполняется запрос: \n'
              f'"my_db = DB.get_instance()\n'
              f'print(my_db)"')
        my_db = DB.get_instance()
        print(my_db)
        print()
        print(f'Выполняется запрос: "'
              f'new_gover = DB(config_db.host, config_db.port, config_db.user, config_db.password, config_db.dbname)"')
        new_gover = DB(config_db.host, config_db.port, config_db.user, config_db.password, config_db.dbname)

    case 2:
        print(f'Выполняется запрос: '
              f'car = Car.make_lada()\n'
              f'car.sold()  для класса Car абстрактный класс\n'
              f'car.discount() для класса Car абстрактный класс\n')
        car = Car.make_lada()
        car.sold()
        car.discount()

