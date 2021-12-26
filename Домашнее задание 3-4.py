def thesaurus(*args) -> dict:
    surnames = sorted(set(x.split(' ')[1][0]for x in args))
    dict_thesaurus = dict()
    for f_sur in surnames:
        dict_thesaurus[f_sur] = list(filter(lambda x: x.split(' ')[1][0] == f_sur, args))
        name = sorted(set(x[0] for x in dict_thesaurus[f_sur]))
        name_thesaurus = dict()
        for f_name in name:
            name_thesaurus[f_name] = list(filter(lambda x: x[0] == f_name, dict_thesaurus[f_sur]))
        dict_thesaurus[f_sur] = name_thesaurus
    return dict_thesaurus


print(thesaurus("Иван Cергеев", "Мария Васечкина", "Петр Афанасьев", "Илья Петров"))
