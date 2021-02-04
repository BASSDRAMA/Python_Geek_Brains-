class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('pen is drawing circles')


class Pencil(Stationary):
    def draw(self):
        print('pencil is charting lines')


class Handle(Stationary):
    def draw(self):
        print('handle is highlighting text')


pen1 = Pen('Blue Pen')
pen1.draw()

pencil1 = Pencil('Red Pencil')
pencil1.draw()

handle1 = Handle('Yellow Handle')
handle1.draw()

