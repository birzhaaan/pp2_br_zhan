def solve(numheads, numlegs):
    rabbits = (numlegs - numheads*2)/2
    chickens = numheads - rabbits
    return rabbits,chickens

numheads, numlegs = map(int,input().split())
if numheads>numlegs:
    print("No solution")
elif numheads==numlegs:
    print("rabbits: ", numheads)
    print("chickens: ", 0)
else:
    a,b = solve(numheads, numlegs)
    if solve:
        print("rabbits: ", a)
        print("chickens: ", b)