#  File: Spiral.py

#  Description:

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: 02/01/21

#  Date Last Modified: 02/01/21

import sys

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral ( n ):
    # create an empty matrix
    matrix = []
    for row in range(n):
        matrix.append([])
        for col in range(n):
          matrix[row].append([])
    
    zero = 0
    ten = n-1
    
    for i in reversed(range(1, n+1, 2)):
        matrix[zero][ten]= i**2
        number = i**2 - 1

        for j in range(i-1):
            matrix[zero][ten-1-j] = number
            number -= 1
        
        
        for k in range(i-1):
            matrix[zero+1+k][zero] = number
            number -= 1
        
        
        for l in range(i-1):
            matrix[ten][zero+1+l] = number
            number -= 1
        

        for m in range(i-2):
            matrix[ten-1-m][ten] = number
            number -=1
        


        # add to the right of the square until full
            
        zero += 1
        ten -= 1
    return matrix



# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (matrix, n, search):
    # while #something about reading all lines without error:
        # find the index 
        index = []
        for row in range(n):
            for col in range(n):
              #print(matrix[row][col])
              if matrix[row][col] == search:
                  index = [row, col]  
                  #print(index) 
                  break  
              if (search == 0) or (search > n**2):
                  return 0
        # find all directions and add them up
        #print(index)
        row = index[0]
        col = index[1]
        sum = 0

        if row != 0:
            sum += matrix[row-1][col]
            #print(sum)

        if (row != 0) and (col != 0):
            sum += matrix[row-1][col-1]
            #print(sum)

        if (row != 0) and (col != (n-1)):
            sum += matrix[row-1][col+1]
            #print(sum)
        
        if row != (n-1):
            sum += matrix[row+1][col]
            #print(sum)
        
        if (row != (n-1)) and (col != 0):
            sum += matrix[row+1][col-1]
            #print(sum)

        if (row != (n-1)) and (col != (n-1)):
            sum += matrix[row+1][col+1]
            #print(sum)
        
        if col != 0:
          sum += matrix[row][col-1]
          #print(sum)
            
        if col != (n-1):
          sum += matrix[row][col+1]
          #print(sum)
            
        return sum


def main():
  # read the input file
    n = int(sys.stdin.readline())
  # make sure n is even  
    if n % 2 == 0:
        n += 1
    #print(n)

  # create the spiral
    matrix = create_spiral(n)
    #for i in range(n):
      #print(matrix[i])
      #print()
  
  # add the adjacent numbers
    for line in sys.stdin:
        search = int(line)
        sum = sum_adjacent_numbers (matrix, n, search)
        print(sum)


  # print the result

if __name__ == "__main__":
    main()
