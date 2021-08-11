import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval

def merge_tuples(tuples_list):
    tuples_list = sorted(tuples_list)
    copy = tuples_list.copy()
    print(tuples_list)
    merged = []
    i = 0
    while any(copy):
        t1 = tuples_list[i]
        print("t1=", t1)
        x = t1[0]
        y = t1[1]
        for t2 in tuples_list:
            if t1 == t2:
                print("t1 = t2 =", t2)
                i += 1
            elif (( t2[0] >= t1[0] and t2[0] <= t1[1] )
            or  ( t2[1] <= t1[1] and t2[1] >= t1[0] )
            or  ( t2[0] >= t1[0] and t2[1] <= t1[1] )
            or  ( t2[0] <= t1[0] and t2[1] >= t1[1] )):
                print("t2=", t2)
                i += 1
                x = min(t1[0], t2[0])
                y = max(t1[1], t2[1])
                m = tuple([x,y])
                copy.remove(t2)
        merged.append(m)
        copy.remove(t1)
        print("copy:", copy)
        print("merged:", merged)






# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    pass

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert merge_tuples([(1,2)]) == [(1,2)]
  
  # write your own test cases

  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases

  return "all test cases passed"

def main():
    # open file intervals.in and read the data and create a list of tuples
    tuples_list = []
    n = int(sys.stdin.readline())
    for line in sys.stdin:
        strinlist = line.split()
        intinlist = [int(i) for i in strinlist]
        t = tuple(intinlist)
        tuples_list.append(t)
    #print(tuples_list)


    # merge the list of tuples
    merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval

    # run your test cases
    '''
    print (test_cases())
    '''

    # write the output list of tuples from the two functions

if __name__ == "__main__":
    main()
