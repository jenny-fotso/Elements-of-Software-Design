# Input: a is a list of positive integers. 2 < len(a) < 20

# Output: divide the list a into two sub-lists. Get the sum of the two sub-lists. 

# Get the absolute value of the difference between the two sums.

# Return the minimum absolute value difference between the sums of the two sub-lists.

import sys

def even_div (left, right, idx, nums, diff):
  if idx == len(nums):
    diff.append(abs(left-right))

  else:
    return ( even_div(left + nums[idx], right, idx+1, nums, diff)
    or even_div(left, right + nums[idx], idx+1, nums, diff) )
  

def main():
  nums = [4, 9, 1, 5]
  diff = []
  even_div(0, 0, 0, nums, diff)
  print(min(diff))
  


if __name__ == "__main__":
  main()