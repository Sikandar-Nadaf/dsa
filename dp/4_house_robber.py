# 🔹 Problem

# You are a robber planning to rob houses along a street.

# Each house has some money

# Adjacent houses cannot be robbed (alarm!)

# You must maximize the total money robbed

# 👉 Return the maximum amount you can rob.


def house_robber(houses):
    n_houses = len(houses)

    if n_houses == 0:
        return 0
    if n_houses == 1:
        return houses[0]
    dp = [0]*n_houses

    dp[0] = houses[0]
    dp[1] = max(houses[0],houses[1])

    for i in range(2,n_houses):

        dp[i] = max(dp[i-2]+houses[i],dp[i-1])

        print(dp)
    return dp[-1]




houses = [10,5,20,15,45,10]
print(house_robber(houses)) ## anser is 45