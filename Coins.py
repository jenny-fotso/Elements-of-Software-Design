import sys

'''
Input:  coins is a dictionary representing how many of each type of coin you have (value -> amount)
        amount is the target amount you want to make change for
Output: True if it possible to make exact change using the coins provided, False otherwise
'''

def canMakeChange(coins, amount):
    print(coins)
    keys_list = coins.keys()

def help(nums, target, keys):
    if target == 0:
        return True
    

def main():
    f = sys.stdin
    num_coins, amount = [int(x.strip()) for x in f.readline().split()]
    coins = {}
    for _ in range(num_coins):
        coin_val, coin_amt = [int(x.strip()) for x in f.readline().split()]
        coins[coin_val] = coin_amt
    print(canMakeChange(coins, amount))

if __name__ == "__main__":
    main()