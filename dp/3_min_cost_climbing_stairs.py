# 🔹 Problem
# You’re given an array cost where:
# cost[i] = cost of stepping on stair i
# You can start from step 0 or step 1
# Each move: climb 1 or 2 steps
# You must reach just beyond the last step (n)
# 👉 Return the minimum cost to reach the top.


def min_cost_climbing_stairs2(n,cost,i):

    if i<=1:
        print(min(n[:2]))
        return min(n[:2])
    
    x = min(min_cost_climbing_stairs2(n,cost+n[i-1],i+1),min_cost_climbing_stairs2(n,cost+n[i-2],i+1)) + 1
    print(x)
    return x


def min_cost_climbing_stairs(c):

    dp = [0]*len(c)
    dp[0] = c[0]
    dp[1] = c[1]

    for i in range(2,len(c)):
        
        dp[i] = min(dp[i-1],dp[i-2]) + c[i]

        print(dp)

    return min(dp[-1],dp[-2])



# c = [1,100,1,1,1]
c =[10,15,20]
print(min_cost_climbing_stairs(c))

