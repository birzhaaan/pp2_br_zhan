'''import re

input_string = input("Введите строку: ")
pattern = r'^a*b*$'

if re.match(pattern, input_string):
    print("Строка соответствует условию.")
else:
    print("Строка не соответствует условию.")'''
'''import re

input_string = input("Введите строку: ")
pattern = r'^[A-Z]$'

if re.match(pattern, input_string):
    print("Строка соответствует условию.")
else:
    print("Строка не соответствует условию.")
'''
'''import re

input_string = input("Введите строку: ")
pattern = r'[a-z]+_[a-z]+'
matches = re.findall(pattern, input_string)

if matches:
    print("Найденные последовательности:")
    for seq in matches:
        print(seq)
else:
    print("В строке нет последовательностей строчных букв, соединенных подчеркиванием.")'''
'''import re

input_string = input("Введите строку: ")
pattern = r'^a.*b$'
matches = re.findall(pattern, input_string)

if matches:
    print("Строка соответствует условию.")
else:
    print("Строка не соответствует условию.")'''
'''import re

input_string = input("text:")
pattern = r'[ ]'

result = re.sub(pattern,':',input_string)
print(result)'''
'''import re

input_string = input("Введите строку: ")
pattern = r'.*[A-Z][a-zA-Z][A-Z]'
matches = re.sub(pattern,' ',input_string)

if matches:
    print("Найденные последовательности:")
    for seq in matches:
        print(seq)
else:
    print("В строке нет последовательностей строчных букв, соединенных подчеркиванием.")'''