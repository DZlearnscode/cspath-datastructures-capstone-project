from final_project_node import Node

class Trie:
  def __init__(self):
    self.root = Node()
	#Write Trie Class Here if you choose to implement the Trie
  def add(self, word):
    current_node = self.root
    for char in word:
      if char in current_node.children.keys():
        current_node = current_node.children[char]
      else:
        current_node.children[char] = Node()
        current_node = current_node.children[char]
    current_node.end_of_word = True
    current_node.word = word
    
  def search(self, prefix):
    current_node = self.root
    for char in prefix:
      if char not in current_node.children.keys():
        return False
      if char in current_node.children.keys():
        current_node = current_node.children[char]
    predictive = current_node.find_possible([])
    return predictive
        
  def find_possible(self, possible):
    possible = []
    for child in self.children.values():
      if child.end_of_word:
        possible.append(child.word)
      if child.children.values():
        child.find_possible(possible)
    return possible
  