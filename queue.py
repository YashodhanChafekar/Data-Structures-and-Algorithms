
"""
This is Queue implementation using array based sequences.
"""

###################################################################################################
###################################################################################################

"""
Class Based Queue using array.
"""

# Exception class that inherit original Exception class in Python.
class Empty(Exception):
    pass


class Queue:

    INITIAL_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Queue.INITIAL_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size 

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            try:
                raise Empty
            except Empty:
                print("Queue is Empty.")
            return None
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            try:
                raise Empty
            except Empty:
                print("Queue is Empty.")
            return None
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

# Uncomment This code to run Queue 

""" 
Q = Queue()            
Q.enqueue(5)         # [5]
Q.enqueue(3)         # [5,3]
print(len(Q))        # Output: 2
print(Q.dequeue())   # Output: 5
print(Q.is_empty())  # Output: False
print(Q.dequeue())   # Output: 3
Q.enqueue(7)         # [7]
print(Q.first())     # Output 7
"""


###################################################################################################
###################################################################################################

