# 📅 Day 5 — House Robber II + Variants (Sprint Day)

# Today you’ll solve 3 tightly related problems.
# By the end, you’ll own the “conflicting choice” DP pattern.
# 🧩 Problem 1 — House Robber II (Circular Houses)
# 🔹 Problem

# Houses are in a circle:

# First and last houses are adjacent

# Same rule: cannot rob adjacent houses


def house_robber(houses):
    n = len(houses)

    if n == 0:
        return 0
    if n == 1:
        return houses[0]

    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    return dp[-1]


def circular_robber(houses):
    n = len(houses)
    if n == 1:
        return houses[0]

    return max(
        house_robber(houses[:-1]),
        house_robber(houses[1:])
    )



houses = [10,5,20,15,45,10]
print(max(circular_robber(houses[:-1]),circular_robber(houses[1:]))) 