

def climbing_stairs(n):

    if n <= 1:
        return 1
    
    return climbing_stairs(n-1) + climbing_stairs(n-2)


print(climbing_stairs(5))
    
    
