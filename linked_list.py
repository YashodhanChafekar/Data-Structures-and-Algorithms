"""
This is Stack and Queue implementation using Linked List.
"""

###################################################################################################
###################################################################################################

"""
Class Based Linked List as a Stack.
"""

# Exception class that inherit original Exception class in Python.
class Empty(Exception):
    pass


class LinkedStack:
    # Private Node Class
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty.')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty.')
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        return ans

# Uncomment This code to run LinkedStack 

"""
ls = LinkedStack()            
ls.push(5)         # [5]
ls.push(8)         # [5,8]
print(ls.top())  # Output: 5
ls.pop()            # [8]
print(ls.top())  # Output: 8
print(ls.is_empty())   # Output: False
"""


###################################################################################################
###################################################################################################

"""
Class Based Linked List as a Queue.
"""

# Exception class that inherit original Exception class in Python.
class Empty(Exception):
    pass


class LinkedQueue:
    # Private Node Class
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty(): 
            raise Empty('Queue is Empty.')
        return self._head._element
    
    def deque(self):
        if self.is_empty(): 
            raise Empty('Queue is Empty.')
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None
        
        return ans
    
    def queue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1

# Uncomment This code to run LinkedQueue 

"""
lq = LinkedQueue()            
lq.queue(5)         # [5]
lq.queue(8)         # [5,8]
print(lq.first())  # Output: 5
lq.deque()            # [8]
print(lq.first())  # Output: 8
print(lq.is_empty())   # Output: False
"""


###################################################################################################
###################################################################################################