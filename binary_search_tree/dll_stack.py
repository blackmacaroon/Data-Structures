import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    # consistance, developer time. why use apples and oranges when apples work for both?
    self.storage = DoublyLinkedList()

  def push(self, value):
    self.storage.add_to_head(value)
    self.size += 1
  
  def pop(self):
    self.size -= 1
    return self.storage.remove_from_head()


  def len(self):
    return self.storage.__len__()