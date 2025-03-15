"""
Stack
    concept ;- LIFO (Last in First out)
    Operations:- push, pop, peek or top, isempty
    algorithm :- hanoi tower

Stack on List
    push - append
    pop - pop
    check stack empty or not
        len(stack==0)
        not stack
    peek or top
        a[-1]

stack on modules
    Collection
    stack= collections.deque()
    operations
        append()
        pop()
        a[-1] for top element
    Queue
    stack=queue.lifoqueue(3) 3 refers
    operations
        put() to append
        get() to remove



"""
from asyncio import timeout


def test_complete_stack_concept_on_list():
        stack=[]
        # n = int(input('enter the limit of the stack'))
        def push():
            if len(stack)==n:
                print('stack is full')
            else:
                x=int(input('enter element to add'))
                stack.append(x)
                print(stack)
        def pop():
            if not stack:
                print('stack is empty')
            else:
                print('removed element is ',stack.pop())
                print(stack)
        n=int(input('enter the limit of stack'))
        while True:
            # print('Stack is ready for operation')
            choice=int(input('enter your choice 1. push 2.pop 3. stop'))
            if choice==1:
                push()
            elif choice ==2:
                pop()
            elif choice == 3:
                break
# ............................. collecton module ........................

def test_stack_on_module_collections():
    import collections
    stack=collections.deque()
    stack.append(10)
    stack.append(12)
    stack.pop()
    stack.pop()
    print(stack)

#................... QUEUE module .......................................

def test_queue_module_on_stack():
    import queue
    stack=queue.LifoQueue(3) # 3 means size of stack
    stack.put(10)
    stack.put(11)
    stack.put(12)
    stack.put(14,timeout=3) # useful when try to insert in fixed size stack
    print(stack)
    print(stack.get())
    print(stack.get())
    print(stack.get())
    print(stack.get(timeout=3)) # userful when try to pop the empty stack


def test_stack_on_list():
    a='he is a python programmer and learns dsa from amulya acaddemy channel'
    a1=[1,2,3,4,5,6]
    b=[a1.pop(),]
    print(b)

def test_reverse_string():
    a = 'bala'
    b = list(a)
    c = []
    for x in range(len(b)):
        c.append(b.pop())
    print(''.join(c))

def test_reverse_array():
    a = [10, 11, 12, 13, 14]
    b = [a.pop(), a.pop(), a.pop(), a.pop()]
    print(b)

