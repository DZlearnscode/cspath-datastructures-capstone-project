from final_project_node import Node

class LinkedList:
  def __init__(self, value=None):
    self.root = Node(value)
    self.children = {}
  
  def insert(self, food_type, new_value):
    current_node = self.children[food_type]
    next_node = current_node.next_node
    if current_node.value == 0:
      current_node = new_value
    while next_node:
      current_node = current_node.next_node
      next_node = next_node.next_node
    current_node.next_node = new_value
    
    
  def stringify_list(self, food_type):
    data_desc = ["Name", "Price", "Rating", "Addres"]
    current_node = self.children[food_type].next_node
    while current_node:
      print("--------------------------\n")
      for data, desc in zip(current_node.value, data_desc):
        print("{0}: {1}".format(desc, data))
      current_node = current_node.get_next_node() 
    print("--------------------------\n")
      
    
  
  def remove_node(self, value_to_remove):
    current_node = self.root
    if current_node.get_value() == node_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.next_node = next_node.get_next_node()
          current_node = None
        else:
          current_node = next_node
