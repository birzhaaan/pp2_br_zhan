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
'''
l; = [1,2,3,4,5]
jprint("result:", eval('*'.join(str(item) for item in l)))  
                                                                                                                                                       '''
'''import datetime
bugin = datetime.datetime.now()
erten = bugin + datetime.timedelta(days=1)
difference = erten - bugin
new_difference = difference.total_seconds()
print(new_difference)'''

'''import re

# Ваша строка
input_string = input("Введите строку: ")

# Шаблон регулярного выражения
pattern = r'\+7|8-[0-9]{3}-[0-9]{2}-[0-9]{2}'

# Поиск последовательности строчных букв, соединенных подчеркиванием, в строке
matches = re.findall(pattern,input_string)

# Вывод результатов
if matches:
    print("Найденные последовательности:", matches)
else:
    print("Последовательности не найдены.")'''

'''import re

# Ваша строка
input_string = input("Введите строку: ")

# Шаблон регулярного выражения
pattern = r'\+7|8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}'

# Поиск номеров телефонов в строке
matches = re.findall(pattern, input_string)

# Вывод результатов
if matches:
    print("Найденные номера телефонов:", matches)
else:
    print("Номера телефонов не найдены.")
'''

'''import re

word = "roses are red, violets are blue"

print(re.findall("roses|violets", word))'''
'''import re

word = "R0ses are r3d, v1olets are blu3"

print(re.findall("[abc]", word))

print(re.findall("[a-z]", word))

print(re.findall("[a-zA-Z0-9]", word))'''
'''import re

word = r"R0ses are r3d, v1olets are blu3"

pattern = re.compile(r"([a-zA-Z0-9]{2})+")

matches = pattern.finditer(word)

for match in matches:
    print(match.group())'''

'''path = "C:/Users/user/Desktop/pp2/text.txt"
save = ""
with open(path, "r") as f:
    save = f.read()
    
with open(path, "w") as f:
    for i in save:
        f.write(str(ord(i)))'''
'''def replace_text_with_unicode(file_path):
    # Открываем файл для чтения
    with open(file_path, "r") as f:
        # Читаем текст из файла
        text = f.read()
    
    # Создаем пустую строку для сохранения преобразованного текста
    converted_text = ""
    
    # Преобразуем каждый символ в его код Unicode и добавляем к строке converted_text
    for char in text:
        converted_text += str(ord(char))
    
    # Открываем файл для записи и записываем преобразованный текст
    with open(file_path, "w") as f:
        f.write(converted_text)

# Задаем путь к файлу
file_path = "C:/Users/user/Desktop/pp2/text.txt"

# Вызываем функцию replace_text_with_unicode с заданным путем к файлу
replace_text_with_unicode(file_path)
'''
'''for i in range(26): 
    file_name = chr(65 + i) + ".txt"  # Получаем имя файла: A.txt, B.txt, ..., Z.txt 
    with open(file_name, "w") as f: 
        numbers = list(range(1, i + 2))  # Создаем список чисел от 1 до i+1 
        f.write(str(numbers))  # Записываем список в файл как строку'''
'''for i in range(26): 
    file_name = chr(65 + i) + ".txt" 
    with open(file_name, "w") as file: 
        data = [str(j) for j in range(1, i + 2)] 
        file.write("[" + ",".join(data) + "]")'''