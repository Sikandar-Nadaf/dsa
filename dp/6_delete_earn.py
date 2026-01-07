# 🧩 Problem — Delete and Earn
# 🔹 Problem

# You’re given an array nums.

# If you take a number x, you must delete all x-1 and x+1

# You earn x points for each occurrence of x

# Maximize total points


from collections import Counter

def robber(houses):
    n = len(houses)
    if n == 0:
        return 0
    if n == 1:
        return houses[0]
    dp = [0]*n
    dp[0] = houses[0]
    dp[1] = max(houses[0],houses[1])
    for i in range(2,n):
        dp[i] = max(houses[i]+dp[i-2],dp[i-1])

    return dp[-1]

def delete_earn(ls):
    c = Counter(ls)
    ls_c = []
    for i in range(max(c.keys())+1):
        ls_c.append(i*c.get(i,0))

    print(ls)
    print(ls_c)
    return robber(ls_c)



nums = [2,2,3,3,3,4]
print(delete_earn(nums)) ## ans=9