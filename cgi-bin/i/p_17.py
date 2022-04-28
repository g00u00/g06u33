'''
П.17. Написать программу, которая считывает текст из файла и выводит его на экран,
после каждого предложения добавляя, сколько раз встретилось в нем введенное
с клавиатуры слово.
'''


text = "Разработчики языка Python придерживаются определённой философии языка языка программирования, называемой «The Zen of Python» («Дзен Питона», или «Дзен Пайтона»)[10]. Её текст выдаётся текст интерпретатором Python по команде import1 this (работает один раз за сессию). Автором этой философии считается Тим Петерс (Tim Peters)."
print("исходный текст: " + text)
word = 'языка'
print ("word: ", word)

sentenses = list()
buf = str()
for i in range(len(text)):
    buf += text[i]
    if text[i] == ";" or text[i] == '.' or text[i] == "!" or text[i] == "?":
        sentenses.append(buf)
        print(sentenses)
        buf = ''

print("len(sentenses):", len(sentenses))
for i in range(len(sentenses)):
    buf = sentenses[i]
    j = 0
    while buf.find(word) != -1:
        print("buf: ", buf)
        print("buf.find(word):", buf.find(word))
        buf = buf[buf.find(word)+len(word):len(buf)]
        j += 1
    sentenses[i] += " - [" + str(j) + "]"

for s in sentenses:
    print(s)
    
