from data import features
from player import message_output
import random
import time


class Character:
    def __init__(self, params):
        self.name = params['name']
        self.lives = params['lives']
        self.energy = params['energy']
        self.energy_max = params['energy_max']
        self.energy_name = params['energy_name']
        self.energy_potion_name = params['energy_potion_name']
        self.skill_book = params['skill_book']
        self.char_auto = params['char_auto']
        self.char_self = params['char_self']
        self.char_move = params['char_move']
        self.potions = params['item']['potion']
        self.ingredient = params['item']['ingredient']
        self.brewed_potions = []
        self.weapon = params['weapon']

        self.strength = params['strength']
        self.moral = params['moral']
        self.type = params['type']

    # ######################### Methods ###############################
    def place_board(self, len_feld):            # OK
        """Beschreibung

        gibt eine zufällige x und eine y Position zurück
        diehnt zur Plazierung von K.I. und Spieler

        :param len_feld:
        :return: x und y wert
        """
        width = len_feld
        height = len_feld
        max_rnd = width * height
        pos = random.randint(0, max_rnd-1)
        x_pos = (pos % width)
        y_pos = (pos // width)
        return y_pos, x_pos

    # move K.I.
    def auto_move(self, rival_pos, my_pos):         # OK
        """ Beschreibung

        Vergleicht die X und Y Koordinaten der beiden K.I. 's
        und gibt neue X und Y Koordinaten für die zu ziehende K.I.



        :param rival_pos:
        :param my_pos:
        :return: y, x, go gibt die Koordinaten X und Y zurück sowie die Richtung(z.b. Norden)
        """
        y = my_pos[0]
        x = my_pos[1]

        if y < rival_pos[0] and x < rival_pos[1]:
            y += 1
            x += 1
            go = 'Südwesten'

        elif y > rival_pos[0] and x > rival_pos[1]:
            y -= 1
            x -= 1
            go = 'Nordosten'

        elif y < rival_pos[0] and x > rival_pos[1]:
            y += 1
            x -= 1
            go = 'Südenosten'

        elif y > rival_pos[0] and x < rival_pos[1]:
            y -= 1
            x += 1
            go = 'Nordwesten'

        elif y < rival_pos[0] and x == rival_pos[1]:
            y += 1
            go = 'Süden'

        elif y > rival_pos[0] and x == rival_pos[1]:
            y -= 1
            go = 'Norden'

        elif y == rival_pos[0] and x < rival_pos[1]:
            x += 1
            go = 'Osten'

        elif y == rival_pos[0] and x > rival_pos[1]:
            x -= 1
            go = 'Westen'

        else:
            go = 'nicht gefunden'
        return y, x, go

    # move Player

    def self_move_input(self, my_pos, game_field):  # OK
        """ Bescheibung:

        Vergleicht die X und Y Position des Spielers, speichert die Richtung, die der Spieler gehn kann,
        in X und Y und gibt diese zurück

        :param my_pos:
        :param game_field:
        :return: y, x, go gibt die Koordinaten X und Y zurück sowie die Richtung(z.b. Norden)

        Details:
          X Achse
        Y|0|_|_|
        A|_|_|_|
        c|_|_|_|
        Spieler steht auf X 0 und Y 0 so kann er nur in 3 Richtungen ziehen
        Bei X 1 und Y 1 wären es 8 Richtungen
        Bei falschen oder keinen Eingaben wird die Funktion erneut aufgerufen(rekursiv)
        """
        y = my_pos[0]
        x = my_pos[1]
        max_xy = len(game_field) - 1
        richtung = ""

        if y == 0 and x == 0:
            richtung = input('(d) für E, (c) für SE und (x) für S\n')
            wertung = ['d', 'c', 'x']

        elif y == 0 and x == max_xy:
            richtung = input('(x) für S, (y) für SE und (a) für W\n')
            wertung = ['x', 'y', 'a']

        elif y == 0 and 0 < x < max_xy:
            richtung = input('(d) für E, (c) für SE, (x) für S, (y) für SW und (a) für W\n')
            wertung = ['d', 'c', 'x', 'y', 'a']

        elif x == 0 and 0 < y < max_xy:
            richtung = input('(w) für N, (e) für NE, (d) für E, (c) für SE und (x) für S\n')
            wertung = ['w', 'e', 'd', 'c', 'x']

        elif x == 0 and y == max_xy:
            richtung = input('(w) für N, (e) für NE, (d) für E\n')
            wertung = ['w', 'e', 'd']

        elif 0 < x < max_xy and 0 < y < max_xy:
            richtung = input('(w) für N, (e) für NE, (d) für E, (c) für SE\n'
                             '(x) für S, (y) für SW, (a) für W und (q) für NW\n')
            wertung = ['w', 'e', 'd', 'c', 'x', 'y', 'a', 'q']

        elif 0 < x < max_xy and y == max_xy:
            richtung = input('(w) für N, (e) für NE, (d) für E, (a) für W und (q) für NW\n')
            wertung = ['w', 'e', 'd', 'a', 'q']

        elif 0 == max_xy and y == max_xy:
            richtung = input('(w) für N, (a) für W und (q) für NW\n')
            wertung = ['w', 'a', 'q']

        else:
            richtung = ""
            wertung = "error"
            print(f"self_move keine positions eingabe")  # TEST

        if richtung not in wertung:
            message_output(features['message']['wrong_entry'])
            return self.self_move_input(my_pos, game_field)

        return richtung

    def self_move(self, my_pos, richtung):              # OK
        """Beschreibung

        Je nach dem welche Richtung der User eingegeben hat, wird die neue Richtung in X und Y gespeichert
        und zurückgegeben

        :param my_pos: X und Y meiner Position
        :param richtung: wird von der Funktion self_move_input() gegeben
        :return: gibt X, Y und go(die Richtung) zurück
        """
        y = my_pos[0]
        x = my_pos[1]
        if richtung:
            if richtung == 'w':
                y -= 1
                go = 'Norden'

            elif richtung == 'e':
                y -= 1
                x += 1
                go = 'Nordosten'

            elif richtung == 'd':
                x += 1
                go = 'Osten'

            elif richtung == 'c':
                y += 1
                x += 1
                go = 'Südosten'

            elif richtung == 'x':
                y += 1
                go = 'Süden'

            elif richtung == 'y':
                y += 1
                x -= 1
                go = 'Südwest'
            elif richtung == 'a':
                x -= 1
                go = 'Westen'
            elif richtung == 'q':
                y -= 1
                x -= 1
                go = 'Nordwesten'
            else:
                go = 'Da ging erwas schief'  # TEST
        else:
            go = 'false'  # TEST

        return y, x, go

    def show_resources(self):                       # OK
        """Beschreibung:

        Zeigt die Ressourcen des Spielers an (0|10 Holz 0|10 Sonnengras 0|10 Mondstengel)

        :return: None
        """
        message_output(f"{self.ingredient['wood']}|{self.ingredient['wood' + '_max']} {features['loot']['wood']['name']}"
        f" {self.ingredient['sungrass']}|{self.ingredient['sungrass' + '_max']} {features['loot']['sungrass']['name']}"
        f" {self.ingredient['moonstems']}|{self.ingredient['moonstems' + '_max']} {features['loot']['moonstems']['name']}")

    def tile_action(self, tile):
        """Beschreibung

        Die beiden Funktionen resource_collect() und building_action() sind in dieser Funktion um konflikte zu vermeiden

        :param tile:
        :return: None

        Details:
        Hier wird abgefrag was sich auf dem tile des Spielfeldes befindet wo der User hingeht
        falls es eine Resource ist wird die Funtion resource_collect() aufgerufen
        falls es ein ManaSchrein ist die building_action() Funktion
        kann hier noch weiter ausgebaut werden
        """
        if tile in features['loot']['loot_list']:
            self.resource_collect(tile)
        elif tile in features['building']['building_list']:
            self.building_action(tile)
        else:
            message_output('Hier gibt es nix\n')

    def resource_collect(self, resource):       # OK
        """Beschreibung:

        Diese Funktion diehnt zum ernten von Ressourcen und zur Ausgabe von Nachrichten der einzelnen ernte Schritte
        mit verzögerung von 1 sec


        :param resource: wie (Holz, Pflanze ...) wird übergeben
        :return: loot_count

        Details:
        Jede Ressource hat verschiedenen Nachrichten die in einem dict gespeichert sind und ausgegben werden sollen
        z.b.
        'wood': {
            'name': 'Holz',
            'count_list': [3, 4, 5],
            'message': {
                'first': 'sieht einen Baum',
                'input': 'zum ernten dück (e), weitergehn mit space\n', # alle Eingaben ausser e führen zum
                                                                          move auf das Ressourcenfeld
                'pick_beginning': 'holt die Axt raus',
                'pick': 'hack',                 # soll 3 bis 5 mal mit einer Verzögerung von 1 sec ausgegeben werden
                'item_falls': 'Baum fällt',
                'pick_end': 'packt die Axt ein',
                'loot': 'sammelt'
            }

        Es kann nur eine maximalwert an Ressourcen geerntet werden
        1*  ist dieser erreicht kommt eine Meldung das diese Ressource nicht mehr geerntet werden kann
            und eine Anzeige 10|10 ressourcen name
        2*  falls meine Ressourcen kleiner sind als der Maxwert und der User e gedrückt hat
            werden die einzelnen Ernteschritte ausgegeben und eine zufällige zahl in loot_count gespeichert
            loot_list = features['loot'][resource]['count_list'] eine zahlen liste
            random.shuffle(loot_list)
            loot_count = loot_list[0]
        3*  falls meine Ressource + loot_count kleiner als der Maxwert ist dann ist
            Ressource = Ressource + loot_count
            und es werden 2 Nachrichten ausgegeben z.b.
                Karina sammelt 2 Mondstengel ein
                Karina hat 2|10 Mondstengel
        4*  falls meine Ressource kleine ist als der Maxwert und der
            Maxwert kleiner ist als meine Ressource + loot_count dann ist der
            loot_count = Maxwert - meine Ressource


        """

        message_output(f"{features['loot'][resource]['message']['first']}")
        if self.ingredient[resource] == self.ingredient[resource + '_max']:         # 1*
            message_output(f"Du kannst nicht mehr {features['loot'][resource]['name']} tragen "
            f"{self.ingredient[resource]} | {self.ingredient[resource + '_max']} {features['loot'][resource]['name']}")

        elif self.ingredient[resource] < self.ingredient[resource + '_max']:        # 2*
            action = input(features['loot'][resource]['message']['input'])
            if action == 'e':
                message_output(f"{features['loot'][resource]['message']['pick_beginning']}")
                time.sleep(1)
                count = 0
                rand_number = random.randint(3, 5)
                while count < rand_number:
                    message_output(f"{features['loot'][resource]['message']['pick']}")
                    time.sleep(1)
                    count += 1
                message_output(f"{features['loot'][resource]['message']['item_falls']}")
                time.sleep(1)
                message_output(f"{features['loot'][resource]['message']['pick_end']}")
                time.sleep(1)
                loot_list = features['loot'][resource]['count_list']
                random.shuffle(loot_list)
                loot_count = loot_list[0]

                if self.ingredient[resource] + loot_count <= self.ingredient[resource + '_max']:  # 3*
                    self.ingredient[resource] += loot_count
                    message_output(f"{self.name} {features['loot'][resource]['message']['loot']} {loot_count} "
                          f"{features['loot'][resource]['name']} ein")

                    message_output(f"{self.name} hat {self.ingredient[resource]}|{self.ingredient[resource + '_max']}"
                          f" {features['loot'][resource]['name']}")
                    message_output()
                    return loot_count
                elif self.ingredient[resource] < self.ingredient[resource + '_max'] < self.ingredient[resource] + \
                        loot_count:         # 4*
                    loot_count = self.ingredient[resource + '_max'] - self.ingredient[resource]
                    self.ingredient[resource] += loot_count
                    message_output(f"{self.name} {features['loot'][resource]['message']['loot']} {loot_count} "
                          f"{features['loot'][resource]['name']} ein")
                    message_output(f"{self.name} hat {self.ingredient[resource]}|{self.ingredient[resource + '_max']}"
                          f" {features['loot'][resource]['name']}")
                    message_output()
                    return loot_count

    def building_action(self, building):

        if building in features['building']['building_list']:
            # erste buildin message
            message_output(f"{features['building'][building]['message']['first'].format(features['building'][building]['resource_coast']['Holz'])}")
            # Abfrage ob genug resourcen vorhanden sind
            if features['building'][building]['resource_coast']['Holz'] <= self.ingredient['wood']:
                message_output(f"{features['building'][building]['message']['resourcen_check'].format(self.ingredient['wood'])}")
                action = input(features['building'][building]['message']['input'])
                if action == 'e':
                    message_output(f"{features['building'][building]['message']['wood_campfire']}")
                    self.ingredient['wood'] -= features['building'][building]['resource_coast']['Holz']
                    time.sleep(1)
                    count = 0
                    rand_number = random.randint(7, 10)
                    while count < rand_number:
                        if self.energy_max >= self.energy:
                            message_output(f"{features['building'][building]['message']['fire']}")
                            rand_energy = random.randint(8, 14)
                            self.energy += rand_energy
                            message_output(f"{self.energy} {self.energy_name}")
                            time.sleep(1)
                            count += 1
                        elif self.energy_max < self.energy:
                            if rand_number > count:
                                count += 1
                                message_output(f"{features['building'][building]['message']['fire']}")
                                time.sleep(1)
                    message_output(f"{features['building'][building]['message']['item_falls']}")
                    time.sleep(1)
                    message_output(f"{features['building'][building]['message']['pick_end']}")
                    # Hp und Ma oder Sta anzeigen

                    time.sleep(1)

            else:
                # falls nicht Meldung ausgeben wieviel noch fehlt
                need_resource = features['building'][building]['resource_coast']['Holz'] - self.ingredient['wood']
                message_output(f"{features['building'][building]['message']['need_resourcen'].format(need_resource)}")
        else:
            message_output('Manaschrein ging shief', building)  # Test Ausgabe

    def use_potion(self, potion_name):
        """Beschreibung:

        Falls K.I. oder der Spieler Tränke haben, werden diese benutzt um Mana oder Stamina
        zu erhöhen, der Trank wird aus der Itemliste gestrichen.
        Desweiteren wird Abgefragt ob es sich um
            einen Trank handelt Ausgabe im Singular (hat noch einen)
            oder um mehrere Ausgabe im Plural       (hat noch )
            oder um keinen Trank                    (hat keinen)


        :param potion_name:
        :return:
        """

        # Abfragen ob Potion vorhanden sind
        if self.potions[potion_name] > 0:
            effect = features["potion"][self.energy_potion_name]["effect"]
            message_output(f'{self.name} {features["potion"][self.energy_potion_name]["message"]}')
            self.energy += features["potion"][self.energy_potion_name][effect]   # mana oder sta wird erhöht
            self.potions[potion_name] -= 1                          # eine Potion wird abgezogen
            if self.potions[potion_name] > 1:                       # abfrage für Singular | Plural
                message_output(f'{self.name} hat noch {self.potions[potion_name]} '
                      f'Flaschen {features["potion"][self.energy_potion_name]["name"]["p"]}')
            elif self.potions[potion_name] == 1:                       # abfrage für Singular | Plural
                message_output(f'{self.name} hat noch einen {features["potion"][self.energy_potion_name]["name"]["s"]}')
            elif self.potions[potion_name] == 0:
                message_output(f'{self.name} hat keinen {features["potion"][self.energy_potion_name]["name"]["s"]}')

    def auto_attack(self, enemy):
        """Beschreibung:

        Beschreibt den Kampfablauf der beiden K.I.'s

        :param enemy: die gegen K.I.
        :return: gibt die damage zurück (wird zur Anzeige benötigt |trifft mit 10 ..| )

        Details:
        energi ist das Mana bei Magierklassen und Stamina bei den Kämpferklassen
        1*  Zuerst wird abgefragt ob die energie kleiner ist als die energiekosten des skills
            falls ja wird mit der Funktion use_potion('energypotion') ein Trank benutzt und die Energie wird um einen
            bestimmten Wert aufgefüllt
        2*  falls kein Trank mehr vorhanden ist und die Energikosten über der Energie sind,
            kämpft die K.I. mit der Waffe, Schaden(damage) wird der gegen K.I. vom den Lebenspunkte abgezogen wenn
            die Lebenspunkte größer gleich dem Schaden sind
            anderenfalls werden die Lebenspunkte des Gegners aud 0 gesetzt,
            so kann der Gegner keine minus Lebenspunkte haben
        3*  wie 2* nur das der Schaden von den Skill atacken kommt, hier werden die Energikosten der
            Energie der K.I. abgezogen

        """
        damage = 0
        if self.energy < features["skill"][self.skill_book[0]]["energy_cost"]:          # 1*
            self.use_potion('energypotion')

        if self.potions['energypotion'] < 1 and \
                self.energy < features["skill"][self.skill_book[0]]["energy_cost"]:     # 2*
            message_output(f'{self.name} {self.weapon["message"]} {enemy.name}')
            damage = 10

            if enemy.lives >= damage:
                enemy.lives -= damage
            else:
                enemy.lives = 0

        if self.energy >= features["skill"][self.skill_book[0]]["energy_cost"]:         # 3*
            message_output(f'{self.name} {features["skill"][self.skill_book[0]]["message"] } {enemy.name}')
            damage = (features['skill'][self.skill_book[0]]['dmg'] * self.lives) // 100

            if enemy.lives >= damage:
                enemy.lives -= damage
            else:
                enemy.lives = 0
            self.energy -= features['skill'][self.skill_book[0]]['energy_cost']

        return damage

    def fight(self, enemy):
        pass

    # ######################### Override Methods ###############################
    def __str__(self) -> str:
        return f'Name: {self.name} \
                init_lives {self.lives} \
                lives {self.energy} \
                strength {self.weapon}\
                char {self.char_self}'

    # ######################### Getter Setter ##########################

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, name):
    #     self.__name = name
    #
    # @property
    # def lives(self):
    #     return self.__lives
    #
    # @lives.setter
    # def lives(self, lives):
    #     self.__lives = lives
    #
    # @property
    # def strength(self):
    #     return self.__strength
    #
    # @strength.setter
    # def strength(self, strength):
    #     self.__strength = strength
    #
    # @property
    # def char_auto(self):
    #     return self.__char_auto
    #
    # @char_auto.setter
    # def char_auto(self, char_auto):
    #     self.__char_auto = char_auto
    #
    # @property
    # def char_move(self):
    #     return self.__char_move
    #
    # @char_move.setter
    # def char_move(self, char_move):
    #     self.__char_move = char_move
    #
    # @property
    # def potions(self):
    #     return self.__potions
    #
    # @potions.setter
    # def potions(self, potions):
    #     self.__potions = potions
    #
    # @property
    # def brewed_potions(self):
    #     return self.__brewed_potions
    #
    # @brewed_potions.setter
    # def brewed_potions(self, brewed_potions):
    #     self.__brewed_potions = brewed_potions

