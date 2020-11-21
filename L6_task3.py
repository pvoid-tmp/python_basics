# Lesson 6 task 3
# проверки типов данных отсуствуют

class Employee:  # не стал называть class Worker, уж больно на "Рабочий класс" похоже

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Employee):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


# main
p1 = Position("Maria Jose", "de la Casa", "IT manager", 20000.0, 8800.0)
print(f"{p1.get_full_name()}, {p1.position}, income: {p1.get_total_income():.2f}")
p2 = Position("Aisha", "Buck", "coffey lady", 7200.0, 0.0)
print(f"{p2.get_full_name()}, {p2.position}, income: {p2.get_total_income():.2f}")
