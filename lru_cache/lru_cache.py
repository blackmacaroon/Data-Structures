import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.max_nodes = limit
    self.node_count = 0
    # self.current_node = None
    self.cache = DoublyLinkedList()
    self.storage = dict()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  # def get(self, key):
  #   #takes in the key
  #   #edge cases, no nodes or no key
  #   if self.node_count == 0 or key not in self.storage:
  #     return None
  #   #if key, set to current node, else return None
  #   elif key in self.storage:
  #     #capture node value
  #     current_node = self.storage[key]
  #     #delete old node
  #     self.cache.delete(current_node)
  #     #move key-value pair to the head aka "most recently used"
  #     self.cache.add_to_head([key, current_node])
  #     #return the value
  #     return current_node
  def get(self, key):
    #pull the calue out of the dict using the key
    if key in self.storage:
      node = self.storage[key]
      self.cache.move_to_front(node)
      # 1 is the value in the array [key, value] 0 would be key
      return node.value[1]
    else:
      return None
    


  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  # def set(self, key, value):
  #   #if key exists in cache already, overwrite it
  #   if key in self.cache:
  #     current_node = self.cache[key]
  #     #delete old node
  #     self.storage.delete(current_node)
  #     #move key-value pair to the head aka "most recently used"
  #     self.storage.add_to_head([key, value])
  #     #set key in cache to new value from storage
  #     self.cache[key] = [value, self.storage.head]
  #     return

  #   #else if cache is full, remove last item and add new item to head
  #   if self.max_nodes is self.node_count:
  #     #delete tail node
  #     current_node = self.storage.tail
  #     self.storage.remove_from_tail()
  #     #
  #   #else just add it to the head in storage
  #   self.storage.add_to_head([key, value])
  #   #add new key, value to the cache
  #   self.cache[key] = [value, self.storage.head]
  #   self.node_count += 1

  def set(self, key, value):
    #if key exists in cache already, overwrite it
    if key in self.cache:
      #update dictionary
      node = self.cache[key]
      node.value = [key, value]
      # mark as most recently used, put it in the head
      self.cache.move_to_front(node)
      return

    #else if cache is full, remove last item and add new item to head
    if self.node_count is self.max_nodes:
      #delete tail node
      del self.storage[self.cache.tail.value[0]]
      self.cache.remove_from_tail()
      self.node_count -= 1
    #else just add it to the head in storage
    self.cache.add_to_head([key, value])
    #add new key, value to the cache
    self.storage[key] = self.cache.head
    self.node_count += 1


