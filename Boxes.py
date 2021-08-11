
#  File: Boxes.py

#  Description: Return the largest number of boxes that can fit inside 
#               each other and the number of such sets of boxes that do
#               fit, given a list of dimensions for said boxes.

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: 03/24

#  Date Last Modified: 03/25

import sys

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  if idx >= len(box_list):
    all_box_subsets.append(sub_set)

  else:
    copy = sub_set[:]
    sub_set.append(box_list[idx])
    sub_sets_boxes(box_list, sub_set, idx+1, all_box_subsets)
    sub_sets_boxes(box_list, copy, idx+1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets):
  # determining whether the subset is nesting and appending those
  # nesting subsets to a new empty list 
  nesting = []
  for subset in all_box_subsets:
    if len(subset) <= 1:
      pass
    else:
      i = 0
      while ( i <= len(subset)-2 ) and does_fit(subset[i], subset[i+1]) :
        i += 1
      if i == (len(subset)-1):
        nesting.append(subset)
  
  # determining the largest nesting subset length and appending those
  # that have that max length to a new list which is then returned
  max_length = max(len(subset) for subset in nesting)
  other = []
  for subset in nesting:
    if len(subset) == max_length:
      other.append(subset)
  return other
   

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  # print (box_list)
  # print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  # for i in box_list:
  #   print(i)
  # print()
  
  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes
  #print(len(all_box_subsets) == 2**num_boxes)

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = largest_nesting_subsets (all_box_subsets)

  # print the largest number of boxes that fit
  print(len(all_nesting_boxes[0]))

  # print the number of sets of such boxes
  print(len(all_nesting_boxes))

if __name__ == "__main__":
  main()

