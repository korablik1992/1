
def num_translate():
    word = input("Впишите числительное")
    print(dict.get(word.lower(), None))


dict = {
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