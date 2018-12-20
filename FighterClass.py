from Character import Character
from data import features


class FighterClass(Character):

    def __init__(self, params):
        super().__init__(params)
        # self.stamina = params['stamina']
        # self.combat_skill = params['combat_skill']

    def fight_auto_attack(self, enemy):
        damage = 0
        if self.energy < features["skill"][self.skill_book[0]]["energy_cost"]:
            self.use_potion('energypotion')

        if self.potions['energypotion'] < 1 and \
                self.energy < features["skill"][self.skill_book[0]]["energy_cost"]:
            print(f'{self.name} {self.weapon["message"]} {enemy.name}')
            damage = 10

            if enemy.lives >= damage:
                enemy.lives -= damage
            else:
                enemy.lives = 0

        if self.energy >= features["skill"][self.skill_book[0]]["energy_cost"]:
            print(f'{self.name} {features["skill"][self.skill_book[0]]["message"] } {enemy.name}')
            damage = (features['skill'][self.skill_book[0]]['dmg'] * self.lives) // 100

            if enemy.lives >= damage:
                enemy.lives -= damage
            else:
                enemy.lives = 0
            self.energy -= features['skill'][self.skill_book[0]]['energy_cost']

        return damage


