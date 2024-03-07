stroka = str(input("Enter the string: "))
countofupper = 0
countoflower = 0
for s in stroka:
    if s.islower():
          countoflower+=1
    if s.isupper():
          countofupper+=1


print("Count of uppercase letters:",countofupper)
print("Count of lowercase letters:",countoflower)