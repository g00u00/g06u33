import random
random.seed()
print("\n\nrandom.randint(-100, 100): ", random.randint(-100, 100)) # оцениваем генератор


randoms=list()
randoms_positive = list()
randoms_negative =list()

len_of_list=25
for i in range(len_of_list): 
    int_random = random.randint(-100, 100)
    randoms.append(int_random)
print ("\n\nrandoms:",randoms)


for random in randoms:
    if random>0:
        randoms_positive.append(random)
    elif random<0:
        randoms_negative.append(random)
print ("\n\nrandoms_positive:",randoms_positive)
print ("\n\nrandoms_negative:",randoms_negative)



print('''\n\n
4. Дан одномерный массив числовых значений, насчитывающий N элементов.
Выполнить перемещение элементов массива по кругу вправо, 
т. е. A[1] -> A[2];  A[2] -> A[3];  . . .  A[n] -> A[1].
''')

print ("randoms: \n", randoms)

randoms_moved =list()
#нулевому элементу присваивем значение крайнего правого
randoms_moved .append(randoms[(randoms.__len__()-1)])
print("randoms_moved: \n", randoms_moved)

for random in randoms: #добавляем по одному элементу из списка
    randoms_moved .append(random)

print ("randoms_moved: \n", randoms_moved) #видим  лишний элемент
randoms_moved .__delitem__( randoms_moved .__len__()-1)#удаляем  лишний элемент

print("\nСравнение массивов")
print ("randoms: \n", randoms)
print ("randoms_moved: \n", randoms_moved)



print('''\n\n
34. Даны число P и число H. Определить сумму чисел меньше P, произведение
чисел больше H и количество чисел в диапазоне значений P и H. При вводе
числа равного P или H, закончить работу.
''')

print ("randoms: \n", randoms)
p=20
h=95
print ("p = ",p)
print ("h = ",h)

rand_sum_le_p=0 #начальная сумма
rand_mult_ge_h=1 #начальный сомножитель
i_amount_of_numbers=0 #начальное количество
for random in randoms:
    if (random < p):
        rand_sum_le_p+=random
    if (random > h):
        rand_mult_ge_h*=random
    if (random > p and random < h):
        i_amount_of_numbers+=1

print("rand_sum_le_p = ", rand_sum_le_p)
print("rand_mult_ge_h = ", rand_mult_ge_h)        
print("i_amount_of_numbers = ", i_amount_of_numbers)
        

print('''\n\n
6. Дан одномерный массив числовых значений, насчитывающий N элементов.
Поменять местами группу из M элементов, начинающихся с позиции K с
группой из M элементов, начинающихся с позиции P.
''')         
print ("randoms:\n", randoms)
new_randoms=list()
i=0
for random in randoms:
    new_randoms.append(randoms[i])
    i+=1
print ("new_randoms:\n", new_randoms)

n=(randoms.__len__()-1)
m=3
k=5
p=10
print ("\n n,m,k,p: \n", n, m, k, p)


i=0 #счетчик по массиву 
i_of_k=0 #счетчик по диапазону
i_of_p=0 #счетчик по диапазону
for random in randoms:
    
    if (i>=k and i<(k+m)):
        new_randoms[i]=randoms[p+i_of_k]
        i_of_k+=1
        print("i:",i, " new_randoms[>=k]:",new_randoms[i])
        
    if (i>=p and i<(p+m)):
        new_randoms[i]=randoms[k+i_of_p]
        i_of_p+=1
        print("i:",i, " new_randoms[>=p]: ",new_randoms[i])
    i+=1    
print("new_randoms: \n",new_randoms)
    



        