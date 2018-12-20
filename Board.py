from player import message_output
from random import shuffle
from data import features

class Board:
    def __init__(self, params):
        self.size = params['size']
        self.char = params['char']
        self.char_fight = params['char_fight']
        self.char_list = params['char_list']

    # ################################# Methods ##################################
    def create_board(self, my_feld):            # OK
        """Beschreibung:

        Erstellt das Spielfeld als Liste


        :param my_feld: ist eine Liste mit Zeichen die als Gebäude oder Ressourcen dienen
        :return: gibt eine Liste zurück

        Details:
        Der User wird aufgefordert eine Spielfeldgröße zu wählen
        Die Eingabe wird dann überprüpft
        wenn alles ok ist:
            wird die liste my_feld(Parametereingabe) mit hilfe von shuffle() gemischt
            danach wird mit List comprehension eine 2d Liste erstellt
            diese wird dann mit shuffle gemischt ohne diese 2. Mischung würden Muster entstehen
            diese Liste wird dann zurückgegeben
        falls die Angaben nicth ok sind:
            ruft sich die Funktion wieder auf(rekrusiv)
        """

        i_size = input(features['board']['message']['size'])

        if i_size == 's' or i_size == 'm' or i_size == 'b':
            # my_feld = [chr(882), chr(882), '#', chr(127799), chr(127799), '#', chr(9962), chr(882), chr(127799)]
            shuffle(my_feld)

            my_list = [[my_feld[(i + 1 + j) % len(my_feld)] + '\t'
                        for i in range(0, self.size[i_size])]
                       for j in range(0, self.size[i_size] * self.size[i_size], self.size[i_size])]

            shuffle(my_list)
            for sublist in my_list:
                shuffle(sublist)

            return my_list
        else:
            return self.create_board(my_feld)

    def auto_create_board(self, char):      # ok
        """Beschreibung:


        Erstellt zufällige 2d Liste für das Spielfeld im Automodus

        :param char:  Zeichen die in der Liste zu sehen sind (|_|_|)
        :return: gibt die Liste zurück

        Details:
        Eine Liste von Zahlen wird in der Variablen my_list übergeben
        diese werden mit shuffle() gemischt, dort wird die erste Zahl in a_size gespeichert
        danach wird mit for eine 2d Liste erstellt und zurückgegeben

        """
        my_list = list(features['board']['size'])
        shuffle(my_list)

        a_size = my_list[0]
        my_board = []
        for i in range(self.size[a_size]):
            my_board.append([char] * self.size[a_size] + ['|'])

        return my_board

    def display_board(self, my_board):  # OK
        """Beschreibung

        Dient zur Anzeige des Spielfeldes

        :param my_board: eine 2d Liste
        :return: None

        Details:
        es werden die einzelnen Listen als Zeilen dargestellt
        """
        for row in range(len(my_board)):
            print(' '.join(my_board[row]))

    # ################################# Getter Setter ############################
