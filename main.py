##1) Из строки «Python is the best programming language in the world» получить подстроку начиная с 6 символа
# с начала исходной строки и до 7 символа с конца исходной строки.
str = 'Python is the best programming language in the world'
StrRes = str[5:-7]
print(StrRes)


##2) Вывести каждый третий символа строки «Guido van Rossum is the benevolent dictator for life».
str2 = 'Guido van Rossum is the benevolent dictator for life'
print(str2[2::3])


##3)Из строки «You have a problem with authority, Mr. Anderson.» получить словарь, где ключ -это символ,
# а значение - это количество повторений символа в строке.
str3 = 'You have a problem with authority, Mr. Anderson.'
print(f'Input: {str3}')
a = dict(zip(str3, list(map(lambda x: str3.count(x),str3))))
print(f'Out: {a}')
