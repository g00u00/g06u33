
print("Получение и представление файла:")
str_txt = str()
stream_read = open("../tmp/r_file.txt", mode = 'r', encoding = "utf-8")
str_txt = stream_read.read()
stream_read.close()
print(str_txt)

print("Обработка файла фильтрами:")
str_txt = str_txt.replace("\n","")
str_txt = str_txt.replace(". ",".")
str_txt = str_txt.replace("! ","!")
str_txt = str_txt.replace("? ","?")
print(str_txt)


print("\n\nФормирование и представление предложений:")
sentence = str()
sentences = list()
i = 0
for char in str_txt:
    sentence = sentence.__add__(char)
    if (char  ==  ".") or (char  ==  "!") or (char  ==  "?"):
        print(i,". ", sentence)
        sentences.append(sentence)
        i+=1
        sentence = ""
print("\n\nСписок предложений")
print(sentences)



print("\n\nСписок предложений")
print(sentences)
chars = "Тим"
print("\n\nВведена строка символов: ", chars)
print("Введенные строки содержатся в предложениях:")
for sentence in sentences:
    if (sentence.__contains__(chars)):
        print (sentence) 


print("\n\nСписок предложений")
print(sentences)
letters = ["о", "п", "р"]
print ("\n\nСписок символов:", letters)        
print("Введенные символы будут заменены прописными вначале слова")
for sentence in sentences:
    words = sentence.split()
    for word in words:
        for letter in letters:
            if (word[0] == letter):
                word = word.capitalize()
        print(word," " , end  = '')
    print ("")
print ("\n")    


print("\n\n\nСписок предложений")
print(sentences)
chars = "Python"
print("Введено слово: ", chars)
print("Сколько раз слово встречается в каждом предложении\n")

print("len(sentences):", len(sentences),"\n\n")
for i in range(len(sentences)):
    sentence = sentences[i]
    j = 0
    while sentence.find(chars) != -1:
        print("sentence: ", sentence)
        print("sentence.find(chars):", sentence.find(chars))
        sentence = sentence[sentence.find(chars)+len(chars):len(sentence)]
        j += 1
    print (i, sentences[i]," Слово ",chars,"встречается", j, "раз\n")

    

