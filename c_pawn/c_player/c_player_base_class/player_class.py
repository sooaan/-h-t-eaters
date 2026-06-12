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

        self.doge = False

        self.f_healthGen()

    def f_healthGen(self):
        self.health = (100 * self.level) * (self.randint(1, 20))

    def f_take_damge(self, op_attack):
        import random
        rannum1 = random.randint(1, 3)
        rannum2 = random.randint(1, 3)
        if self.doge != True:
            self.health -= op_attack

        elif self.doge == True:
            if rannum1 == rannum2:
                print ("Player : 'Haha You MMMiiiisssed'")
                self.health -= 0
            else:
                print ("Your doge went wrong")
                self.health -= op_attack
                

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

    def f_doge(self):
        self.doge = True
        
        return self.doge

    def critical_damage(self):
        self.health = self.health - (self.f_attack() * self.randint(1, 3))

    def __int__(self):
        th = self.health
        return (th)

    def __str__(self):
        return (f"""
            Player :
                    Health= {self.health}
                    Stamina= {self.stamina}
                    {self.f_stamina()}
                    
               """)
