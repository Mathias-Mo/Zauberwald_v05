"""
zum etwas austesten und zwischenspeichern gedacht
"""

import random
# my_list = ['Holz', 'Wasser', 'Mücke']
#
# print(my_list[my_list.index('Holz')+1])
# print(my_list.index('Holz')+1)
#
# my_dict = {'item': {
#                 'potion': {
#                     'manapotion': 3,
#                     'healingpotion': 0
#                 },
#                 'ingredient': {
#                     'wood': 0,
#                     'wood_max': 10,
#
#                 },
#             },
# }
#
# # self.ingredient[self.ingredient.index(resource)]
# my_list = my_dict['item']['ingredient']
#
# print(my_list['wood'+'_max'])

# from MyFactory import MyFactory
# from data import character_props as props
# import random
#
# class_list =[['Wizard', 'suny'], ['Witch', 'ursel'], ['Warrior', 'kurak']]
#
# random.shuffle(class_list)
# class_name = class_list[0][0]
#
# instance = MyFactory.instanciate(class_name, props[class_name.lower()][class_list[0][1]])
#
# print(instance.name)
###################################################################################################

# char_list = [f" {chr(882)}  ", f" {chr(882)}  ", f" {chr(127801)} ", f" {chr(127799)} ", f" {chr(127799)} ",
#               f" {chr(127801)} ", f" {chr(9962)} ", f" {chr(882)}  ", f" {chr(127799)} "]

# char_list = [f"{chr(882)}", f"{chr(882)}", f"{chr(127801)}", f"{chr(127799)}", f"{chr(127799)}",
#              f"{chr(127801)}", f"{chr(9962)}", f"{chr(882)}", f"{chr(127799)}"]
#
# random.shuffle(char_list)
#
# myboard = [char_list[i % len(char_list)] for i in range(25)]
#
#
#
# tmp_str = ''
# for i in range(0, 25, 5):
#     tmp_str = ''
#     for j in range(5):
#         tmp_str += str(myboard[(i+j)%len(myboard)] + '\t')
#         # tmp_str += format(str(myboard[(i + j) % len(myboard)]), '^6')
#     print(tmp_str)

# stringmy = 'Hallo du da {:s} du brauchst'
# print(stringmy.format(str(5)))


#####################################################################################
# dic = {
# '\\' : b'\xe2\x95\x9a',
# '-'  : b'\xe2\x95\x90',
# '/'  : b'\xe2\x95\x9d',
# '|'  : b'\xe2\x95\x91',
# '+'  : b'\xe2\x95\x94',
# '%'  : b'\xe2\x95\x97',
# }
#
# def decode(x):
#     return (''.join(dic.get(i, i.encode('utf-8')).decode('utf-8') for i in x))
#
# print(decode('+-------------------------------------%'))
# print(decode('|   Willkommen bei uns im Zauberwald   |'))
# print(decode('\\-------------------------------------/'))

print(b'\xe2\x95\x94'.decode('utf-8'))
#######################################################################################


    # if i % 5:
    #     tmp_str += "\n"
# print(tmp_str)

# class Tile:
#
#     def __init__(self):
#         self.neighbors = []
#         self.sign = [char_list]


# class Boardy:
#
#     def __init__(self, size):
#         self.size = size
#         self.tiles = []
#
#     def build_board(self):
#         for i in range(self.size**2):
#             x = i % self.size
#             y = i // self.size
#             self.tiles.append(Tile())
#         return board
#
#
# mychar = Tile()
#
# mychar.sign[0]
# print('hallo', mychar)


# format(my_feld[(i + 1 + j) % len(my_feld)], '<1s')
#
# board = Boardy(10)
#
# my_board = board.build_board()
#
# print(my_board)

# the_board = [my_board.tiles[i*10:i*10+10] for i in range(10)]
#
# width = 10
# i = 0
# j = 0
#
# for tile in the_board:
#     tmp_str = ''
#     i += 1
#
#     tmp_str += str(tile.sign[i % len(tile.sign)])
#     j += 1
#     print(' '.join(tmp_str))

#####################################################################
# class Tile:
#
#     def __init__(self):
#         self.neighbors = []
#         self.sign = '_'
#
#     def add_neighbor(self, neighbor):
#         self.neighbors.append(neighbor)
#
#     def __str__(self):
#         return self.sign
#
#
# class Boardy:
#
#     def __init__(self, size):
#         self.size = size
#         self.tiles = []
#
#     def build_board(self):
#         for i in range(self.size**2):
#             x = i % self.size
#             y = i // self.size
#             self.tiles.append(Tile())
#         return board
#
#
#
# board = Boardy(10)
#
# my_board = board.build_board()
# the_board = [my_board.tiles[i*10:i*10+10] for i in range(10)]
#
# for row in the_board:
#     tmp_str = ''
#     for tile in row:
#         tmp_str += tile.sign + ' '
#     print(tmp_str)


# y * w + x

####################################################################################################################
# Alte Funktion safen
# move Player
# def self_move_b(self, my_pos, game_field):  # OK
#     """ Bescheibung:
#
#     Vergleicht die X und Y Position des Spielers, speichert die Richtung, die der Spieler gehn kann,
#     in X und Y und gibt diese zurück
#
#     :param my_pos:
#     :param game_field:
#     :return: y, x, go gibt die Koordinaten X und Y zurück sowie die Richtung(z.b. Norden)
#
#     Details:
#       X Achse
#     Y|0|_|_|
#     A|_|_|_|
#     c|_|_|_|
#     Spieler steht auf X 0 und Y 0 so kann er nur in 3 Richtungen ziehen
#     Bei X 1 und Y 1 wären es 8 Richtungen
#     Bei falschen oder keinen Eingaben wird die Funktion erneut aufgerufen(rekursiv)
#     """
#     y = my_pos[0]
#     x = my_pos[1]
#     max_xy = len(game_field) - 1
#
#     if y == 0 and x == 0:
#         richtung = input('(d) für E, (c) für SE und (x) für S\n')
#         wertung = ['d', 'c', 'x']
#
#     elif y == 0 and x == max_xy:
#         richtung = input('(x) für S, (y) für SE und (a) für W\n')
#         wertung = ['x', 'y', 'a']
#
#     elif y == 0 and 0 < x < max_xy:
#         richtung = input('(d) für E, (c) für SE, (x) für S, (y) für SW und (a) für W\n')
#         wertung = ['d', 'c', 'x', 'y', 'a']
#
#     elif x == 0 and 0 < y < max_xy:
#         richtung = input('(w) für N, (e) für NE, (d) für E, (c) für SE und (x) für S\n')
#         wertung = ['w', 'e', 'd', 'c', 'x']
#
#     elif x == 0 and y == max_xy:
#         richtung = input('(w) für N, (e) für NE, (d) für E\n')
#         wertung = ['w', 'e', 'd']
#
#     elif 0 < x < max_xy and 0 < y < max_xy:
#         richtung = input('(w) für N, (e) für NE, (d) für E, (c) für SE\n'
#                          '(x) für S, (y) für SW, (a) für W und (q) für NW\n')
#         wertung = ['w', 'e', 'd', 'c', 'x', 'y', 'a', 'q']
#
#     elif 0 < x < max_xy and y == max_xy:
#         richtung = input('(w) für N, (e) für NE, (d) für E, (a) für W und (q) für NW\n')
#         wertung = ['w', 'e', 'd', 'a', 'q']
#
#     elif 0 == max_xy and y == max_xy:
#         richtung = input('(w) für N, (a) für W und (q) für NW\n')
#         wertung = ['w', 'a', 'q']
#
#     else:
#         richtung = ""
#         wertung = "error"
#         print(f"self_move keine positions eingabe")  # TEST
#
#     if richtung not in wertung:
#         message_output(features['message']['wrong_entry'])
#         return self.self_move(my_pos, game_field)
#
#     if richtung:
#         if richtung == 'w':
#             y -= 1
#             go = 'Norden'
#
#         elif richtung == 'e':
#             y -= 1
#             x += 1
#             go = 'Nordosten'
#
#         elif richtung == 'd':
#             x += 1
#             go = 'Osten'
#
#         elif richtung == 'c':
#             y += 1
#             x += 1
#             go = 'Südosten'
#
#         elif richtung == 'x':
#             y += 1
#             go = 'Süden'
#
#         elif richtung == 'y':
#             y += 1
#             x -= 1
#             go = 'Südwest'
#         elif richtung == 'a':
#             x -= 1
#             go = 'Westen'
#         elif richtung == 'q':
#             y -= 1
#             x -= 1
#             go = 'Nordwesten'
#         else:
#             go = 'Da ging erwas schief'  # TEST
#     else:
#         go = 'Richtung leer'  # TEST
#
#     return y, x, go
