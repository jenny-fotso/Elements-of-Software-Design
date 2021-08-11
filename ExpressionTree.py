#  File: ExpressionTree.py

#  Description: Evaluate an expression and print its result, 
#               pre-fix and post-fix versions of the expression.

#  Student's Name: Jenny Fotso

#  Student's UT EID:   

#  Course Name: CS 313E 

#  Unique Number: 52235

#  Date Created: 18th april

#  Date Last Modified: may 12th

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        operators = ['+', '-', '*', '/', '//', '%', '**']
        expr = expr.split()
        the_stack = Stack()
        self.root = Node()
        curr = self.root
        
        for i in expr:
            if i == "(":
                curr.lChild = Node()
                the_stack.push(curr)
                curr = curr.lChild
            elif i in operators:
                curr.data = i
                the_stack.push(curr)
                curr.rChild = Node()
                curr = curr.rChild
            elif i.isdigit( ) or "." in i:
                i = i.strip()
                # consider floats
                if "." in i:
                    curr.data = float(i)
                else:
                    curr.data = int(i)
                curr = the_stack.pop()

                curr.rChild = Node()
                curr = curr.rChild
            elif i == ")":
                if not the_stack.is_empty():
                    curr = the_stack.pop()
                else:
                    break
        
        return expr

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode.data == "+":
            return float( self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild) )
        elif aNode.data == "-":
            return float( self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild) )
        elif aNode.data == "*":
            return float( self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild) )
        elif aNode.data == "/":
            return float( self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild) )
        elif aNode.data == "//":
            return float( self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild) )
        elif aNode.data == "%":
            return float( self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild) )
        elif aNode.data == "**":
            return float( self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild) )
        elif aNode.data.isdigit() or "." in aNode.data:
            return eval(aNode.data) * 1.0
    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        return self.pre_help(aNode)

    def pre_help (self, aNode):
        if aNode is not None:
            return str(aNode.data) + " " + self.pre_help(aNode.lChild) + self.pre_help(aNode.rChild)
        else:
            return ""
        
    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        return self.post_help(aNode)
    
    def post_help (self, aNode):
        if aNode is not None:
            return self.post_help(aNode.lChild) + self.post_help(aNode.rChild) + " " + str(aNode.data)
        else:
            return ""

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()