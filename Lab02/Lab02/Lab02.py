import random
class Matrix:
    rnb = random.Random()
    def __init__(self, rows, cols, f='r'):
        self.M = []
        if f == 'r':
            self.rMatrix(rows, cols)
        else :
            self.zMatrix(rows, cols)


    def rMatrix(self, rows, cols):
        while len(self.M) < rows:
            self.M.append([])
            while len(self.M[-1]) < cols:
                self.M[-1].append(Matrix.rnb.randint(1, 10))

    def zMatrix(self, rows, cols):
        while len(self.M) < rows:
            self.M.append([])
            while len(self.M[-1]) < cols:
                self.M[-1].append(0)

    def mPrint(self):
        for rows in self.M:
            print([x for x in rows])

    def __str__(self):
        return self.M

    def __repr__(self):
        print("Mymatrix is that")
        return self.M

    def __add__(self, other):
        rowsA = len(self.M)
        colsA = len(self.M[0])
        C = Matrix(rowsA, colsA, 'z')

        for row in range(rowsA):
            for col in range(colsA):
                C.M[row][col] = self.M[row][col] + other.M[row][col]
        print("add two Matrix!")
        return C
    def __sub__(self, other):
        rowsA = len(self.M)
        colsA = len(self.M[0])
        C = Matrix(rowsA, colsA, 'z')

        for row in range(rowsA):
            for col in range(colsA):
                C.M[row][col] = self.M[row][col] - other.M[row][col]
        print("sub two Matrix!")
        return C

    def __mul__(self, other):
        rowsA = len(self.M)
        colsA = len(self.M[0])
        C = Matrix(rowsA, colsA, 'z')

        for X in range(rowsA):
            for Y in range(colsA):
                for Z in range(rowsA):
                    C.M[X][Y] = self.M[X][Z] * other.M[Z][Y]
        print("mul two Matrix!")
        return C


    def transpose(self):
        rowsA = len(self.M)
        colsA = len(self.M[0])
        T = [[0 for _ in range(rowsA)] for _ in range(colsA)]

        for X in range(rowsA):
            for Y in range(colsA):
               T[Y][X] = self.M[X][Y]
        return T
class EightQueens:
    rnb = random.Random()
    def __init__(self):
        self.bd = list(range(8))
    def runEQ(self, nos):
        found = 0
        tries = 0
        while found<nos:
            while found < nos:
                EightQueens.rnb.shuffle(self.bd)
                if not self.has_clashes():
                    found +=1
                    print(f"solution {found}. {self.bd}, {tries}")
                tries+=1
    def has_clashes(self):
        for col in range(1, len(self.bd)):
            if self.col_clashes(col):
                return True
            else:
                return False
    def col_clashes(self, k):
        for i in range(k):
            if self.dclashes(i, self.bd[i], k, self.bd[k]):
                return True
        return False

    def dclashes(self,x0, y0, x1, y1):
        d1 = abs(x0-y0)
        d2 = abs(x1-y1)
        return d1 == d2

class TicTacToe:
    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append('-')

    def play_ttt(self):
        win = False
        move = 0
        while not win:
            self.printBound()
            if move % 2 == 0:
                turn = 'X'
            else:
                turn = 'O'
            print(f"Turn for player '{turn}'")

            user = self.getInput(turn)
            while self.board[user] != '-':
                print("Invalid Input!")
                user = self.getInput(turn)

            self.board[user] = 'O' if turn == 'O' else 'X'
            move +=1
            if move > 3:
                winner = self.check_win()
                if winner:
                    print(f"winner is '{'X' if winner == 'X' else 'O'}'👏👏👏")
                    win = True
            if self.quit_game():
                break
        self.printBound()
        if win:
            print(f"Retry?(Y or n)")
            self.re_game()
        else:
            print(f"Oh~ Draw~!\nRetry?(Y or n)")
            self.re_game()

    def getInput(self, turn):
        n = int(input(f"{turn}'s turn! Input Your Number"))
        return n

    def check_win(self):
        win_cord = ((1,2,3), (4,5,6),(7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7) )
        for each in win_cord:
            if self.board[each[0]-1] == self.board[each[1]-1] == self.board[each[2]-1] and self.board[each[0]-1] != '-':
                return self.board[each[0]-1]
        return False

    def printBound(self):
        print(self.board[:3], self.board[3:6], self.board[6:], sep="\n")

    def quit_game(self):
        return '-' not in self.board
    def re_game(self):
        while True:
            n = input()
            if n == 'Y':
                print("Okay! retry~!!")
                for i in range(9):
                    self.board[i]='-'
                self.play_ttt()
                break
            if n =='n':
                print("Okay! See You Later~!!")
                break
            print("Your input is wrong!!\nRetry?(Y or n)")