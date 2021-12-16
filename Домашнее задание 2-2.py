sign = '"'
list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list2 = []
def list2_func(x,y):
    list2.append(x)
    list2.append(n.zfill(y))
    list2.append(x)
for x,n in enumerate(list) :

    if n.isdigit():
        list2_func(sign,2)
        
    elif n[0] in ["+","-"] and  n[1:].isdigit():
        list2_func(sign, 3)

    else:
        list2.append(n)
message = ' '.join(list2)
print(message)

