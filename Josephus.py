#  File: Josephus.py

#  Description: Using circular lists to solve the Josephus problem

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: april 11th

#  Date Last Modified: may 11th

import sys

class Link(object):
  def __init__(self, data, next = None):
    self.data = data
    self.next = next


class CircularList(object):
  # Constructor
  def __init__ ( self ): 
    self.first = None

  # Insert an element (value) in the list
  def insert ( self, data ):
    if self.find(data) != None:
      return

    new = Link(data)
    curr = self.first
    if curr == None:
      self.first = new
      new.next = new
      return

    while curr.next != self.first:
      curr = curr.next

    curr.next = new
    new.next = self.first
    return

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
    curr = self.first
    if curr == None:
      return None
    if curr.data == data:
      return curr
    curr = curr.next
    while curr.data != self.first.data:
      if curr.data == data:
        return curr
      curr = curr.next
    return None

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):
    curr = self.first
    prev = self.first

    if curr == None:
      return None

    while prev.next != self.first:
      prev = prev.next
    
    while curr.data != data:
      prev = curr
      curr = curr.next
    
    if self.first == self.first.next:
      self.first = None
    else:
      self.first = curr.next
    
    prev.next = curr.next

  # Delete the nth Link starting from the Link start 
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
    curr = self.first
    if curr == None:
      return None
    while curr.data != start:
      curr = curr.next

    for i in range(n-1):
      curr = curr.next
    self.delete(curr.data)
    del_data = curr.data
    del_link = curr.next.data
    return [del_data, del_link]

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__ 
  # format for normal Python lists
  def __str__ ( self ):
    curr = self.first

    if curr == None:
      return 'None'

    out = '[' + str(curr.data) + ', '
    curr = curr.next
    while curr.data != self.first.data:
      out += str(curr.data) + ', '
      curr = curr.next
    out += str(curr.data) + ']'
    return out

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)
  
  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # create a circular list to hold the numbers
  game = CircularList()
  for i in range(1, num_soldiers+1):
    game.insert(i)
  
  # loop to eliminate each soldier
  for i in range(num_soldiers):
    result = game.delete_after(start_count, elim_num)
    start_count = result[1]
    print(result[0])
    




if __name__ == "__main__":
  main()