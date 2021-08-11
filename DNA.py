#  File: DNA.py

#  Description: Print out the longest common sequence(s) for the two
# DNA sequence strings. If there is more than one longest common sequence
# then print each of those sequences on separate lines in alphabetical order.

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: 01/25/21

#  Date Last Modified:

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.

import sys

def longest_subsequence (s1, s2):

    #figure out which string is shorter so we don't index out of bounds
    if len(s1) >= len(s2):
        slength = len(s2)
    else:
        slength = len(s1)
    
    #create list to store common sequences
    sequences = []
    x = 0
    y = x + 2

    #slice s1 & find look the slice p in s2
    while x < 3:
        # make sure we're counting right
        print('(x,y) =', x, y)
        slice = s1[x:y]
        print(slice, end=' ')
        #add the common sequence to a list
        if slice in s2:
            sequences.append(s1[x:y])
            y += 1
            print(sequences) 
        else:
            x += 1
            y = x + 2
        
    return sequences

def main():
    # read the data
    n = int(sys.stdin.readline())

    # for each pair
    for i in range(n):
        s1 = sys.stdin.readline().strip().upper()
        s2 = sys.stdin.readline().strip().upper()
        results = longest_subsequence (s1, s2)
        print(results)
    
    # call longest_subsequence

    # write out result(s)

	# insert blank line

if __name__ == "__main__":
  main()