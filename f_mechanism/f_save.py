def f_save(enemy, player, level):
    import pickle
    data = [enemy, player, level]
    with open("save", "wb") as d:
        pickle.dump(data, d)


def f_load():
    import pickle
    with open("save", "rb") as g:
        a = pickle.load(g)

    for i in a:
        enemy, player, level = a
    return (enemy, player,level)