'''Write a program that creates files "A.txt" with "[1]" in it, "B.txt" with [1,2] ... and so on till "Z.txt" with [1,2,3,...25,26] in it'''
for i in range(26):
    file = chr(65+i) + "txt"
    with open()