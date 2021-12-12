
percent_ov = ('процентов')
percent_a = ('процента')
percent = ('процент')

for n in range(1, 101):
    if (10<n<20) or (n % 10 in [0, 5, 6, 7 , 8, 9]):
        answer_final = (n, percent_ov)
    elif n % 10 == 1:
        answer_final = (n, percent)
    else:
        answer_final = (n, percent_a)

    print(answer_final)
