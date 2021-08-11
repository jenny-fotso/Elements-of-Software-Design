#  File: Poly.py

#  Description: represent a polynomial as a Linked List and implement
#                additon and multiplication on those polynomials

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: april 15th

#  Date Last Modified: may 12th

import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    if coeff == 0:
      return None

    new_link = Link(coeff, exp)
    curr = self.first
    prev = self.first
    
    if curr == None or curr.exp < exp:
      new_link.next = self.first
      self.first = new_link
      return

    while curr.next != None:
      if curr.exp <= exp:
        new_link.next = prev.next
        prev.next = new_link
        return
      prev = curr
      curr = curr.next

    if curr.exp < exp:
      new_link.next = prev.next
      prev.next = new_link
    else:
      curr.next = new_link

    return
    

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    adding = LinkedList()
    curr = self.first
    p_curr = p.first

    if curr == None:
      return p
    elif p_curr == None:
      return self

    while True:
      if curr == None and p_curr == None:
        return adding

      if p_curr != None and curr == None:
        exp = p_curr.exp
        coeff = p_curr.coeff
        p_curr = p_curr.next
      
      if curr != None and p_curr == None:
        exp = curr.exp
        coeff = curr.coeff
        curr = curr.next
      
      if p_curr != None and curr != None:
        if curr.exp > p_curr.exp:
          exp = curr.exp
          coeff = curr.coeff
          curr = curr.next
        elif curr.exp < p_curr.exp:
          exp = p_curr.exp
          coeff = p_curr.coeff
          p_curr = p_curr.next
        elif curr.exp == p_curr.exp:
          exp = curr.exp
          coeff = curr.coeff + p_curr.coeff
          curr = curr.next
          p_curr = p_curr.next
          
        
      adding.insert_in_order(coeff, exp)

    
  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    multi = LinkedList()
    curr = self.first

    while curr != None:
      p_node = p.first
      temp = LinkedList()

      while p_node != None:
        multiply = curr.coeff * p_node.coeff
        add = curr.exp + p_node.exp
        temp.insert_in_order( multiply, add )
        p_node = p_node.next
      curr = curr.next
      multi = multi.add(temp)

    return multi
      
  # create a string representation of the polynomial
  def __str__ (self):
    current = self.first
    str = ""
    if current != None:
      str += f"({current.coeff}, {current.exp})"
      current = current.next
    while current != None:
      str += f" + ({current.coeff}, {current.exp})"
      current = current.next
    return str.strip()

def main():
  # read data from file poly.in from stdin
  terms = int(sys.stdin.readline())

  # create polynomial p
  p = LinkedList()
  for i in range(terms):
    coeff, exp = [  int(loop) for loop in sys.stdin.readline().strip().split(" ") ]
    p.insert_in_order(coeff, exp)
  sys.stdin.readline()

  # create polynomial q
  terms = int(sys.stdin.readline())
  q = LinkedList()
  for i in range(terms):
    coeff, exp = [  int(loop) for loop in sys.stdin.readline().strip().split(" ") ]
    q.insert_in_order(coeff, exp)
  sys.stdin.readline()

  # get sum of p and q and print sum
  addList = p.add(q)
  print(addList)

  # get product of p and q and print product
  multList = p.mult(q)
  print(multList)

if __name__ == "__main__":
  main()
