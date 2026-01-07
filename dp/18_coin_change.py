# Coin Change (Minimum Coins)
# You are given:
# a list of coin denominations coins
# a target amount A
# Question:

# What is the minimum number of coins needed to make amount A?
# If it’s not possible, return -1.




def min_coins(coins,target):
    
    n = len(coins)
    dp = [target+1]*(target+1)
    dp[0] = 0

    for c in coins:
        for j in range(1,target+1):
            dp[j] = min(dp[j],dp[j-c]+1)
            print(dp)

    return dp[-1] if dp[-1] != (target+1) else -1

    


coins = [1, 2, 5]
# coins = [2]
A = 11
# A = 3
print(min_coins(coins,A))