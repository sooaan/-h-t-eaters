from f_mechanism import f_damage_type

def f_action(enemy, player, option):
    from random import randint
    rannum1 = randint(1, 5)
    rannum2 = randint(1, 5)

    def f_normal_attack():

        print("Player: Did a Normal Attack")
        enemy.f_take_damge(player.f_attack())
        print("Enemy: Did a Normal Attack")
        player.f_take_damge(enemy.f_attack())


    def f_double_attack():

        print("Player:")
        enemy.f_take_damge(f_damage_type.f_tripple_attack(player))
        
        if rannum1 == rannum2:
            print("Enemy: Did a Duble Attack")
            player.f_take_damge(f_damage_type.f_double_attack(enemy))
        else:
            print("Enemy: Did a Normal Attack")
            player.f_take_damge(enemy.f_attack())


    def f_triple_attack():

        print("Player: Did a Tripple")
        enemy.f_take_damge(f_damage_type.f_tripple_attack(player))
        
        if rannum1 == rannum2:
            print("Enemy: Did a Tripple")
            player.f_take_damge(f_damage_type.f_tripple_attack(enemy))

        else:
            print("Enemy: Did a Normal Attack ")
            player.f_take_damge(enemy.f_attack())


    def f_kill_shot():

            print("Player: Did a Kill shot Attack")
            enemy.f_take_damge(f_damage_type.f_kill_shot(player))

            print("Enemy: Did a Normal Attack")
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

        
