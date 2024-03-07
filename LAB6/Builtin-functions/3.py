stroka = str(input("Enter the string:"))
reversed_stroka = ''.join(reversed(stroka))
if reversed_stroka == stroka:
    print("String is a palindrome")
else:
    print("String isn't palindrome")