# ░░░░░░░░░░░░░▄▄▄▄▄▄▄▄░░░░░░░░░░░░░ на момент создания этого текста время 4:50 утра, я истощен и счастлив, осилив лото
# ░░░░░░░░▄▄▀▀▀░░░░░░░░▀▀▀▄▄░░░░░░░░ для меня задание было трудным, некоторые моменты я искал в интернете,
# ░░░░░▄▄▀░░░░░░░░░░░░░░░░░░▀▄▄░░░░░ но по большей части это были запросы как сделать то или иное в питоне
# ░░░░█▀░░░░░░░░░░░░░░░░░░░░░░▀▄░░░░ также узнал очень много нового о блоке рандом и некоторых новых встроенных функциях
# ░░▄▀░░░░░░░░░░░░░░░░░░░░░░░░░░█▄░░
# ░▄█░░░▄██▀░░░░░░░░░░░░░░▀██▄░░░█▄░
# ░█░░▄█▀▀░░▄░░░░░░░░░░░░▄░░▀██▄░░█░
# ▄▀░░█▀▄███████▄░░░░▄███████▄▀█░░▀▄
# █░░░░░█▀░░░▄░▀▀░░░░▀▀░▄░░░▀█░░░░░█
# █░░░░░█░░░░█░░░░░░░░░░█░░░░█░░░░██
# ▀█░░░░█░░░░█░░░▄▄▄▄░░░█░░░░█░░░░█░
# ░█░░░░█░░░██░▄█▀░░▀█▄░██░░░█░░░░█░
# ░░█░░░█░░░██░██▄▄▄▄██░██░░░█░░░█░░
# ░░░▀▄░█░░░██░████████░██░░░█░▄▀░░░
# ░░░░▀▄█▄░░██░▀██████░░██░░▄█▄▀░░░░
# ░░░░░░▀█▄▄██░░░░▀▀░░░░██▄▄█▀░░░░░░
# ░░░░░░░░░▀▀█▄▄▄▄▄▄▄▄▄▄█▀▀░░░░░░░░░
import random

class Card:
    def __init__(self, player_type):
        self.player_type = player_type
        self.card = [[], [], []]
        self.stroked_nums = 0
        self.numbers = random.sample(range(1, 91), 90)

        for line in self.card:
            for _ in range(4):
                line.append(' ')
            for _ in range(5):
                line.append(self.numbers.pop())

        def nums_and_spaces(x):
            if isinstance(x, int):
                return x
            return random.randint(1, 90)

        for index, line in enumerate(self.card):
            self.card[index] = sorted(line, key=nums_and_spaces)

    def check_number(self, number):
        for line in self.card:
            if number in line:
                return True
        return False

    def stroke_number(self, num):
        for index, line in enumerate(self.card):
            for num_index, num_in_card in enumerate(line):
                if num == num_in_card:
                    self.card[index][num_index] = '-'
                    self.stroked_nums += 1
                    if self.stroked_nums >= 15:
                        raise Exception(f'{self.player_type} победил')
                    return True
        return False


    def __str__(self):
        header = f'\n{self.player_type}:\n--------------------------'
        body = '\n'
        for line in self.card:
            for field in line:
                body += str(field).ljust(3)
            body += '\n'
        return header + body


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.nums_count = 90
        self.bag_nums = random.sample(range(1, 91), 90)

    def get_num(self):
        return self.bag_nums.pop()

    def start(self):
        for i in range(90):
            print(self.player, self.computer)
            num = self.get_num()
            print(f'Новый бочонок {num}, осталось {len(self.bag_nums)}')
            choice = input('Хотите зачеркнуть? Если да, нажмите "y", если нет - "n"\n')
            if choice == 'y':
                if not self.player.stroke_number(num):
                    print('Игрок проиграл!')
                    break
            elif self.player.chek_number(num):
                print('Игрок проиграл!')
                break
            if self.computer.chek_number(num):
                self.computer.stroke_number(num)


human_player = Card('Игрок')
computer_player = Card('Компьютер')

game = Game(human_player, computer_player)
game.start()



