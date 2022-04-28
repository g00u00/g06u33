import random

random.seed()

randoms=list()
minus_random =list()
plus_random = list()

sizeof_list=100
for i in range(sizeof_list):
    int_random = random.randint(-100, 100)
    randoms.append(int_random)
print (randoms)

for random in randoms:
    if random>0:
        plus_random.append(random)
    elif random<0:
        minus_random.append(random)

print (plus_random)
print (minus_random)
        