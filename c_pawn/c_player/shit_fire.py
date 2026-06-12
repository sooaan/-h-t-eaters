from c_pawn.c_player.c_player_base_class.player_class import player
class shit_fire(player):
    def __init__(self, health=200, level=200, stamina=36, damage=200,
                 stamina_reduction_rate=2):
        player.__init__(self, health, level, stamina, damage,
                        stamina_reduction_rate)
        