from Character import Character
from data import features


class MageClass(Character):
    def __init__(self, params):
        super().__init__(params)
         # self.spell_book = params['spell_book']
        # self.mana = params['mana']

    # # ######################### Methoden ###############################

    ################
    # ### attack ######################################################################################
    ################

    def mag_auto_attack(self, enemy):
        damage = 0
        if self.energy < features["spells"][self.skill_book[0]]["mana_cost"]:
            self.use_potion('manapotion')

        if self.potions['manapotion'] < 1 and self.energy < features["spells"][self.skill_book[0]]["mana_cost"]:
            print(f'{self.name} {self.weapon["message"]} {enemy.name}')
            damage = 10

            if enemy.lives >= damage:
                enemy.lives -= damage
            else:
                enemy.lives = 0

        if self.energy >= features["spells"][self.skill_book[0]]["mana_cost"]:
            print(f'{self.name} {features["spells"][self.skill_book[0]]["message"] } {enemy.name}')
            damage = (features['spells'][self.skill_book[0]]['dmg'] * self.lives) // 100

            if enemy.lives >= damage:
                enemy.lives -= damage
            else:
                enemy.lives = 0
            self.energy -= features['spells'][self.skill_book[0]]['mana_cost']

        return damage


    # ######################### Getter Setter ###############################


