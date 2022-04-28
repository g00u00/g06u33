import os, pwd, datetime 
#print (os.getuid()) # numeric uid
print("\n\nИсполнитель, место и время исполнения")
#print (pwd.getpwuid(os.getuid()))
print(os.environ['USER'])
print(os.environ['PWD'])
print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M'))
print("\nФормулировка задачи(страница, номер, полное описание)\n...\n")
print("\nТекст программы\n...\n")
print("\nСодержание файла исходных данных программы\n...\n")
print("\nРешение задачи\n...\n")
print("\nСодержание файла с результатами\n...\n")
