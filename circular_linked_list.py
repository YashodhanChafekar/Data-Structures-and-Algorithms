"""
This is Circular Linked List implementation of Queue.
"""

###################################################################################################
###################################################################################################

"""
Class Based Linked List as a CircularQueue.
"""

# Exception class that inherit original Exception class in Python.
class Empty(Exception):
    pass


class CircularQueue:
    # Private Node Class
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    
    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty(): 
            raise Empty('Queue is Empty.')
        head = self._tail._next
        return head._element
    
    def deque(self):
        if self.is_empty(): 
            raise Empty('Queue is Empty.')
        head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head._next
        self._size -= 1

        return head._element
    
    def queue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            new._next = new
        else:
            new._next = self._tail._next
            self._tail._next = new
        self._tail = new
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

# Uncomment This code to run CircularQueue 

"""
cq = CircularQueue()            
cq.queue(5)         # [5]
cq.queue(8)         # [5,8]
print(cq.first())  # Output: 5
cq.deque()            # [8]
print(cq.first())  # Output: 8
print(cq.is_empty())   # Output: False
"""

###################################################################################################
###################################################################################################

# A Base class for Doubly Linked List.
class _Doubly_Linked:

    class _Node:
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev
        
        def get_node(self):
            if self._prev == None:
                if self._next == None:
                    print(f"None->/{self._element}/->None")
                else:
                    print(f"None->/{self._element}/->{self._next._element}")
            else:
                if self._next == None:
                     print(f"{self._prev._element}->/{self._element}/->None")
                else:
                    print(f"{self._prev._element}->/{self._element}/->{self._next._element}")

    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, pre, post):
        new = self._Node(e, pre, post)
        pre._next = new
        post._prev = new
        self._size += 1
        return new

    def _delete_node(self, e):
        if self._head._next == e:
            self._head._next = e._next
        elif self._tail._prev ==e:
            self._tail._prev = e.prev
        else:
            pre = e._prev
            post = e._next
            pre._next = e._next
            post._prev = e._prev
        self._size -= 1
        ans = e._element
        e._prev = e._next =  e._element = None
        return ans
    
# Linked Double Ended Queue.

class LinkedDeque(_Doubly_Linked):

    def first(self):
        if self.is_empty():
            raise Empty("LinkedDeque is empty.")
        return self._head._next._element
    
    def last(self):
        if self.is_empty():
            raise Empty("LinkedDeque is empty.")
        return self._tail._prev._element
    
    def insert_first(self, e):
        self._insert_between(e, self._head, self._head._next)
    
    def insert_last(self, e):
        self._insert_between(e, self._tail._prev, self._tail)

    def delete_first(self):
        if self.is_empty():
            raise Empty("LinkedDeque is empty.")
        self._delete_node(self._head._next)
    
    def delete_last(self):
        if self.is_empty():
            raise Empty("LinkedDeque is empty.")
        self._delete_node(self._tail._prev)

# Uncomment This code to run LinkedQueue 

"""
ld = LinkedDeque()            
ld.insert_first((5))         # [5]
print(ld.first())  # Output: 5
ld.insert_last(8)            # [8]
print(ld.last())  # Output: 8
ld.delete_first()
print(ld.first()) # Output: 8
print(ld.is_empty())   # Output: False
"""
    
###################################################################################################
###################################################################################################