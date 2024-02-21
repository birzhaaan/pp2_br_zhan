def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a,b = map(int,input().split())
fum = squares(a,b)
print("All squares of numbers from", a , "to",  b, ":")
for num in fum:
    print(num)