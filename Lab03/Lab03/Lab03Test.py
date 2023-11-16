from Lab03 import Stack, StackApp

def useStackApp():

    print("---------------------Call converBase()---------------------")
    sa = StackApp()
    sa.converBase(1026)

    print("---------------------Call checkBrackets()---------------------")
    expr = "mu(ha{m[ad  Ta]r}iq is God!!)"
    print(f"expr : {expr}")
    print(f"Are bracket Balance?: {sa.checkBrakets(expr)}")
    print("---------------------Call infix2Postfix()---------------------")
    expr = "2+(4+3*2+1)/3"
    print(f"expr : {expr}")
    print(f"Postfix Expresion : {sa.infix2Postfix(expr)}")
    print("---------------------Call evalPostfix()---------------------")
    expr = "2432*+1+3/+"
    print(f"expr : {expr}")
    print(f"Postfix Evalutaion = {sa.evalPostfix(expr):0.2f}")
def useStack():
    odd = Stack()
    even = Stack()
    print(f"Even isEmpty? {even.isEmpty()}", end="\t\t\t\t\t\t\t\t | ")
    print(f"Odd isEmpty? {odd.isEmpty()}")
    print(f"Even Stack : {even}", end="\t\t\t\t\t\t\t\t\t | ")
    print(f"Odd Stack : {odd}")
    print(f"Even Size : {even.size()}", end=", ")
    print(f"Len Even : {len(even)}", end="\t\t\t\t\t\t | ")
    print(f"Odd Size : {odd.size()}", end=", ")
    print(f"Len Odd : {len(odd)}")
    print("---------------------------Call push() Function!----------------------------")
    for i in range(20):
        if i % 2 ==0:
            even.push(i)
        else:
            odd.push(i)
    print(even.__iter__())
    print(f"Even Stack : {even}", end=" | ")
    print(f"Odd Stack : {odd}")
    print(f"Even Peek : {even.peek()}", end="\t\t\t\t\t\t\t\t\t | ")
    print(f"Odd Peek : {odd.peek()}")
    print(f"Even Stack {even.__iter__()}", end="\t | ")
    print(f"Odd Stack {odd.__iter__()}")
    print(f"Even Size : {even.size()}", end=", ")
    print(f"Len Even : {len(even)}", end="\t\t\t\t\t | ")
    print(f"Odd Size : {odd.size()}", end=", ")
    print(f"Len Odd : {len(odd)}")
    print("----------------------------Call pop() Function!----------------------------")
    print(f"Even Pop : {even.pop()}", end="\t\t\t\t\t\t\t\t\t | ")
    print(f"Odd Pop : {odd.pop()}")
    print(f"Even Stack : {even}", end=" \t | ")
    print(f"Odd Stack : {odd}")
    print(f"Even Size : {even.size()}", end=", ")
    print(f"Len Even : {len(even)}", end="\t\t\t\t\t\t | ")
    print(f"Odd Size : {odd.size()}", end=", ")
    print(f"Len Odd : {len(odd)}")
    print("---------------------------Call clear() Function!---------------------------")
    even.clear()
    odd.clear()
    print(f"Even Stack : {even}", end="\t\t\t\t\t\t\t\t\t | ")
    print(f"Odd Stack : {odd}")
    print(f"Even Size : {even.size()}", end=", ")
    print(f"Len Even : {len(even)}", end="\t\t\t\t\t\t | ")
    print(f"Odd Size : {odd.size()}", end=", ")
    print(f"Len Odd : {len(odd)}")
def main():
    useStack()
    #useStackApp()

if __name__ == "__main__":
    main()
