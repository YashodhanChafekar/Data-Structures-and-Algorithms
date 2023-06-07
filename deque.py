
"""
This is Double Ended Queue (deque) implementation using array based sequences.
"""

###################################################################################################
###################################################################################################

"""
Class Based Deque using array.
"""

# Exception class that inherit original Exception class in Python.
class Empty(Exception):
    pass


class Deque:

    INITIAL_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Deque.INITIAL_CAPACITY
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
                print("Satck is Empty.")
            return None
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            try:
                raise Empty
            except Empty:
                print("Satck is Empty.")
            return None
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        if self.is_empty():
            try:
                raise Empty
            except Empty:
                print("Satck is Empty.")
            return None
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            try:
                raise Empty
            except Empty:
                print("Satck is Empty.")
            return None
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer
        

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front -1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
    
    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        if self._size == 0:
            self._data[self._front] = e
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e 
        self._size += 1

# Uncomment this code to run Deque.
""" 
D = Deque()
D.add_last(5)
print(f"Queue after Adding 5: {D._data}")
D.add_first(3)
print(f"Queue should now be 3,5: {D._data}")
D.add_first(7)
print(f"Queue should now be 7,3,5: {D._data}")
print(f"Should print 7:  {D.first()}")
D.delete_last()
print(f"Queue should now be 7,3: {D._data}")
print(f"Should print 2:  {len(D)}")
D.delete_first()
print(f"Queue should now be 3: {D._data}")
D.delete_last()
print(f"Queue should now be None: {D._data}")
print(D.is_empty())
D.add_first(8)
D.add_first(6)
print(D.is_empty())
print(D.first())
print(D.last())
print(f"Queue should now be 6,8: {D._data}") 
"""


###################################################################################################
###################################################################################################



