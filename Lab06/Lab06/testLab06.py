from binaryNode import binaryNode
from queue import Queue, LifoQueue
from binaryTree import *
from expressionTree import *
from morsecodes import *
from bstTree import *
from wmDictionary import *
from minheap import *
from Huffmancodes import *
def useMorseCodes():
    mc = MorseCodes()
    mc.makeMorseTree()
    mc.printMorseTree()

    bt =binaryTree(mc.root)
    bt.printInorder()
    bt.printPreorder()
    bt.printPostorder()
    bt.printLevelorder()
    print(f"Tree Height : {bt.get_height(bt.getRoot())}")
    print(f"Leaf count : {bt.count_node(bt.getRoot())}")
    print(f"Size of the Tree : {bt.count_node(bt.getRoot())}")


    str01 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    mlist = []
    for ch in str01:
        code = mc.encode(ch)
        mlist.append(code)
    print()
    print("Morse Code : ", mlist)
    print("Decoding : ", end='')
    for code in mlist:
        ch = mc.decode(code)
        print(ch, end='')
    print()
def useET():
    et = ExpressionTree()
    postfix = "359++2*"
    tnode = et.constructTree(postfix)
    print("\nInorder( infix )")
    et.inorder(tnode)
    print("\npreorder( prefix )")
    et.preorder(tnode)
    print("\npostorder( postfix )")
    et.postorder(tnode)

    et2 = ExpressionTree()
    pf2 = "ab+ef*g*-"
    tn = et2.constructTree(pf2)
    print("\nInorder( infix )")
    et2.inorder(tn)
    print("\npreorder( prefix )")
    et2.preorder(tn)
    print("\npostorder( postfix )")
    et2.postorder(tn)
def useBinarySearchTree():
    _tree = BinarySearchTree()
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]

    print("Tree for data " + str(data))
    for i in data:
        _tree.insert_bst(i)
        _tree.printInorder()

    _tree.printPreorder()
    _tree.printPostorder()
    _tree.printLevelorder()
    print(f"Nodes = {_tree.count_node(_tree.root)}")
    print(f"Leaf Nodes = {_tree.count_leaf(_tree.root)}")
    print(f"Height = {_tree.get_height(_tree.root)}")
    print(f"Maximum = {_tree.search_max_bst(_tree.root).data}")
    print(f"Minimum = {_tree.search_min_bst(_tree.root).data}")
    _tree.search_bst(26)
    _tree.search_bst(25)

    _tree.printLevelorder("original LevelOrder: ")
    _tree.delete_bst(3)
    _tree.printLevelorder("     case1 : < 3 >: LevelOrder : ")
    _tree.delete_bst(60)
    _tree.printLevelorder("     case2 : < 60 >: LevelOrder : ")
    _tree.delete_bst(18)
    _tree.printLevelorder("     case3 : < 18 >: LevelOrder : ")
    _tree.delete_bst(35)
    _tree.printLevelorder("     case3 : < 35 >: LevelOrder : ")
    print(f"Nodes = {_tree.count_node(_tree.root)}")
    print(f"Leaf Nodes = {_tree.count_leaf(_tree.root)}")
    print(f"Height = {_tree.get_height(_tree.root)}")
    print(f"Maximum = {_tree.search_max_bst(_tree.root).data}")
    print(f"Minimum = {_tree.search_min_bst(_tree.root).data}")
def useWMDic():
    wmd = Dictionary()
    wmd.runDict()

def useMinHeap():
    print("\nHeap Test")
    _heap = MinHeap()
    data = [2, 5, 4 ,8, 9, 3, 7, 3]
    print("Data elements : " + str(data))
    for e in data:
        _heap.insert(e)
    print(_heap)
    _heap.printHeap()
    _heap.delete()

    print(_heap)
    _heap.printHeap()

    print(_heap)
    _heap.delete()
    _heap.printHeap()

    print(_heap)
    _heap.delete()
    _heap.printHeap()

def useHuffman():
    with open('document1.txt') as txt_file:
        text = txt_file.read()
    # text = "abcdefghijklmnopqrstuvwxyz"
    hc = Huffman(text)
    freq = hc.makeFrequencyDict()
    for key in freq:
        print(f"{key}:{freq[key]}")
    hc.printCodes()
# Press the green button in the gutter to run the script.
def main():
    print("Lab 06")
    #useBST()
    #useBTree()
    # useBinaryNode()
    #useMorseCodes() # 1_morsecode
    # useET()
    #useBinarySearchTree()
    #useWMDic() # 2_BST
    # useMinHeap()
    useHuffman() # 3_HuffmanCode
if __name__ == '__main__':
    main()