#  File: FullTree.py

#  Description: Given a binary tree, return True if it's full or False otherwise

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS313E

#  Unique Number: 52235

#  Date Created: may 7th

#  Date Last Modified: may 7th


class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):    
  # the only parameter for the Tree class is self.root, which is a Node object
  # a printlevelorder method has been provided to help with debugging

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
      #print(level)
      return max(self.height_help(node.lchild, level+1), self.height_help(node.rchild, level+1))

  # complete the isFull method below and return a boolean
  def isFull(self):
    #self.printlevelorder()
    # get the heigh of the tree
    h = self.get_height()
    if self.root != None:
      return self.full_help(self.root, h, 0)
    return False
    
  def full_help(self, node, height, level):
    # node has no children
    if (node.lchild == None) and (node.rchild == None):
      return True
    # node only has a left child
    if (node.lchild != None) and (node.rchild == None):
      return False
    # node only has right child
    if (node.lchild == None) and (node.rchild != None):
      return False
    # node has two children
    else:
      level += 1
      return self.full_help(node.lchild, height, level) and self.full_help(node.rchild, height, level)


  # **there is no reason to change anything below this line**
    
  # prints each level in the tree separately
  # a _ character indicates that there is no node there
  def printlevelorder(self):
    def get_height_helper (aNode):
      if aNode == None:
        return 0
      else:
        return max(get_height_helper(aNode.lchild), get_height_helper(aNode.rchild)) + 1

    def printGivenLevel(root, level):
      if level == 1:
        if root is None:
          print('_', end = ' ')
        else:
          print(root.data, end = ' ')
      elif root is None:
        return root
      elif level > 1:
        printGivenLevel(root.lchild, level - 1)
        printGivenLevel(root.rchild, level - 1)

    h = get_height_helper(self.root)
    for i in range(1, h + 1):
        printGivenLevel(self.root, i)
        print()

  # creates a tree from a list input
  def __init__ (self, tree_list):
    if len(tree_list) == 0 or tree_list[0] == None:
      self.root = None
      return
    self.root = Node(tree_list[0])
    node_objs = [None]
    tree_list.insert(0, None)
    node_objs.append(self.root)
    for i in range(2, len(tree_list)):
      if tree_list[i] != None:
        parent_ind = i // 2
        parent_node = node_objs[parent_ind]
        new_node = Node(tree_list[i])
        # for error checking
        if parent_node != None:
          if i == parent_ind * 2:
            parent_node.lchild = new_node
          else:
            parent_node.rchild = new_node
          node_objs.append(new_node)
        else:
          node_objs.append(None)
      else:
        node_objs.append(None)

import sys
def main():
  # create the tree
  tree_list = sys.stdin.readlines()
  for i in range(len(tree_list)):
    tree_list[i] = tree_list[i].strip()
    if tree_list[i] == "None":
      tree_list[i] = None
    
  tree = Tree(tree_list)

  print (tree.isFull())

if __name__ == "__main__":
  main()
