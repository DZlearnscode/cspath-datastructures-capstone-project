from final_project_trie import Trie
from final_project_data import *
from final_project_welcome import *
from final_project_linkedlist import LinkedList
from final_project_node import Node

'''
Which data structure(s) did you use for part 1? Why did you select these data structures?
	
  For part 1 I decied to use Trie Tree data stracture as 		it required less programming and less computation thus 		resulting in a faster more efficient stracture for 				predictive search. A Trie data stracture is a tree 
  stracture associating keys to values where all
  descendants of a node have a common prefix associated
  with that node.
  
  
What is the runtime (in asymptotic notation) of searching for a food type? Do you think there is a more efficient runtime?

	The runtime of the food type search function is O(N).
  The algorithm run time potentially could be constant if
  I have implemented a prefix search option.
  
Which data structures did you use for part 2? Why did you select these data structures?

	For part 2 I used a linked list data stracture with a 
  with a touch of trie tree stracture, giving the heah
  node a children attribute making the runtime of the 
  function constant. I decided to use this combination of
  stracture as linked list makes it a convenient, quick 
  and easy way to traverse through the restaurant data and
  return it with minimal computation. The trie tree 
  stracture touch, adding the children attribute to the 
  head node makes it more efficient to link restaurants 
  to the food type. Linked List is a sequence of data 
  elements which are linked together by each element 
  pointing to the next one in the sequence 
  
What is the runtime (in asymptotic notation) of retrieving the restaurant data? Do you think there is a more efficient runtime?

  The runtime of retrieving the restaurant data is
  constant, thus O(1). I do not think there is a more
  efficient runtime.
  
Outside of this project, what are other innovative ways you can utilize data structures?

	Data structures are used everywhere, from simple 
  computer games to complicated neural networks.
  An innovative way of using data structures would be 
  combining a series of structures to try represent
  and model the way our brains collect, categorise and
  store information. 
  
'''


#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
trie = Trie()
for rest in types:  
  trie.add(rest)  
#Write code to insert restaurant data into a data structure here. The data is in data.py
restaurants = LinkedList()
for t in types:
  restaurants.children[t] = Node()  
for rest in restaurant_data:  
  restaurants.insert(rest[0], Node(rest[1:]),)
#Write code for user interaction here

while True:
  user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n\n")).lower()
  options = trie.search(user_input)

  if not options:
    print("\nSorry couldn't find any food type beginning with '{0}''\n".format(user_input)) 
  
  elif len(options) == 1:
    
    print("\nThe only option with those first letters is {0}. Do you want to look at {0} restaurants? Enter 'y' for yes and 'n for no.'\n".format(options[0]))
    show_restaurants = str(input("\n"))
    if show_restaurants == "y":
      print(restaurants.stringify_list(options[0]))
      other_restaurants = str(input("Do you want to find other restaurants? Enter 'y' for yes and 'n' for no\n\n")).lower()
      if other_restaurants == "n":
        print("Thank you for using Soho Restaurants,\nenjoy your meal.")
        break
  else:  
    print("\nwith those beginning letters, your choices are:\n {0}\n".format(options))
  