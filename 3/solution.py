
############################################################
# Write code in file solution.py 
# Post� solution.py in Canvas along with 4 screen shots that shows Leetcode has passed. We will not use screen shot to give 100
# Cut and paste the whole solution.py file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run solution.py file 4 times in 225, 235,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
         
            
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT

    def is_empty(self) -> bool:
        return self._len == 0
        #return self._first is None or self._last is None
    
    def add_first(self, value):
        new_node = ListNode(val=value)
        if self.is_empty():
            self._first = self._last = new_node
        else:
            new_node.next = self._first
            self._first = new_node
        self._len += 1

    def add_last(self, value):
        new_node = ListNode(val=value)
        if self._last is not None:
            self._last.next = new_node
        self._last = new_node
        if self._first is None:
            self._first = new_node
        self._len += 1
    
    def remove_first(self):
        val = 0
        if self.is_empty():
            raise IndexError("Remove from an empty list")
        elif self._first is not None:
            val = self._first.val
            self._first = self._first.next
            self._len -= 1
        if self._len == 0:
            self._last = None
        return val
    
    def remove_first_queue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self._first.val
        self._first = self._first.next
        self._len -= 1
        if self._first is None:
            self._last = None
        return value

    def peek_first(self):
        if self.is_empty():
            raise IndexError("peek from an empty list")
        return self._first.val
    
    def __len__(self):
        return self._len
    
    
############################################################
#  class  MyStack
#225. Implement Stack using Queues

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()      

    def push(self, x: int) -> None:
        self._s.add_first(x)

    def pop(self) -> int:
        return self._s.remove_first()
        
    def top(self) -> int:
        return self._s.peek_first()

    def empty(self) -> bool:
        return self._s.is_empty()
      


############################################################
#  class  MyQueue
#232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()        

    def push(self, x: int) -> None:
        self._s.add_last(x)

    def pop(self) -> int:
        return self._s.remove_first_queue()

    def peek(self) -> int:
        return self._s.peek_first()

    def empty(self) -> bool:
        return self._s.is_empty()
    




############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

#  The circular queue is a linear data structure in which the operations 
# are performed based on FIFO (First In First Out) principle, and the last
# position is connected back to the first position to make a circle. 
# It is also called "Ring Buffer".

#  One of the benefits of the circular queue is that we can 
# make use of the spaces in front of the queue. In a normal queue, once the queue
# becomes full, we cannot insert the next element even if there is a space 
# in front of the queue. But using the circular queue, we can use the space to store new values.
########################################################### 

class MyCircularQueue:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
 
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            new_node = ListNode(value)
            if self._s._last is None: # empty queue
                self._s._first = new_node
                self._s._last = new_node
                self._s._last.next = self._s._first # keep queue circular

            else:
                new_node.next = self._s._last.next
                self._s._last.next = new_node
                self._s._last = new_node
            self._s._len += 1
            return True


    def deQueue(self) -> bool:
        if self.isEmpty() or self._s._first is None:
            return False
        else:
            result = self._s._first.val
            if self._s._first == self._s._last: # one element
                self._s._first = None
                self._s._last = None
            else:
                self._s._first = self._s._first.next
                self._s._last.next = self._s._first # keep queue circular
            self._s._len -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            if self._s._first is not None:
                return self._s._first.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self._s._last.val

    def isEmpty(self) -> bool:
        return self._s.is_empty()
    
    def isFull(self) -> bool:
        return self._s._len == self._K

    
############################################################
#  MyCircularDeque
#641. Design Circular Deque
#https://leetcode.com/problems/design-circular-deque
# Design your implementation of the circular double-ended queue (deque).

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
 
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            new_node = ListNode(value)
            if self._s._first is None:
                self._s._first = new_node
                self._s._last = new_node
                self._s._last.next = self._s._first
            else:
                new_node.next = self._s._first
                self._s._first = new_node
                self._s._last.next = new_node
            self.increaseLength()
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            new_node = ListNode(value)
            if self._s._last is None:
                self._s._first = self._s._last = new_node
                self._s._last.next = self._s._first
            else:
                new_node.next = self._s._last.next
                self._s._last.next = new_node
                self._s._last = new_node
            self.increaseLength()
            return True
                
    def deleteFront(self) -> bool:
        if self.isEmpty() or self._s._first is None:
            return False
        else:
            if self._s._first == self._s._last:
                self._s._first = None
                self._s._last = None
            else:
                self._s._first = self._s._first.next
                self._s._last.next = self._s._first
            self.decreaseLength()
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty() or self._s._last is None:
            return False
        else:
            if self._s._first == self._s._last:
                self._s._last = self._s._first = None
            else:
                current = self._s._first
                while current.next != self._s._last:
                    current = current.next
                current.next = self._s._first
                self._s._last = current
            self.decreaseLength()
            return True
        
    def increaseLength(self):
        self._s._len += 1

    def decreaseLength(self):
        self._s._len -= 1

    def getFront(self) -> int:
        if self.isEmpty() or self._s._first is None:
            return -1
        else:
            return self._s._first.val

    def getRear(self) -> int:
        if self.isEmpty() or self._s._last is None:
            return -1
        else:
            return self._s._last.val

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return self._s._len == self._K


def main():
    """
    
    myStack = MyCircularDeque(4)
    print(myStack.insertFront(9))
    print(myStack.deleteLast())
    print(myStack.getRear())
    print(myStack.getFront())
    print(myStack.getFront())
    print(myStack.deleteFront()) # error
    print(myStack.insertFront(6))
    print(myStack.insertLast(5))
    print(myStack.insertFront(9))
    print(myStack.getFront())
    print(myStack.insertFront(6))
    """
    
    myStack = MyCircularDeque(2)
    print(myStack.insertFront(7))
    print(myStack.deleteLast())
    print(myStack.getFront())
    print(myStack.insertLast(5))
    print(myStack.insertFront(0))
    print(myStack.getFront())
    print(myStack.getRear())
    print(myStack.getFront())
    print(myStack.getFront())
    print(myStack.getRear())
    print(myStack.insertLast(0))


if __name__ == "__main__":
    main()
    # make some changes
    # make some noises
    # see changes