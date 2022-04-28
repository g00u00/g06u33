print("\nСимволы из файла:")
my_string='Вопросительное предложение? Восклицательное предложение! Второе восклицательное предложение! Повествовательное предложение.'
print(my_string)
new_string=my_string.__add__(' Восклицательное предложение 2! ')
my_string=new_string
print (my_string)

print("\n\nФормируем законченные предложения ...")
sentence=str()
sentences=list()
i=0         
for symbol in my_string:
     if not(i==0  and symbol==" "):
         sentence_new=sentence.__add__(symbol)
         sentence=sentence_new
         i=i+1
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
        
