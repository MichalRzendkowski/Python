class GameOfLife:

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = [[False for i in range(m)] for j in range(n)]

    def setCell(self, x : int, y : int, value: bool):
        self.matrix[x][y] = value

    def getCellState(self, x : int, y : int):
        if x < 0 or x > self.m - 1 or y < 0 or y > self.n - 1: return False
        return self.matrix[x][y]
    
    def getMatrix(self):
        return self.matrix

    def nextState(self):
        nextMatrix = [[False for i in range(self.m)] for i in range(self.n)]
        for i in range(self.m):
            for j in range(self.n):
                neighbours = self.liveNeighbours(i, j)
                if (self.matrix[i][j] and neighbours in [2, 3]) or \
                   (not self.matrix[i][j] and neighbours == 3):
                    nextMatrix[i][j] = True
        self.matrix = nextMatrix

    def liveNeighbours(self, x, y):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if self.getCellState(x + i, y + j) and not i == j == 0:
                    count += 1
        return count

    def printMatrix(self):
        for i in range(self.n):
            print(self.matrix[i])

