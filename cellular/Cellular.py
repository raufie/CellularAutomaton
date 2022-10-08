import numpy as np


class Cellular:
    def __init__(self):
        self.binary = str(format(0, "08b"))
        self.res = 100

    def get_rule(self, neighbors, binary):
        #     binary=str(format(30,"08b" ))
        n = "".join([str(n) for n in neighbors])

        for i in range(8):
            s = int(bin(i)[2:])
            if s == int(n):
                return int(binary[7-i])
        return 0

    def get_next_grid(self, grid):

        new_grid = grid[:]
        for i, item in enumerate(grid):
            n = []

            if i == 0:
                n.append(0)
            else:
                n.append(grid[i-1])

    #         sandwitch righht abopve
            n.append(grid[i])

            if i == len(grid) - 1:
                n.append(0)
            else:
                n.append(grid[i+1])

            new_grid[i] = self.get_rule(n, self.binary)
        return new_grid

    def get_image(self):
        img = []
        GRID = np.zeros(self.res*2, dtype=np.int).tolist()
        GRID[self.res] = 1

        for i in range(self.res):
            img.append(GRID)
            GRID = self.get_next_grid(GRID)
        return img
