
def climbStairs(n):
    a, b = 1, 1
    for i in range(n-1):
        temp = a
        a = a + b
        b = temp
    return a

n = 38
print(climbStairs(n))
