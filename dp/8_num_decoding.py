# Day 6 — Decode Ways
# 🔹 Problem

# You’re given a string of digits.

# Mapping:
# '1' -> 'A'
# '2' -> 'B'
# ...
# '26' -> 'Z'
# 👉 Return the number of ways to decode the string.

def num_decodings(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, n + 1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]

        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]

    return dp[n]




nums = "2121"
print(num_decodings(nums))