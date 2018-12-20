
"""
    Die Variablen dienen zu Testzwecken und können bei Veröffendlichung des Spiel gelöscht werden
"""
char_self = chr(128520)+'\t'
char_self_move = '::\t'

lives = 100
mana = 70

fire_man_cost = 35
pain_man_cost = 30
double_sta_cost = 30
mana_potion = 60

fire_dmg = 12
pain_dmg = 10
double_hit_dmg = 14

sta_potion = 60
stab_schaden = 10
besen_schaden = 12
schwert_schaden = 10

"""
    Hier werden alle Eigenschafften der Spielklassen in einem dictionary geschreiben
"""

character_props = {
    'Wizard': {
        'suny': {
            'name': 'Lia Suny',
            'lives': lives,
            'energy': mana,
            'energy_max': 120,
            'energy_name': 'Ma',
            'energy_potion_name': 'manapotion',
            'skill_book': ['fireball'],

            'strength': 2,
            'moral': 100,
            'type': 'M',
            'char_auto': '|W',  # + chr(9937),  # ' W ',
            'char_self': '-W-',
            'char_move': '|*',  # + chr(9928)
            'weapon': {
                'name': 'Stab',
                'dmg': stab_schaden,
                'message': 'Schwingt den Stab und trifft'
            },
            'item': {
                'potion': {
                    'energypotion': 3,  # mana
                    'energypotion_max': 3,
                    'healingpotion': 0,
                    'healingpotion_max': 3
                },
                'ingredient': {
                    'wood': 0,
                    'wood_max': 10,
                    'moonstems': 0,
                    'moonstems_max': 10,
                    'sungrass': 0,
                    'sungrass_max': 10,

                },
            },
        },

        'w': {
            'name': 'XXX',
            'lives': lives,
            'energy': 0,
            'energy_max': 120,
            'energy_name': 'Ma',
            'energy_potion_name': 'manapotion',
            'skill_book': ['fireball'],

            'strength': 2,
            'moral': 100,
            'type': 'M',
            'char_auto': '|P',
            'char_self': char_self,  # + chr(9937),  # ' W ',
            'char_move': char_self_move,  # + chr(9928)
            'weapon': {
                'name': 'Stab',
                'dmg': stab_schaden,
                'message': 'Schwingt den Stab und trifft'
            },
            'item': {
                'potion': {
                    'energypotion': 0,  # mana
                    'energypotion_max': 3,
                    'healingpotion': 0,
                    'healingpotion_max': 3

                },
                'ingredient': {
                    'wood': 0,
                    'wood_max': 10,
                    'moonstems': 0,
                    'moonstems_max': 10,
                    'sungrass': 0,
                    'sungrass_max': 10,
                }
            },
            'message': {
                'create': 'erstelle einen Wizard für'
            }

        },

    },

    'Witch': {
        'ursel': {
            'name': 'Ursel Raa',
            'lives': lives,
            'energy': mana,
            'energy_max': 120,
            'energy_name': 'Ma',
            'energy_potion_name': 'manapotion',
            'skill_book': ['pain'],

            'strength': 2,
            'moral': 100,
            'type': 'M',
            'char_auto': '|H',  # + chr(9927),  # ' H '
            'char_self': '-H-',
            'char_move': '|+',  # + chr(9957)
            'weapon': {
                'name': 'Hexenbesen',
                'dmg': besen_schaden,
                'message': 'Steigt vom Besen, schwingt ihn links rechts und trifft'
            },
            'item': {
                'potion': {
                    'energypotion': 3,  # mana
                    'energypotion_max': 3,
                    'healingpotion': 0,
                    'healingpotion_max': 3
                },
                'ingredient': {
                    'wood': 0,
                    'wood_max': 10,
                    'moonstems': 0,
                    'moonstems_max': 10,
                    'sungrass': 0,
                    'sungrass_max': 10,
                }
            },

        },

        'h': {
            'name': 'U',
            'lives': lives,
            'energy': 0,
            'energy_max': 120,
            'energy_name': 'Ma',
            'energy_potion_name': 'manapotion',
            'skill_book': ['pain'],

            'strength': 2,
            'moral': 100,
            'type': 'M',
            'char_auto': '|P',
            'char_self': char_self,  # + chr(9927),  # ' H '
            'char_move': char_self_move,  # + chr(9957)
            'weapon': {
                'name': 'Hexenbesen',
                'dmg': besen_schaden,
                'message': 'Steigt vom Besen, schwingt ihn links rechts und trifft'
            },
            'item': {
                'potion': {
                    'energypotion': 0,  # mana
                    'energypotion_max': 3,
                    'healingpotion': 0,
                    'healingpotion_max': 3

                },
                'ingredient': {
                    'wood': 0,
                    'wood_max': 10,
                    'moonstems': 0,
                    'moonstems_max': 10,
                    'sungrass': 0,
                    'sungrass_max': 10,
                }
            },
            'message': {
                'create': 'erstelle Hexe für'
            }
        },
    },

    'Warrior': {
        'kurak': {
            'name': 'Kurak',
            'lives': 100,
            'energy': 100,
            'energy_max': 120,
            'energy_name': 'Sta',
            'energy_potion_name': 'staminapotion',
            'skill_book': ['double_hit'],

            'strength': 80,
            'moral': 100,
            'type': 'W',
            'char_auto': '|K',  # + chr(9927),  # ' H '
            'char_self': '-K-',
            'char_move': '|+',  # + chr(9957)
            'weapon': {
                'name': 'Schwert',
                'dmg': schwert_schaden,
                'message': 'schwingt das Schwert links rechts und trifft'
            },
            'item': {
                'potion': {
                    'energypotion': 3,  # stamina
                    'energypotion_max': 3,
                    'healingpotion': 0,
                    'healingpotion_max': 3
                },
                'ingredient': {
                    'wood': 0,
                    'wood_max': 10,
                    'moonstems': 0,
                    'moonstems_max': 10,
                    'sungrass': 0,
                    'sungrass_max': 10,
                }
            },

        },

        'k': {
            'name': 'XX',
            'lives': 100,
            'energy': 0,
            'energy_max': 120,
            'energy_name': 'Sta',
            'energy_potion_name': 'staminapotion',
            'skill_book': ['double_hit'],

            'strength': 80,
            'moral': 100,
            'type': 'W',
            'char_auto': '|P',
            'char_self': char_self,  # + chr(9927),  # ' H '
            'char_move': char_self_move,  # + chr(9957)
            'weapon': {
                'name': 'Schwert',
                'dmg': schwert_schaden,
                'message': 'schwingt das Schwert links rechts und trifft'
            },
            'item': {
                'potion': {
                    'energypotion': 0,      # stamina
                    'energypotion_max': 3,
                    'healingpotion': 0,
                    'healingpotion_max': 3,
                },
                'ingredient': {
                    'wood': 0,
                    'wood_max': 10,
                    'moonstems': 0,
                    'moonstems_max': 10,
                    'sungrass': 0,
                    'sungrass_max': 10,
                }
            },
            'message': {
                'create': 'erstelle Krieger für'
            }
        },
    },



}

"""
    Hier werden alle Eigenschafften der Features in einem dictionary geschreiben
    w.z.b.
    board(Spielfeld) | größen, Schriftzeichen, message(Ausgaben) ...
    Skills(Schadensarten) | name, damage, message ...
    potion | name, zutaten(für die Herstellung) lives oder ...(Wert)...
    loot |  lootsorten, zahlenliste(menge von bis), 
            message steps(Ausgaben die Angezeigt werden wenn der User etwas lootet)
    
"""

features = {
    'board': {
        'name': 'Board',
        'size': {
            's': 5,
            'm': 10,
            'b': 15,
        },
        'char': '|_',  # ' ' + chr(9882) + ' ',  # chr(9617)*3
        'char_fight': '|X',  # + chr(9932)
        # 882 Holz | 127801 sungras | 127799 Mondscheinstengel | 9962 Manaschrein
        'char_list': [chr(882), chr(882), chr(127801), chr(127799), chr(127799),
                      chr(127801), chr(9962), chr(882), chr(127799)],
        chr(882)+'\t': 'wood',
        chr(127801)+'\t': 'sungrass',
        chr(127799)+'\t': 'moonstems',
        chr(9962)+'\t': 'manashrine',
        '::\t': 'fussspur',
        'message': {
            'size': 'Bitte die Spielfeldgröße eingeben\ns für 5*5, m für 10 * 10 und b für 15 * 15\n'
        }

    },
    'skill': {
        'thunderbolt': {
            'name': 'Thunderbolt',
            'dmg': 35,
            'energy_cost': 40,
            'effect': 'Stunn',
            'color': 'rot',
            'message': 'Zaubert Thunderbolt auf '
        },

        'fireball': {
            'name': 'Feuerball',
            'dmg': fire_dmg,
            'energy_cost': fire_man_cost,
            'effect': 'Verbrennung 2. Grades',
            'color': 'rot',
            'message': 'schmeist Feuerball auf '
        },

        'cold': {
            'name': 'Froststoß',
            'dmg': 15,
            'energy_cost': 20,
            'effect': 'Schränkt Bewegung ein',
            'color': 'blau',
            'message': 'Zaubert Froststoß auf '
        },

        'coldray': {
            'name': 'Froststrahl',
            'dmg': 40,
            'energy_cost': 40,
            'effect': 'Einfrieren',
            'color': 'blau',
            'message': 'Zaubert Froststrahl auf '
        },

        'pain': {
            'name': 'Schmerz',
            'dmg': pain_dmg,
            'energy_cost': pain_man_cost,
            'effect': 'angst',
            'color': 'rot',
            'message': '\"Schmerz und Qual komme auf\"'
        },

        'double_hit': {
            'name': 'Doppel Schlag',
            'dmg': double_hit_dmg,
            'energy_cost': double_sta_cost,
            'effect': 'doppelter Schaden',
            'message': 'schwingt das Schwert bliz schnell und trifft'
        }
    },

    'potion': {
        'healingpotion': {
            'name': {
                's': 'Heiltrank',
                'p': 'Heiltränke',
            },
            'zutaten': {
                'Sonnengras': 2,
                'Mondstengel': 2,
            },

            'steps': [
                'zaubert Sonnengras zu Pulver',
                'zauber Mondstengel zu Mondtausaft ',
                'mixt beides zusammen',
                'und füllt es in eine Flasche'
            ],
            'effect': 'lives',
            'color': 'red',
            'message' 'trinkt einen Heiltrank und fühlt sich lebendig'
            'force': 0,
            'lives': 50
        },

        'manapotion': {
            'name': {
                's': 'Manatrank',
                'p': 'Manatränke',
            },

            'zutaten': {
                'Sonnengras': 2,
                'Mondstengel': 2,
            },

            'steps': [
                'zaubert Mondstengel in Mehl',
                'zaubert Sonnengras zu Grastausaft',
                'mixt beides zusammen',
                'und füllt es in eine Flasche'
            ],

            'effect': 'mana',
            'color': 'grün',
            'message': 'trinkt einen Manatrank und fühlt sich erfrischt',
            'force': 0,
            'mana': mana_potion
        },

        'staminapotion': {
            'name': {
                's': 'Staminatrank',
                'p': 'Staminatränke',
            },

            'zutaten': {
                'Sonnengras': 2,
                'Mondstengel': 2,
            },

            'steps': [
                'hackt Mondstengel klitze klein',
                'presst Sonnengras aus',
                'mixt beides zusammen',
                'und füllt es in eine Flasche'
            ],

            'effect': 'stamina',
            'color': 'grün',
            'message': 'trinkt einen Staminatrank und fühlt sich fit',
            'force': 0,
            'stamina': sta_potion
        },
        'stechender schmerz': {     # TODO vieleicht ein Moral trank für fighter Klassen
            'name': 'Stechender Schmerz',
            'zutaten': [
                'Bärentatzen',
                'Distelkraut',
                'Spinengift',
                'arsen',

            ],
            'steps': [
                'zaubert Bärentatzen und Diestelkraut in Pulver',
                'Mixt das Pulver mit Schlangengift',
                'gibt Spinnengift und Arsen hinzu',
                'In Flasche füllen'
            ],
            'effect': 'Ermüdung',
            'color': 'grün',
            'force': 10
        }

    },

    'loot': {
        'loot_list': ['wood', 'sungrass', 'moonstems'],
        'wood': {
            'name': 'Holz',
            'count_list': [3, 4, 5],
            'message': {
                'first': 'sieht einen Baum',
                'input': 'zum ernten dück (e), weitergehn mit space\n',
                'pick_beginning': 'holt die Axt raus',
                'pick': 'hack',
                'item_falls': 'Baum fällt',
                'pick_end': 'packt die Axt ein',
                'loot': 'sammelt'
            }
        },
        'sungrass': {
            'name': 'Sonnengras',
            'count_list': [2, 3, 4],
            'message': {
                'first': 'sieht Sonnengras',
                'input': 'zum ernten dück (e), weitergehn mit space\n',
                'pick_beginning': 'holt die Sichel raus',
                'pick': 'schneid',
                'item_falls': 'hat eine Handvoll zusammen',
                'pick_end': 'packt die Sichel ein',
                'loot': 'sammelt'
            }
        },
        'moonstems': {
            'name': 'Mondstengel',
            'count_list': [2, 3, 4],
            'message': {
                'first': 'sieht Mondstengel',
                'input': 'zum ernten dück (e), weitergehn mit space\n',
                'pick_beginning': 'holt die Sichel raus',
                'pick': 'schneid',
                'item_falls': 'hat eine Handvoll zusammen',
                'pick_end': 'packt die Sichel ein',
                'loot': 'sammelt'
            }
        },
    },

    'building': {
        'building_list': ['manashrine'],
        'manashrine': {
            'name': 'Mana Schrein',
            'resource_coast': {'Holz': 5},
            'message': {
                'first': 'sieht ein Manaschrein, du benötigst {0:d} Holz zum meditieren',
                'resourcen_check': 'du hast {0:d} Holz',
                'need_resourcen': 'du benötigst noch {0:d} Holz',
                'input': 'zum meditieren dück (e), weitergehn mit space\n',
                'wood_campfire': 'schichtet Holz zum Lagerfeuer auf und zündet es an',
                'fire': 'brenn',
                'item_falls': 'du fühlst dich super',
                'pick_end': 'löscht das feuer\n',

            },
        },
    },

    'class': {
        'w': 'Wizard',
        'h': 'Witch',
        'k': 'Warrior',
        'all_class': ['w für Wizard', 'h für Hexe', 'k für Krieger'],
        'mage_class': ['w', 'h'],
        'fighter_class': ['k'],
        'class_list_b': ['Wizard', 'Witch', 'Warrior'],
        'class_list': [['Wizard', 'suny'], ['Witch', 'ursel'], ['Warrior', 'kurak']]
    },

    'message': {
        'welcome': 'Willkommen bei uns im Zauberwald',
        'game_mode': 'Drücke (a) um dir das Spiel anzuschauen oder (s) um selber zu spielen',
        'wrong_entry': 'Falsche eingabe'
    },
}



