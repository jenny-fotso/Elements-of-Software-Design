#  File: TestBinaryTree.py

#  Description: Adding methods to the Tree class and testing them

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: Sunday 25th

#  Date Last Modified: Monday 26th

import sys

class Node (object):
  def __init__ (self, data):
      self.data = data
      self.lchild = None
      self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node
    
    #print("insert:", self.root.lChild)

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    if pNode == None:
      return False
    if self.root == None and pNode.root == None:
      return True

    return self.similar_help(self.root, pNode.root)

  def similar_help(self, nodeA, nodeB):
    if nodeA != None and nodeB != None:
      if nodeA.data == nodeB.data:
        return self.similar_help(nodeA.lchild, nodeB.lchild) and self.similar_help(nodeA.rchild, nodeB.rchild)
      else:
        return False
    else:
      return nodeA == nodeB

  # Returns a list of nodes at a given level from left to right
  def get_level (self, level): 
    if self.root == None:
      return []
    elif level == 0:
      return [self.root]
    else:
      nodes = []
      self.level_help(self.root, level, nodes)
      return nodes

  def level_help(self, node, level, list):
    if node != None:
      if level == 0:
        list.append(node)
      else:
        self.level_help(node.lchild, level-1, list)
        self.level_help(node.rchild, level-1, list)

  # Returns the height of the tree
  def get_height (self): 
    if self.root == None:
      return 0
    if self.root.rchild == None and self.root.lchild == None:
      return 1
    else:
      return self.height_help(self.root, 1)
  
  def height_help(self, node, level):
    if node == None:
      return level-1
    else:
      print(level)
      return max(self.height_help(node.lchild, level+1), self.height_help(node.rchild, level+1))

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    return self.nodes_help(self.root)

  def nodes_help(self, node):
    if node == None:
      return 0
    else:
      left = self.nodes_help(node.lchild)
      right = self.nodes_help(node.rchild)
      return 1 + left + right

def main():
  # Create three trees - two are the same and the third is different
	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree1_input = list (map (int, line)) 	# converts elements into ints
	tree1 = Tree()
	for i in tree1_input:
		tree1.insert(i)

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree2_input = list (map (int, line)) 	# converts elements into ints
	tree2 = Tree()
	for i in tree2_input:
		tree2.insert(i)

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree3_input = list (map (int, line)) 	# converts elements into ints
	tree3 = Tree()
	for i in tree3_input:
		tree3.insert(i)

  # Test your method is_similar()
	print( tree1.is_similar(tree2) )
	print( tree1.is_similar(tree3) )

	print( tree2.is_similar(tree1) )
	print( tree2.is_similar(tree3) )

	print( tree3.is_similar(tree1) )
	print( tree3.is_similar(tree2) )

  # Print the various levels of two of the trees that are different
	print( tree2.get_level(3) )
	print( tree3.get_level(3) )

	print( tree2.get_level(1) )
	print( tree1.get_level(1) )

  # Get the height of the two trees that are different
	print( tree1.get_height() )
	print( tree3.get_height() )

  # Get the total number of nodes a binary search tree
	print( tree1.num_nodes() )
	print( tree2.num_nodes() )
	print( tree3.num_nodes() )

if __name__ == "__main__":
  main()