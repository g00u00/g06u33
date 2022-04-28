Основы
https://docs.python.org/3.5/tutorial/introduction.html
https://docs.python.org/3.5/tutorial/introduction.html#numbers
https://docs.python.org/3.5/library/functions.html#input
https://docs.python.org/3.5/library/functions.html#print
https://docs.python.org/3.5/reference/compound_stmts.html#if
https://docs.python.org/3.5/tutorial/controlflow.html#intermezzo-coding-style

----------------------------------------------------------------
Списки (массивы)
https://docs.python.org/3.5/tutorial/introduction.html#lists
https://docs.python.org/3.5/tutorial/datastructures.html
https://docs.python.org/3.5/library/random.html?highlight=random#module-random
https://docs.python.org/3.5/library/stdtypes.html#range
https://docs.python.org/3.5/reference/compound_stmts.html#index-6
https://docs.python.org/3.5/library/operator.html?highlight=list%20__add__#module-operator
https://docs.python.org/3.5/library/

import random
a,b,c=10,20,30
squares = list()
for i in range(a):
    squares.append(random.randrange(b,c))
print(squares)

for item in "string":
    if item == "i":
        break
    print(item)
print("The end")


l=[1, 3, 6, 8, -2.4]
l_1=l[0:-1:2]


-----------------------------
Символы и строки
https://docs.python.org/3.5/tutorial/introduction.html#strings

my_string='Вопросительное предложение? Восклицательное предложение! Второе восклицательное предложение! Повествовательное предложение.'
print (my_string)
print("\n\nФормируем законченные предложения ...")
sentence=str()
sentences=list()
i=0         
for symbol in my_string:
    if not(i==0  and symbol==" "):
        sentence_new=sentence.__add__(symbol)
        sentence=sentence_new
        i+=1
        print(symbol, end="")
        if symbol=="." or symbol=="?" or symbol=="!":
            sentences.append(sentence)
            sentence=""
            i=0
            print("\n")
print(sentences)
print("\n\nОкончательные результаты:") 
for sentence in sentences: 
    if sentence[-1]=="!": print (sentence)
for sentence in sentences: 
    if sentence[-1]==".": print (sentence)


--------------------------------
Запись в файл и считывание данных из файла
https://docs.python.org/3.5/library/fileinput.html#fileinput.input
https://docs.python.org/3.5/library/functions.html#open
https://docs.python.org/3.5/library/io.html
https://www.tutorialspoint.com/python/python_files_io.htm
https://docs.python.org/3/library/string.html#string-formatting
https://www.datacamp.com/community/tutorials/python-data-type-conversion

Пример 1
f_stream = open('../tmp/test.txt', mode='a', encoding="utf-8", errors=None)
f_stream.write("%2s;%3.2f;%1i;%10s;\n" % (str("1-строка"), float(2), int(300), str("abc") ))
f_stream.close()
f_stream = open('../tmp/test.txt', mode='r', encoding = 'utf-8')
content = f_stream.read() 
print(content)
file.close()

Пример 2
file="../tmp/lr4.txt"
file_stream = open(file, mode='a', encoding="utf-8", errors=None)
file_stream.write("%2s; %2s; %2s; %2s; %2s;\n" % (str(os.environ['REMOTE_ADDR']), str(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')), str(task_name), str(form_word), str(right_sentences) ))
file_stream.close()

print("\nСчитываем данные из файла и обрабатываем")
r_stream = open(file, mode='r', encoding="utf-8")
print ("<table border=1>")
for line in r_stream.readlines():
    words = line.split(";")
    print ("words: ",words)
    print ("<tr valign=top>")
    for word in words[:-1]:
        print("<td>", word)
r_stream.close()
print ("</table>")

