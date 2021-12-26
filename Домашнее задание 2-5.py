import random
list2 =[]
n=0
while (n <= 20):
    list2.append(f'{random.uniform(1,1000):.2f}')
    n += 1
list3=[]
for g in list2 :
    r=g.split(".")[1]
    kk=g.split(".")[-1]
    list3.append(f'{r} руб {kk} коп')
print(list3)
list2.sort()
print(list2)
print(sorted(list2, reverse=True))

print(sorted(list2, reverse=True)[:5])

