str_txt=str()
stream_read=open("../tmp/pavl_02.txt", mode='r', encoding="utf-8")
str_txt=stream_read.read()
stream_read.close()

str_txt=str_txt.replace("\n","")
str_txt=str_txt.replace(". ",".")
str_txt=str_txt.replace("! ",".")
str_txt=str_txt.replace("? ",".")
print(str_txt)

sentence=""
sentences=list()
i=int(0)
for char in str_txt:
    if char != ".":
        sentence=sentence.__add__(char)
    else:
        print(i, sentence)
        sentences.append(sentence)
        i+=1
        sentence=""
print(sentences)
word="совершенно"
print("Ведено слово")
print(word)
for sentence in sentences:
    if (sentence.__contains__(word)):
        print (sentence)
print ("см предложение выше")



        