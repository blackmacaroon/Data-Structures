# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

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

    #if greater than root, move right
    #if less than root, move left
    #recursion?
    if value >= self.value:
      #if there's no node to the right, value becomes the right node
      if not self.right:
        self.right = value
      else:
        self.right.insert(value)
    if value < self.value:
      #if there's no node to the left, value becomes the left node
      if not self.left:
        self.left = value
      else:
        self.left.insert(value)
    
  '''search the tree for input value, return boolean whether it exists or not
  start from root and traverse the tree
  stop at the first instance of a value
  its not found it we get to a node that doesn't have children'''
  def contains(self, target):
    #if target = node value, return true
    if self.value is target:
      return True
    #edge cases, no kiddos
    elif not self.right and not self.left:
      return False
    #else if target > node, go right, recursively calling contains
    elif target >= self.value:
      return self.right.contains(target)
    #else if target < node, go left, recursively calling contains
    else:
      return self.left.contains(target)
    #anything else?
  '''returns the max value in the tree
  '''
  def get_max(self):
    #hard right til no child = largest 
    if self.right:
      return self.right.get_max()
    #edge case, you are the largest
    else:
      return self.value
    
  '''traverses every node in the tree, executing the passed-in callback function on each tree node value. '''
  def for_each(self, cb):
    #recursion ?
    pass