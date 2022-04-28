#ввод текста
str_txt=str()
stream_read=open("../tmp/pavl_02.txt", mode='r', encoding="utf-8")
str_txt=stream_read.read()
stream_read.close()
print("Исходный файл")
print(str_txt)

#начальная фильтраця
str_txt=str_txt.replace("\n","")
str_txt=str_txt.replace(". ",".")
str_txt=str_txt.replace("! ",".")
str_txt=str_txt.replace("? ",".")
print("Файл после фильтрации")
print(str_txt)


# Формирование списка предложений
sentence=""
sentences=list()
i=int(0)
for char in str_txt:
    sentence=sentence.__add__(char)
    if (char == ".") or (char == "!") or (char == "!"):
        print(i, sentence)
        sentences.append(sentence)
        i+=1
        sentence=""
print(sentences)



print("\n\nВведенный символ содержится в следующих предложениях:")
word=","
print("Введен символ")
print(word)
for sentence in sentences:
    if (sentence.__contains__(word)):
        print (sentence) 

print("\n\nВведенные строчные символы будут заменены прописными вначале слова")
letters=["о", "п", "р"]

for sentence in sentences:
    words=sentence.split()
    for word in words:
        for letter in letters:
            if (word[0]==letter):
                word=word.capitalize()
        print(word," " , end ='')
    print ("\n")
print(letters)