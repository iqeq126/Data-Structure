from Lab02 import Matrix, EightQueens, TicTacToe
def useMatrix():
    print("Matrix initializer and string __str__")
    print(*Matrix(3, 3, 'r' ).__str__(), sep="\n")
    print("Matrix initializer and representaion __repr__()")
    print(*Matrix(3, 3, 'r').__repr__(), sep="\n")
    print("m1 Matrix")
    m1 = Matrix(5,5, 'r')
    m1.mPrint()
    print("\nm2 Matrix")
    m2 = Matrix(5,5,'r')
    m2.mPrint()
    # print(m1)
    print("\nm1 add m2 Matrix")
    m = m1 + m2 # (m1).__add()__(m2)
    m.mPrint()
    print("\nm1 sub m2 Matrix")
    m = m1 - m2# (m1).__sub()__(m2)
    m.mPrint()
    print("\nm1 mul m2 Matrix")
    m = m1 * m2# (m1).__mul()__(m2)
    m.mPrint()
    print("\nm Transepose")
    print(*m.transpose(), sep="\n")
def useEightQueens():
    e1 = EightQueens()
    e1.runEQ(10)
def useTicTacToe():
    t1 = TicTacToe().play_ttt()

def main():
    #useMatrix()
    #useEightQueens()
    useTicTacToe()
if __name__ == '__main__':
    main()