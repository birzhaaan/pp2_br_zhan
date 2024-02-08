import math
def obem(rad):
    solution = (4 * math.pi * rad**3)/3
    return solution

a = int(input())
result = obem(a)
print(result)