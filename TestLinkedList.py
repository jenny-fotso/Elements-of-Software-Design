#  File: TestLinkedList.py

#  Description: helper methods for the LinkedList class

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: Friday April 9th

#  Date Last Modified: Saturday May 1st

import random

class Link (object):
  def __init__ (self, data, next = None ):
      self.data = data
      self.next = next


class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.first = None

  # get number of links 
  def get_num_links (self):
    count = 0
    curr = self.first
    while curr != None:
      count += 1
      curr = curr.next
    return count
  
  # add an item at the beginning of the list
  def insert_first (self, data): 
    new_link = Link(data)
    new_link.next = self.first
    self.first = new_link
    return

  # add an item at the end of a list
  def insert_last (self, data): 
    new_link = Link(data)
    curr = self.first
    if curr == None:
      self.first = new_link
      return
    while curr.next != None:
        curr = curr.next
    curr.next = new_link

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 
    curr = self.first
    if curr == None:
      self.first = Link(data)
      return
    
    if curr.data >= data:
      self.insert_first(data)

    while curr.next != None:
      if curr.next.data >= data:
        new_link = Link(data)
        new_link.next = curr.next
        curr.next = new_link
        return
      else:
        curr = curr.next
    curr.next = Link(data)
    return

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
    curr = self.first
    if curr == None:
      return None

    while curr != None :
      if curr.data == data:
        return curr
      else:
        curr = curr.next

    return None

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    curr = self.first
    if curr == None:
      return None

    while curr.next != None:
      if curr.data == data:
        return curr
      elif curr.next.data > data:
          return None
      else:
        curr = curr.next

    return None

  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):
    curr = self.first
    if curr == None:
      return None
    
    if curr.data == data:
      temp = Link(curr.data)
      curr.next = curr.next.next
      return temp

    while curr.next != None:
      if curr.next.data == data:
        temp = Link(curr.next.data)
        curr.next = curr.next.next
        return temp
      else:
        curr = curr.next
    
    return None

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    curr = self.first
    string = ""
    count = 0
    if curr == None:
      return ""

    while curr != None:
      string += str(curr.data) + '  '
      curr = curr.next
      count += 1
      if count % 10 == 0:
        string += "\n"
    return string

  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
    new_list = LinkedList()
    curr = self.first
    new_list.first = self.first

    if curr == None:
      return new_list
    
    newcurr = new_list.first
    curr = curr.next
    while curr!= None:
      newcurr.next = Link(curr.data)
      curr = curr.next
      newcurr = newcurr.next
    return new_list

  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self): 
    new_list = LinkedList()
    curr = self.first
    while curr != None:
      new_list.insert_first(curr.data)
      curr = curr.next
    return new_list

  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 
    new_list = LinkedList()
    curr = self.first
    if curr == None:
      return self
    while curr != None:
      new_list.insert_in_order(curr.data)
      curr = curr.next
    return new_list

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    curr = self.first
    if curr == None or curr.next == None:
      return True

    while curr.next != None:
      if curr.next.data < curr.data:
        return False
      curr = curr.next
    return True

  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    return self.first == None

  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
    new_list = LinkedList()
    selfcurr = self.first
    othercurr = other.first
    while selfcurr != None:
      new_list.insert_in_order(selfcurr.data)
      selfcurr = selfcurr.next
    while othercurr != None:
      new_list.insert_in_order(othercurr.data)
      othercurr = othercurr.next
    return new_list

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    selfcurr = self.first
    othercurr = other.first

    if selfcurr == None and othercurr == None:
      return True

    while selfcurr.next != None and othercurr.next != None:
      if selfcurr.data != othercurr.data:
        return False
      else:
        selfcurr = selfcurr.next
        othercurr = othercurr.next
    return selfcurr == None and othercurr == None

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
    new_list = LinkedList()
    dupes = []
    curr = self.first
    if curr == None:
      return new_list

    while curr.next != None:
      if curr.data not in dupes:
        dupes.append(curr.data)
        new_list.insert_last(curr.data)
      curr = curr.next
    return new_list
      
def main():
  test = LinkedList()

  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  for i in range(6):
    test.insert_first(i)
  print(test)
  print()

  # Test method insert_last()
  test.insert_last(6)
  print(test)
  print()

  # Test method insert_in_order()
  #for i in range(6):
    #test.insert_in_order(i)
  #print(test)
  #print()

  # Test method get_num_links()
  print( test.get_num_links() )

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 
  print( test.find_unordered(2) )
  print( test.find_unordered(7) )

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 
  #print( test.find_ordered(2) )
  #print( test.find_ordered(7) )

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  print( test.delete_link(0) )
  print( test.delete_link(7) )
  print(test)

  # Test method copy_list()
  #print( test.copy_list() )

  # Test method reverse_list()
  #print( test.reverse_list() )

  # Test method sort_list()
  print( test.sort_list() )

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print( test.is_sorted() )
  print( test.sort_list().is_sorted() )

  # Test method is_empty()
  print( test.is_empty() )

  # Test method merge_list()
  print( test.merge_list(test.reverse_list()) )

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  #print( test.is_equal( test ) )
  #print( test.is_equal( test.reverse_list() ) )

  # Test remove_duplicates()
  print( test.merge_list(test.reverse_list()).remove_duplicates() )

if __name__ == "__main__":
  main()