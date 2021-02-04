class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_mass(self):
        mass = float(self._length * self._width * 25 * 5 / 1000)
        print(f'Asphalt mass is about: {mass} t')

new_road = Road(3400, 230)
new_road.get_asphalt_mass()
