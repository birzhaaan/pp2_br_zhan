def rever(soz):
    return soz[::-1]

a = input()
b = a
answer = rever(a)
if b==answer:
    print("True")
else:
    print("False")