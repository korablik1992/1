from random import randrange

def get_jokes(x):
        list_j = []
        for _ in range(x):
            jk = ' '.join([noun[randrange(len(noun))], adv[randrange(len(adv))], adj[randrange(len(adj))]])
            list_j.append(jk)
        print(list_j)


noun = ["автомобиль", "лес", "огонь", "город", "дом"]
adv = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adj = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(10)