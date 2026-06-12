from c_pawn.c_player.c_player_base_class.player_class import player
class shit_digger(player):
    def __init__(self, health=10, level=2, stamina=36, damage=10,
                 stamina_reduction_rate=2):
        player.__init__(self, health, level, stamina, damage,
                        stamina_reduction_rate)
        