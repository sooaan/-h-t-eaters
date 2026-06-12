class player:
    from random import randint

    def __init__(self, health, level, stamina, damage,
                 stamina_reduction_rate,):

        self.health = health

        self.level = level

        self.stamina = stamina
        self.stamina_reduction_rate = stamina_reduction_rate
        self.start_stamina = self.stamina
        self.end_stamina = 0

        self.damage = damage

        self.doge_tick = 0
        self.doge_start_tick = self.randint(5, 20)
        self.doge_end_tick = 0

        
        self.f_healthGen()
        
    def f_healthGen(self):
        self.health = (100 * self.level) * (self.randint(1, 20))

    def f_take_damge(self,op_attack):
        self.doge()
        if self.doge_start_tick > self.doge_end_tick:
            self.health -= op_attack

        elif self.doge_end_tick >= self.doge_start_tick:

            self.doge_end_tick = self.doge_tick
            self.health -= 0
            return ("Player : 'Haha You MMMiiiisssed'")


    def f_attack(self):
        self.f_stamina()
        total_damage = self.damage*self.level
        return total_damage

    def f_stamina(self):
        if self.stamina == self.end_stamina:
            self.stamina = self.start_stamina

        if self.stamina > self.end_stamina:
            self.stamina -= self.stamina_reduction_rate

            if self.stamina == 0:
                self.critical_damage()
                return ("Enemy did a Critical Hit on you")


    def doge(self):
        self.doge_end_tick += 1

    def critical_damage(self):
        self.health = self.health - (self.f_attack() * self.randint(10, 30))

    def __int__(self):
        th = self.health
        return (th)

    def __str__(self):
        return (f"""
            Player :Health= {self.health}
               """)