import os,sys
import time, datetime
import cgi, cgitb
cgitb.enable()
sys.stderr  =  sys.stdout

def find_word():

    print("\n<h3>Логин g00u00, задача 123</h3>", end="")
    print("\n<p>Написать программу, которая считывает текст из файла и выводит на экран только предложения, содержащие введенное с клавиатуры слово.</p>", end="")
    string = str()
    print('<a href="../tmp/file_pav_02.txt">\n\n<h3>Построчное содержание файла</h3></a>',end="")
    with open('./find_word.txt', mode='r', encoding="utf-8") as f_read:
        for line in f_read.readlines():
            string+= line
            print(line,"\n<br>", end="")
    print("\n</p>")

    print("\n\n<h3>Решение задачи</h3>", end='')
    word='код'
    print("\n<p>Введено следующее слово:",word,"</p>", end="")
    string=string.replace("\n","")
    string=string.replace(". ",".")
    string=string.replace("! ","!")
    string=string.replace("? ","?")
    print("\n<p>Файл после обработки его содержания фильтрами:", end='')
    print("\n<br>",string, "\n</p>")
    sentences=list()
    sentence=str()
    print("\n<p>Предложения в виде строк:", end='')
    for char in string:
        if (char != '.' and char != '!' and char != '?'):
            sentence=sentence.__add__(char)
        else:
            sentence=sentence.__add__(char)
            sentences.append(sentence)
            print("\n<br>",sentence, end='')
            sentence=""
    print("\n</p>")
    print ("\n<p>Cлово \"", word, "\" содержится в следующих предложениях:", sep='', end='')
    #word=word.ljust((word.__len__()+1), " ")
    #word=word.rjust((word.__len__()+1), " ")
    for sentece in sentences:
        if (sentece.__contains__(word)):
            print ("\n<br>",sentece)
    print("</p>")
  
if __name__ == '__main__':
    find_word()
