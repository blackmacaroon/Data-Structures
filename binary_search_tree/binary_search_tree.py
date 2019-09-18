import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

#questions:
#Only ints?
#identical numbs?
#>= goes right
#need to traverse to delete
#when deleting the smallest child becomes parent

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  '''adds the input value to the binary search tree, adhering to tree order'''
  def insert(self, value):
    pass
  '''search the tree for input value, return boolean whether it exists or not
  start from root and traverse the tree
  stop at the first instance of a value
  its not found it we get to a node that doesn't have children'''
  def contains(self, target):
    pass
  '''returns the max value in the tree
  for each, count += 1'''
  def get_max(self):
    pass
  '''traverses every node in the tree, executing the passed-in callback function on each tree node value. '''
  def for_each(self, cb):
    pass