sign = '"'
list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i=0

def num(i,y):
    list1[i] = n.zfill(y)
    list1.insert(i, sign)
    list1.insert(i + 2, sign)


while i < len(list1):
    n = list1[i]

    if n.isdigit():
        num(i,2)
        i += 2
    elif n[0] in ["+","-"] and  n[1:].isdigit():
        num(i, 3)
        i += 2

    i += 1





message = ' '.join(list1)
print(message)