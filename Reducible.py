#  File: Reducible.py

#  Description: Returns the longest reducible word given a file of words.

#  Student Name: Jenny Fotso

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: Sunday April 4th

#  Date Last Modified: Monday April 26th

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  key = hash_word(s, const)
  return const - (key % const)

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  n = len(hash_table)
  idx = hash_word(s, n)
  step = step_size(s, 13)
  i = 1

  if hash_table[idx] == "":
    hash_table[idx] = s
  else:
    while hash_table[ ( idx + step * i ) % n ] != "":
      i += 1
    hash_table[ ( idx + step * i ) % n ] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  n = len(hash_table)
  idx = hash_word(s, n)
  step = step_size(s, 13)
  i = 1

  if hash_table[idx] == s:
    return True
  elif hash_table[idx] != "":
    while hash_table[(idx + step * i) % n] != "":
      if hash_table[(idx + step * i) % n] == s:
        return True
      i += 1
  return False 

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if len(s) == 1:
    return s == "a" or s == "i" or s == "o"
  if find_word(s, hash_memo):
    return True
  
  for i in range( len(s) )  :
    string = s[:i] + s[i+1:]
    if len(string) > 1:
      if find_word(string, hash_table) and is_reducible(string, hash_table, hash_memo):
        insert_word(s, hash_memo)
        return True
    else:
      if is_reducible(string, hash_table, hash_memo):
        insert_word(s, hash_memo)
        return True

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  longest_w = ""
  longest_list = []

  for i in string_list:
    if len(i) > len(longest_w):
      longest_w = i
      longest_list = []
      longest_list.append(i)
    elif len(i) == len(longest_w):
      longest_list.append(i)
  return longest_list

def main():
  # create an empty word_list
  word_list = []

  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  # find length of word_list
  n = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  N = 2 * n
  while not is_prime(N):
    N += 1

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  hash_list = [ "" for i in range(N) ]

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list:
    insert_word(word, hash_list)

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  hash_memo = []
  M = int( 0.2 * len(word_list) ) + 1
  while not is_prime(M):
    M += 1

  # populate the hash_memo with M blank strings
  hash_memo = [ "" for i in range(M) ]

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for word in word_list:
    if is_reducible(word, hash_list, hash_memo):
      reducible_words.append(word)

  # find the largest reducible words in reducible_words
  reducible_words = get_longest_words(reducible_words)

  # print the reducible words in alphabetical order
  # one word per line
  reducible_words = sorted(reducible_words)
  for word in reducible_words:
    print(word)

if __name__ == "__main__":
  main()

