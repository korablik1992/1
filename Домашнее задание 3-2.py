
def num_translate() :
    word = input("Впишите числительное")
    if word .istitle():
        print(dict1.get(word.lower().title(), None))
    else:
         print(dict1.get(word.lower()))


dict1 = {
    "one" : "один",
    "two" : "два",
    "three" : "три",
    "four" : "четрые",
    "five" : "пять",
    "six" : "шесть",
    "seven" : "семь",
    "eight" :  "восемь",
    "nine" : "девять",
    "ten" : "десять"
}


num_translate()