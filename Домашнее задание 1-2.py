num = int(1)
uneven_1000 = []
for num in range(1000):
    if (num % 2)!=0 :
        num_cube = num ** 3
        uneven_1000.append(num_cube)

sum = 0
for part in uneven_1000:
    part_num = part
    part_num_sum = 0
    while part_num != 0:
        part_num_sum += part_num % 10
        part_num = part_num // 10
    if (part_num_sum % 7) == 0:
        sum += part_num_sum
    else:
        sum = sum
sum2 = 0
for part in uneven_1000:
    part += 17
    part_num = part
    part_num_sum = 0
    while part_num != 0:
        part_num_sum += part_num % 10
        part_num = part_num // 10
    if (part_num_sum % 7) == 0:
        sum2 += part_num_sum
    else:
        sum2 = sum2
print (sum)
print (sum2)





print(uneven_1000)