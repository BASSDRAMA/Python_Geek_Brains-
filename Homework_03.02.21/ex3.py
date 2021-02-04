class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': float(wage), 'bonus': float(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)


    def get_full_name(self):
        print(f'Co-worker name: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'{self._income["wage"] + self._income["bonus"]} проплаченных деревянных - total worker income')

co_worker1 = Position('Олегсей', 'Нувульный', 'Секретный отдел Госдепа СЩА', 150000, 15000000000)

co_worker1.get_full_name()
co_worker1.get_total_income()
