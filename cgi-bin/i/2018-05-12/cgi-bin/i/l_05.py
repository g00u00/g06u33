my_string="слово1 слово2, слово3. Слово4, слово5 слово6?"
print("\n\n Получен текст:") 
print(my_string)

print("\n\n Формируем список разбивкой по пробелам") 
my_list=my_string.split(" ")
print(my_list)

print("\n\n Очищаем список от лишних символов") 
right_words=list()
for word in my_list:
     if (word[-1]=="!") or (word[-1]=="?") or (word[-1]==".") or (word[-1]==","):
         right_words.append(word[0:-1])
     else:  right_words.append(word)
print( right_words)

print('\n\nОкончательные результаты анализа и перестановок')
i=0
for word in right_words:
    if (i.__mod__(2)):
        print(right_words[i-1])
    else:
        print(right_words[i+1])
    i=i+1
