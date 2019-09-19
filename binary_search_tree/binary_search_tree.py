import sys
import io
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

#questions:
#Only ints?
#negative numbers
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
    #recursion?
    #edge case? or redundant??
    # if self.value is None:
    #   self.value = value
    #if greater than or equal to root, move right
    if value >= self.value:
      #if there's no node to the right, value becomes the right node
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    #if less than root, move left
    else:
      if value < self.value:
      #if there's no node to the left, value becomes the left node
        if not self.left:
          self.left = BinarySearchTree(value)
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
    #base case, you are the largest
    if not self.right:
      return self.value
    return self.right.get_max()
    
    #iterative instead of recursive
    # max_value = self.value
    # current = self
    # while current:
    #   max_value = current.value
    #   current = current.right
    # return max_value
    
  '''traverses every node in the tree, executing the passed-in callback function on each tree node value. '''
  def for_each(self, cb):
    #recursion ?
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

#DAY 2 Project
  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_dft(self, node):
      pass

  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  '''Breadth first search - queue

  check each level one at a time 
  create a queue
  put root in queue
  while queue is not empty
  pop first item in queue
  check left and right add to queue
  shift 
  go to head of queue and continue '''
  def bft_print(self, node):
      pass

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  '''create a stack
  put root in stack
  while stack is not empty
  pop first item in stack
  check root.left and put it in stack
  check root.right and put it in stack
  go to top of stack and continue'''
  def dft_print(self, node):
      pass








  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
      pass