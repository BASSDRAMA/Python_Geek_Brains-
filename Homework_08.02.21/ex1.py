class Matrix:
    def __init__(self, new_list):
        self.new_list = new_list

    def __str__(self):
        for row in self.new_list:
            for i in row:
                print(f'{i:4}', end='')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.new_list)):
            for n_i in range(len(other.new_list[i])):
                self.new_list[i][n_i] = self.new_list[i][n_i] + other.new_list[i][n_i]
        return Matrix.__str__(self)


matrixx = Matrix([[3, 0, 1], [-1, 3, 0], [1, 0, -3]])
matrixx2 = Matrix([[4, 0, 2], [-4, 2, 0], [4, 2, 0]])
print(matrixx.__add__(matrixx2))
