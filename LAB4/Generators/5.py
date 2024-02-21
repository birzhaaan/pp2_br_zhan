def generate(n):
    for i in range(n,-1,-1):
        yield i
n = int(input("Enter:"))
fum = generate(n)
for num in fum:
    print(num)