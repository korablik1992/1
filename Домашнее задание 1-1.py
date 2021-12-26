time = int(input("Ввeдите количество секунд"))
if (time<60):
    print (time , "cек")
elif (time<3600):
    min = time // 60
    sec = time % 60
    print(min , " мин " , sec , " cек")
elif (time<86400):
    hour = time // 3600
    min  = time % 3600 // 60
    sec =  time % 3600 % 60
    print(hour , " час " , min , " мин " , sec , " cек")
else:
    day = time // 86400
    hour = time % 86400 // 3600
    min = time % 86400 % 3600 // 60
    sec = time % 86400 % 3600 % 60
    print(day , " дней " , hour , " час " , min , " мин " , sec , " cек")

