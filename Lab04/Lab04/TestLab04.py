from queueADT import *
from TCS import *
from MediaPlayer import *
from Maze import *

def testCircularDeque():
    print("Deque Test")
    q = CircularDeque()
    for i in range(10):
        q.enqueue(i)
    print("\tenqueue()×9 : ", end="")
    q.print()
    print("\t\tdequeue()-->", q.deleteFront())
    print("\t\tdequeue()-->", q.deleteFront())
    print("\t\tdequeue()-->", q.deleteFront())
    print("\t\tdequeue()-->", q.deleteRear())
    print("\t\tdequeue()-->", q.deleteRear())
    print("\tdequeue()×5", end='')
    q.print()

    q.clear()
    q.enqueue('aaa')
    q.enqueue('bbb')
    q.enqueue('ccc')
    q.enqueue('ddd')
    print('\t\tenqueue()×4: ', end="")
    q.print()
    print("\t\tdequeue()-->", q.deleteRear())
    print("\tdequeue()×9 ", end="")
    q.print()
    print("\t\tpeek()-->", q.peek())
    print("\n")

def testMPQ():
    track1 = Track("white whistle")
    track2 = Track("butter butter")
    track3 = Track("Oh black star")
    track4 = Track("Watch that chicken")
    track5 = Track("Don't go")
    mp = MediaPlayerQueue()
    mp.add_track(track1)
    mp.add_track(track2)
    mp.add_track(track3)
    mp.add_track(track4)
    mp.add_track(track5)
    mp.play()

def runSimulation():
    # done = TicketCounterSimulation(6, 100, 2, 5)
    done = TicketCounterSimulation(2, 100, 2, 8)
    done.run()
def testCircularQueue():

    print('Test Queue')
    q = CircularQueue()
    for i in range(10):
        q.enqueue(i)

    print('\tenqueue()×9: ', end='')
    q.print()
    print('\t\tdequeue()-->',q.dequeue())
    print('\t\tdequeue()-->',q.dequeue())
    print('\t\tdequeue()-->',q.dequeue())
    print('\t\tdequeue()×3',end='')

    q.clear()
    print()
    q.enqueue('aaa')
    q.enqueue('bbb')
    q.enqueue('ccc')
    q.enqueue('ddd')
    print('\tenqueue()×4: ', end='')
    q.print()
    print('\t\tdequeue()-->', q.dequeue())
    print('\tdequeue()×9', end='')
    q.print()
    print("\t\tpeek()-->", q.peek())
    print("\n")

def main():
    #testCircularQueue()
    #testCircularDeque()
    #runSimulation()
    # testMPQ()
    m = Maze()
    m.DFS1()
    m.DFS2()
    m.DFS3()
    m.BFS1()
    m.BFS2()
if __name__ == '__main__':
    main()

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
