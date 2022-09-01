
"""
This is Stack implementation using array based sequences.
"""

###################################################################################################
###################################################################################################

"""
Class Based Stack using array.
"""

# Exception class that inherit original Exception class in Python.
class Empty(Exception):
    pass
    

class Stack:

    def __init__(self):
        self._elements = []
    
    def __len__(self):
        return len(self._elements)

    def is_empty(self):
        return len(self._elements) == 0
    
    def push(self, e):
        self._elements.append(e)

    def top(self):
        if self.is_empty():
            try:
                raise Empty
            except Empty:
                print("Satck is Empty.")
            return None
        else:
            return self._elements[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty.")
        return self._elements.pop()
"""    
s = Stack() 
s.push(10)
print(s.pop())
s.push(20)
s.push(30)
print(s.top())
s.is_empty()
print(len(s))
print(s.pop())
print(len(s))

"""

###################################################################################################
###################################################################################################

""" 
Matching Delimiters Code with Stack.
"""

def is_matched(st):
    left = '({['
    right = ')}]'
    S = Stack()
    for i in st:
        if i in left:
            S.push(i)
        elif i in right:
            if S.is_empty():
                return False
            if right.index(i) != left.index(S.pop()):
                return False
    return S.is_empty()
""" 
print(is_matched('()(()){([()])}'))
 """

###################################################################################################
###################################################################################################
