from c_pawn.c_enemy.c_enemy_base_class.enemy_class import enemy
class bat_shit(enemy):
    def __init__(self,health=10, level=10, stamina=30, damage=20,
                 stamina_reduction_rate=2):
        enemy.__init__(self,health, level, stamina, damage,
                                   stamina_reduction_rate)      

