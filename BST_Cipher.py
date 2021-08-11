#  File: BST_Cipher.py

#  Description: Create a simple encryption scheme using a binary search tree

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: thursday april 22nd

#  Date Last Modified: friday april 23rd

import sys

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
      encrypt_str = encrypt_str.lower()
      self.root = None

      for i in encrypt_str:
          if ( 97 <= ord(i) <= 122 ) or ( ord(i) == 32) :
              self.insert(i)


  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    curr = self.root
    parent = None

    while curr != None:
      parent = curr
      if ord(ch) > ord(curr.data):
        curr = curr.rChild
      elif ord(ch) < ord(curr.data):
        curr = curr.lChild
      else:
        return
    
    if parent == None:
      self.root = Node(ch)
    elif ord(ch) > ord(parent.data):
      parent.rChild = Node(ch)
    elif ord(ch) < ord(parent.data):
      parent.lChild = Node(ch)

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    curr = self.root
    code = ""
      
    if curr == None:
      return ""

    if curr.data == ch:
      return "*"

    while curr != None:
      if ord(ch) == ord(curr.data):
        return code
      elif ord(ch) < ord(curr.data):
        code += "<"
        curr = curr.lChild
      elif ord(ch) > ord(curr.data):
        code += ">"
        curr = curr.rChild

    return ""

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    if st == "":
      return ""
    
    curr = self.root
    for char in st:
      if curr == None:
        return ""
      elif char == "*":
        curr = self.root
      elif char == ">":
        curr = curr.rChild
      elif char == "<":
        curr = curr.lChild
    return curr.data if curr != None else ""

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    st = st.lower()
    coded = ""
    
    if st == "":
      return coded
    
    for i in st:
      if ( 97 <= ord(i) <= 122 ) or ord(i) == 32:
        coded += str( self.search(i) ) + "!"
    return coded[:-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    st = st.split("!")
    decoded = ""
    for i in st:
      decoded += self.traverse(i)
    return decoded

def main():
  # read encrypt string
  line = sys.stdin.readline()
  encrypt_str = line.strip()

  # create a Tree object
  the_tree = Tree (encrypt_str)

  # read string to be encrypted
  line = sys.stdin.readline()
  str_to_encode = line.strip()

  # print the encryption
  print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
  line = sys.stdin.readline()
  str_to_decode = line.strip()
  
  # print the decryption
  print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
  main()