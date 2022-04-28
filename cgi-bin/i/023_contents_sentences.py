contents='Предложение, которое содержит одну запятую. Предложение без запятой.'
sentences=contents.split('.')
print("\n\nСодержание:\n",sentences,"\n")
print("\ncontents.count('.'): ",contents.count('.'),"\n")
for key in range(contents.count('.')):
    
    print(key, sentences[key])
    s=sentences[key]
    
    if  not s.__contains__(','):
        print("\n\nПредложения без запятой_v0:\n",s)
    
    if s.__contains__(','):
        print("\nПредложения c запятой_v1:\n",s)
    else:
        print("\nПредложения без запятой_v1:\n",s)
