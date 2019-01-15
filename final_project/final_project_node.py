class Node:
  def __init__(self, value=None):
    self.word = None 
    self.children = {} 
    self.end_of_word = False
    #linked list functionality
    self.value = value
    self.next_node = None
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
    
  def find_possible(self, possible):
    possible = possible
    for child in self.children.values():
      if child.end_of_word:
        possible.append(child.word)
      if child.children.values():
        child.find_possible(possible)
    return possible
  
  def stringify_list(self):
    string_list = ""
    current_node = self
    while current_node:
      string_list += str(current_node.value) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
    