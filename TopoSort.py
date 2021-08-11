#  File: TopoSort.py

#  Description: Add two functions to the graph to perform a
#               topological sort

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: sunday may 2nd

#  Date Last Modified: monday 3rd

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))

  def peek(self):
    return self.queue[0]

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
        # create the Queue
    theQ = Queue()
    # mark the vertex as visited and add to the queue
    (self.Vertices[v]).visited = True
    print(self.Vertices[v])
    theQ.enqueue(v)
    # visit all the other vertices according to depth
    while not theQ.is_empty():
      # get the adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex( theQ.peek() )
      if u == -1:
        u = theQ.dequeue()
      else:
        (self.Vertices[u]).visited = True
        print(self.Vertices[u])
        theQ.enqueue(u)
    # the queue is empty, let us rest the flags
    nVert = len( self.Vertices )
    for i in range(nVert):
      (self.Vertices[i]).visited = False
  
  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    start = self.get_index(fromVertexLabel)
    end = self.get_index(toVertexLabel)
    self.adjMat[start][end] = 0
    self.adjMat[end][start] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
    idx = self.get_index(vertexLabel)
    del self.Vertices[idx]
    del self.adjMat[idx]
    for i in range( len(self.Vertices) ):
      del self.adjMat[i][idx]

  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle (self):
    for v in range( len(self.Vertices) ):
      # create the stack
      theStack = Stack()
      # mark the vertex v as visited and push onto the stack
      (self.Vertices[v]).visited = True
      theStack.push(v)
      # visit all the other vertices accodring to depth
      while not theStack.is_empty():
        # get an adjacent unvisited vertex
        u = self.get_adj_unvisited_vertex(theStack.peek())
        if u == -1:
          u = theStack.pop()
        else:
          (self.Vertices[u]).visited = True
          theStack.push(u)
          # iterate to check if there's a path from u to any vertex in the stack
          for i in range( len(self.Vertices) ):
            if self.adjMat[u][i] != 0 and i in theStack.stack:
              for j in range (len(self.Vertices)):
                self.Vertices[j].visited = False
              return True

      return False

  # return a list of vertices after a topological sort
  # this function should not print the list
  def toposort (self):
    sorts = []

    while len(self.Vertices) != 0:
      level = []
      # check for vertices with a 0 in-degree and add them to a list
      for vertex in self.Vertices:
        idx = self.get_index(vertex.label)
        if self.get_in_degrees(idx) == 0:
          level.append(vertex.label)
      # sort the list of each level alphabetically and add it to the final list
      level.sort()
      sorts.extend(level)
      # delete each level once we're done
      for label in level:
        self.delete_vertex(label)
    
    return sorts
    
  # get the in-degree for a vertex  
  def get_in_degrees (self, v):
    count = 0
    for i in range(len(self.Vertices)):
      if self.adjMat[i][v] > 0:
        count += 1
    return count

def main():
  # create the Graph object
  theGraph = Graph()

  # read the number of vertices
  num_vertices = int( sys.stdin.readline().strip() )
  for i in range(num_vertices):
    theGraph.add_vertex( sys.stdin.readline().strip() )
  
  # read the number of edges
  num_edges = int( sys.stdin.readline().strip() )
  for i in range(num_edges):
    edge = sys.stdin.readline().strip().split()
    start = theGraph.get_index( edge[0] )
    end = theGraph.get_index( edge[1] )
    theGraph.add_directed_edge(start, end)
  
  # test if a directed graph has a cycle
  if (theGraph.has_cycle()):
    print ("The Graph has a cycle.")
  else:
    print ("The Graph does not have a cycle.")

  # test topological sort
  if (not theGraph.has_cycle()):
    vertex_list = theGraph.toposort()
    print ("\nList of vertices after toposort")
    print (vertex_list)


if __name__ == "__main__":
  main()
