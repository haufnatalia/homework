"""
    Выполните все пункты.
    * можно описывать вложенные with open(), если это необходимо.
    * работа в основном с одним файлом, поэтому имя можно присвоить переменной
"""

# 1.
# Создайте файл file_practice.txt
# Запишите в него строку 'Starting practice with files'
# Файл должен заканчиваться пустой строкой

file_practice = open('file_practice.txt', 'w')
file_practice.write('Starting practice with files \n')
file_practice.close()

# 2.
# Прочитайте файл, выведете содержимое на экран
# Прочитайте первые 5 символов файла и выведите на экран

file_practice = open('file_practice.txt','r')
print(file_practice.read())

data_1 = file_practice.seek(0)
print(file_practice.read()[:5])
file_practice.close()

# 3.
# Прочтите файл 'files/text.txt'
# В прочитанном тексте заменить все буквы 'i' на 'e', если 'i' большее количество,
# иначе - заменить все буквы 'e' на 'i'
# Полученный текст дописать в файл 'file_practice.txt'

with open('files/text.txt','r') as text:
    i_count = text.read().count('i') 
with open('files/text.txt','r') as text:
    e_count = text.read().count('e')

with open('files/text.txt','r+') as text:
    if i_count > e_count:
        text_2 = text.read().replace('e','i')
        text.seek(0)
        text.write(text_2)
        print(text.read())
    elif i_count < e_count:
        text_2 = text.read().replace('i','e')
        text.seek(0)
        text.write(text_2)

with open('files/text.txt','r')as text, open ('file_practice.txt','a') as file_practice:
    file_practice.write(text.read())


# 4.
# Вставьте строку '*some pasted text*'.
# Если после вставки курсор остановился на четной позиции
#   - добавить в конец файла строку '\nthe end',
# иначе - добавить в конец файла строку '\nbye'
# Прочитать весь файл и вывести содержимое

with open('file_practice.txt','a') as file_practice:
    file_practice.write(input('Enter some text: '))
    if file_practice.tell() % 2 == 0:
        print('\nthe end')
    elif file_practice.tell() % 2 != 0:
        print('\nbye')
