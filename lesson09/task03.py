# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    name = ''
    surname = ''
    position = ''
    __income = {"wage": 0, "bonus": 0}

    def get_income(self):
        return self.__income

    def set_bonus(self, sum):
        self.__income['bonus'] = sum

    def set_wage(self, sum):
        self.__income['wage'] = sum


class Position(Worker):
    def get_full_name(self):
        return ' '.join((self.surname,self.name))

    def get_total_income(self):
        inc_dict = Worker.get_income(self)
        return sum(inc_dict.values())


pos = Position()
pos.name = 'иванов'
pos.surname = 'илья'
pos.set_bonus(12300)
pos.set_wage(3000)
print(pos.get_full_name())
print(pos.get_total_income())
