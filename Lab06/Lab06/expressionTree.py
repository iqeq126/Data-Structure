from binaryTree import *
from queue import LifoQueue

class ExpressionTree(binaryTree):
    def __init__(self, root=None):
        super().__init__(root=root)

    def isOperator(self, c):
        if c in "+-*/^":
            return True
        else:
            return False

    def constructTree(self, postfix):
        stack = LifoQueue()

        # Traverse through every character of input expression
        for c in postfix:
            # if operand, simply push into stack
            if not self.isOperator(c):
                t = binaryNode(c)
                stack.put(t)
            # Operater
            else:
                # Pop two top nodes
                t = binaryNode(c)
                t1 = stack.get()
                t2 = stack.get()

                # make them children
                t.setRight(t1)
                t.setLeft(t2)

                # Add this subexpression to stack
                stack.put(t)
        # Only element will be the root of expression tree
        et = stack.get()

        return et
