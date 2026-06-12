
import damage_type


def f_turn_base(count):
    from time import sleep
    sleep(0.1)
    if count % 2 != 0:
        return ("player")

    if count % 2 == 0:
        return ("enemy")


def f_action(count, enemy, player, option):
    from random import randint
    f_turn = f_turn_base(count)
    rannum1 = randint(1, 5)
    rannum2 = randint(1, 5)

    def f_normal_attack():

        if f_turn == "player":
            print("Player:")
            enemy.f_take_damge(player.f_attack())


        if f_turn == "enemy":
            print("Enemy:")
            player.f_take_damge(enemy.f_attack())


    def f_double_attack():

        if f_turn == "player":
            print("Player:")
            enemy.f_take_damge(damage_type.f_tripple_attack(player))


        if rannum1 == rannum2:

            if f_turn == "enemy":

                print("Enemy:")
                player.f_take_damge(enemy.f_attack())

        else:
            print("Enemy:Tripple")
            player.f_take_damge(enemy.f_attack())


    def f_triple_attack():

        if f_turn == "player":
            print("Player:Tripple")
            enemy.f_take_damge(damage_type.f_tripple_attack(player))


        if rannum1 == rannum2:

            if f_turn == "enemy":
                print("Enemy:Tripple")
                player.f_take_damge(enemy.f_attack())

        else:
            print("Enemy:Tripple")
            player.f_take_damge(enemy.f_attack())


    def f_kill_shot():

        if f_turn == "player":
            print("Player:Tripple")
            enemy.f_take_damge(damage_type.f_kill_shot(player))


        if rannum1 == rannum2:

            if f_turn == "enemy":
                print("Enemy:Tripple")
                player.f_take_damge(enemy.f_attack())

        else:
            print("Enemy:Tripple")
            player.f_take_damge(enemy.f_attack())

    def f_doge():
        if rannum1 == rannum2:
            player.f_doge()
        else:
            player.f_take_damge(enemy.f_attack())
    if option.lower() == "attack":
        print("1")
        f_normal_attack()
    elif option.lower() in "duble attack":
        f_double_attack()
    elif option.lower() == "tripple attack":
        f_triple_attack()
    elif option.lower() == "kill shot":
        f_kill_shot()
    elif option.lower() == "doge":
        f_doge()

        
