class Matrix:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(self.list_1)):
            for k in range(len(self.list_2)):
                self.matrix[i][k] = self.list_1[i][k] + self.list_2[i][k]
        return self.matrix

    def __str__(self):
        out = ""
        for matrix in self.matrix:
            for m in matrix:
                out += f"{m} "
            out += "\n"
        return out


m = Matrix([[20, 3, 5], [2, 5, 2], [6, 10, 1]], [
    [5, 7, 8], [2, 3, 9], [11, 21, 31]])
print(m.__add__())
print(m)
