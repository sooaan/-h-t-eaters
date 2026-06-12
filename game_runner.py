from c_pawn.c_player.shit_digger import shit_digger
from c_pawn.c_player.shit_eater import shit_eater
from c_pawn.c_player.shit_head import shit_head
from c_pawn.c_player.shit_fire import shit_fire
from c_pawn.c_enemy.bat_shit import bat_shit
from f_mechanism.f_actionsv2 import f_action
from f_mechanism import f_menus
from f_mechanism import f_save


def f_start():
    option = f_menus.f_start_menu()
    if option.lower() in ["yes", "start"]:
        return True
    if option.lower() == "exit":
        return False


def f_charater():
    option = f_menus.f_charater_select()
    if option == "shit digger":
        charater = shit_digger()
        return charater
    if option == "shit eater":
        charater = shit_eater()
        return charater
    if option == "shit head":
        charater = shit_head()
        return charater
    if option == "shit fire":
        charater = shit_fire()
        return charater


def f_moves(count, enemy, charater):
    option = f_menus.f_attack_menu()
    f_action(enemy, charater, option)


def is_defeated():
    global enemy
    global charater
    global level
    
    try:
        if charater.health < 0:
            print("Lose")
            
            return True
    
        if enemy.health < 0:
            print("you Win")
            level += 1
            enemy = None
            f_save.f_save(enemy, charater, level)
            return True
    
        else:
            return False
    except:
        if charater != None:
            charater = None
            f_save.f_save(enemy, charater, level)
            SystemExit()
            
def f_level_loader():
    enemy, charater, level = f_save.f_load()

    if enemy != None and charater != None:
        print("Karmikonam1")
        enemy = bat_shit()
        return enemy, charater, level

    elif charater == None:
        print("Karmikonam2")
        charater = f_charater()
        return enemy, charater, level
    elif enemy == None:
        enemy = bat_shit()

def f_run_gmae(enemy, charater, level):
    f_moves(count, enemy, charater)
    
    return (
        f'''
    {enemy}
            ========================
    {charater}
        '''
    )


count = 0

enemy, charater, level = f_level_loader()
while f_start():
 
    print(is_defeated())
    
    while is_defeated() == False:
        count += 1
        print(f_run_gmae(enemy, charater, level))
        # print(charater.health)
    
    
