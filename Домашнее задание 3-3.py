def thesaurus(*args):
    names = sorted(set(x[0]for x in args))
    dict_thesaurus = {}
    for f in names:
        f_letter = f[0].capitalize()
        dict_thesaurus[f_letter] = list(filter(lambda x: x[0] == f_letter, args))

    return (dict_thesaurus)


print(thesaurus("Иван", "Мария", "Петр", "Илья"))