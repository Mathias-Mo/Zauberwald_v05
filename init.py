from MyFactory import MyFactory
from player import *
from data import character_props as props
from data import features
from random import shuffle
import time

################################################
"""Beschreibung:    Kleines Spiel

    Das Spiel befindet sich noch in der Entwicklung, allerdings
    kann man schon mit einigen Modulen spielen w.z.b.
    - Autospiel hier kann man zuschauen und muss nix weiter machen
        der Autospielmodus wird mit Game Over beendet
    - Self Spiel
        hier startet der User mit 0 Energie und 0 Ressourcen
         * Resourcen wie Holz und Pflanzen sammeln
         * zu einen Manaschrein gehen und meditieren 
            dieses setzt eine gewisse Anzahl an Ressourcen vorraus
            beim meditieren erhält der User Energie 
                Manna bei einer Magierklasse und
                Stamina bei einer Kriegerklasse 
        
    ausführliche Informationen befinden im doku Ordner
    
"""
# ###### v05 #########################


def game_mod():                                         # ### OK ###
    """Beschreibung:

    Fragt den Spielmodus mit der Funktion auto() ab

    :return: gibt   a für (auto Spiel)
             oder   s für (Spieler spielt) zurück
    """
    game_mode = auto()
    return game_mode


def object_initialization_auto():                       # ### OK ###
    """Beschreibung:

    Hier werden die Objekte initialisiert wie
    das Spielbrett und die K.I. 's
    auch wird ein Spielfeld ersrtellt


    :return: gibt die Objekte zurück und ein Spielfeöd als Liste

    Details:

    Initialisiert das bord Objekt aus der Klasse Board
    Initialisiert 2 zufällige K.I. Objekte aus einer Klassenliste
    mit hilfe der Funktion MyFactory(Klassenname, parameterliste) die auch die Klassen importiert

    Beispiel:
    MyFactory.instanciate('Wizard', character_props['Wizard']['Suny'])
    character_props['Wizard']['Suny'] ergibt eine Liste mit Eigenschaften die bei der Erstellung erforderlich sind
    (Initialiesator(Konstraktor) Wizard)
    desweiteren importiert MyFactory die Klasse Wizard
    """

    # Bord erstellen
    class_name = features['board']['name']
    board1 = MyFactory.instanciate(class_name, features["board"])

    # K.I. Objekt aus den aus den Klassen initialisieren
    # liste der Klassen mischen
    shuffle(features["class"]["class_list"])
    # K.I. 1 erstellen
    class_name = features["class"]["class_list"][0][0]
    ki1 = MyFactory.instanciate(class_name, props[class_name][features["class"]["class_list"][0][1]])
    # K.I. 2 erstellen
    class_name = features["class"]["class_list"][1][0]
    ki2 = MyFactory.instanciate(class_name, props[class_name][features["class"]["class_list"][1][1]])

    game_field = board1.auto_create_board(board1.char)  # zufälliges Speíelfeld erstellen
    return board1, ki1, ki2, game_field   # , 'auto'


def object_initialization_self():       # OK
    """Beschreibung

    wird nur im Spielermodus aufgerufen
    Hier werden die Objekte initialisiert wie
    das Spielbrett die K.I. eine zufällige Klasse aus einer Liste
    der Spieler kann seine Klasse aussuchen und sich einen Namen geben
    auch wird ein Spielfeld ersrtellt


    :return: gibt die Objekte zurück und ein Spielfeöd als Liste

    Details siehe object_initialization_auto()
    """
    # Bord erstellen
    class_name = features['board']['name']
    board1 = MyFactory.instanciate(class_name, features["board"])

    # liste der Klassen mischen
    shuffle(features["class"]["class_list"])
    # K.I. 1 erstellen
    class_name = features["class"]["class_list"][0][0]
    ki1 = MyFactory.instanciate(class_name, props[class_name][features["class"]["class_list"][0][1]])

    # mit der Funktion choose_class() kann der User eine Klasse und ein Namen wählen, eingeben
    # (w), (h) oder (k)
    my_class = choose_class()

    # player 1
    class_name = features['class'][my_class]
    player1 = MyFactory.instanciate(class_name, props[class_name][my_class])
    # message an User, dass Klasse erstellt wurde
    message = props[features['class'][my_class]][my_class]['message']
    message_output(message['create'], player1.name)

    # # board
    game_field = board1.create_board(board1.char_list)

    return board1, ki1, player1, game_field


def start_game_auto():                                 # ### OK
    """Beschreibung

    Hier erhalten beide K.I. 's eine zufällige Position auf dem Spielfed und bewegen sich aufeinander zu


    :return: ki1, ki2, 'ki1' oder 'ki2' zurück
    'ki1' oder 'ki2' wird in der auto_fight() Funktion benötigt, sie bestimmt wer mit dem Kampf anfängt

    """
    # board1, ki1, ki2, game_field in objecte ablegen
    objecte = object_initialization_auto()

    board1 = objecte[0]
    ki1 = objecte[1]
    ki2 = objecte[2]
    game_field = objecte[3]

    pos_ki1 = ki1.place_board(len(game_field))
    pos_ki2 = ki2.place_board(len(game_field))
    # falls die positionen gleich sind funktion nochmal aufrufen
    if pos_ki2 == pos_ki1:
        pos_ki2 = ki2.place_board(len(game_field))
    # beide K.I. s aufs Spielfeld stellen
    game_field[pos_ki1[0]][pos_ki1[1]] = ki1.char_auto
    game_field[pos_ki2[0]][pos_ki2[1]] = ki2.char_auto

    # Message ausgeben
    message_output()
    message_output(ki1.name, 'und', ki2.name, 'betreten das Spielfeld')
    message_output()
    time.sleep(1)
    # Spielfeld und beide K.I. anzeigen
    board1.display_board(game_field)

    #####################################################################
    # ############## move auto ###########################################
    #####################################################################
    while True:
        # K.I.1 (move)
        time.sleep(1)
        # ki1 bewegt sich, neue Position in pos_ki1_neu speichern
        pos_ki1_neu = ki1.auto_move(pos_ki2, pos_ki1)
        # Nachricht anzeigen
        message_output()
        message_output(ki1.char_auto, ki1.name, 'geht nach', pos_ki1_neu[2])
        message_output()
        # bewegungs zeichen auf Karte setzten(Fußspuren)
        game_field[pos_ki1[0]][pos_ki1[1]] = ki1.char_move
        # wenn beide K.I. s noch nicht zusammen getroffen sind weiter bewegen
        if game_field[pos_ki1_neu[0]][pos_ki1_neu[1]] != ki2.char_auto:
            game_field[pos_ki1_neu[0]][pos_ki1_neu[1]] = ki1.char_auto
        else:
            game_field[pos_ki1_neu[0]][pos_ki1_neu[1]] = board1.char_fight
            # Nachricht anzeigen
            message_output(ki2.char_auto, ki2.name, 'beginnt den Kampf')
            message_output()
            time.sleep(1)
            board1.display_board(game_field)
            return ki1, ki2, 'ki2'

        pos_ki1 = pos_ki1_neu
        time.sleep(1)
        # Spielfeld anzeigen
        board1.display_board(game_field)

        # K.I.2 (move)
        if pos_ki2 != pos_ki1:
            pos_ki2_neu = ki2.auto_move(pos_ki1, pos_ki2)
            # msg
            message_output()
            message_output(ki2.char_auto, ki2.name, 'geht nach', pos_ki2_neu[2])
            message_output()
            # bewegungs zeichen auf Karte setzten
            game_field[pos_ki2[0]][pos_ki2[1]] = ki2.char_move

            if game_field[pos_ki2_neu[0]][pos_ki2_neu[1]] != ki1.char_auto:
                game_field[pos_ki2_neu[0]][pos_ki2_neu[1]] = ki2.char_auto
            else:
                game_field[pos_ki2_neu[0]][pos_ki2_neu[1]] = board1.char_fight
                # msg
                message_output(ki1.char_auto, ki1.name, 'beginnt den Kampf')
                message_output()
                # beide anzeigen
                time.sleep(1)
                board1.display_board(game_field)

                return ki1, ki2, 'ki1'

            pos_ki2 = pos_ki2_neu

            # beide anzeigen
            time.sleep(1)
            board1.display_board(game_field)


def start_game_self():
    """Beschreibung

    (kann erweitert werden)
        * Spieler kann sich auf der Karte bewegen
        * 3 Ressourcen können einsammeln werden

    :return:

    Details:
    holt sich die Objekte von der  object_initialization_self() Funktion
    und speichert sie in die Variable objecte
    mit der Funktion place_board() werden die X und Y Achsen in pos_... gespeichert
    falls die Positionen gleich sind wird die Funktion place_board() wieder aufgerufen (recrusiv)
    wenn nicht dann wird der Spieler auf das Spielfeld gesetzt und eine Meldung ausgegeben
    danach wird die Karte angezeigt

    move Spieler
        wird in einer while Schleife verwendet
        jetzt werden alle ressourcen des Spielers angezeigt z.b.
        0|10 Holz 0|10 Sonnengras 0|10 Mondstengel

        1*  mit der Funktion self_move werden die Koordinaten X und Y sowie die Richtung(z.b. Norden)
            in pos_player1_neu gespeichert
            dann wird eine Meldung ausgegeben in welche Richtung der Spieler sich bewegt
            und eine bewegungszeichen(Fußspur) gespeichert

        2*  player1.resource_collect(features['board'][game_field[pos_player1_neu[0]][pos_player1_neu[1]]])
            die Funktion resource_collect(ressourcenname) erfordert einen Ressourcennamen
            game_field[pos_player1_neu[0]][pos_player1_neu[1]] liefert uns das Zeichen welches sich
            auf der tile des Spielfeldes befindet und dieses Zeichen gibt den Ressourcennamen zurück

    """
    # board1, ki1, player1, game_field in objecte ablegen
    objecte = object_initialization_self()

    board1 = objecte[0]
    ki1 = objecte[1]
    player1 = objecte[2]
    game_field = objecte[3]

    # Y X in pos_ki1 und pos_player1 speichern
    pos_ki1 = ki1.place_board(len(game_field))      # # TODO muss später plaziert werden
    pos_player1 = player1.place_board(len(game_field))

    # falls die positionen gleich sind funktion nochmal aufrufen
    if pos_player1 == pos_ki1:
        pos_ki1 = player1.place_board(len(game_field))

        # K.I. aufs Spielfeld stellen
        # game_field[pos_ki1[0]][pos_ki1[1]] = ki1.char_self      # TODO muss später plaziert werden
    else:
        # Spieler aufs Spielfeld stellen
        game_field[pos_player1[0]][pos_player1[1]] = player1.char_self
        message_output()
        message_output(player1.name, 'betritt das Spielfeld')
        message_output()
        # Spieler anzeigen
        board1.display_board(game_field)

        #####################################################################
        # ############## move Spieler ###########################################
        #####################################################################
        test_i = 0
        while True:
            # player1
            message_output()
            # time.sleep(1)
            player1.show_resources()    # zeigt die Ressourcen des Spielers an
            time.sleep(1)
            # Eingabe des Users speichern welche Richtung er geht
            richtung = player1.self_move_input(pos_player1, game_field)
            if not richtung == 'false':

                pos_player1_neu = player1.self_move(pos_player1, richtung)    # 1*

                message_output()
                message_output(f"{player1.char_self}{player1.lives} HP {player1.energy} {player1.energy_name} {player1.name} geht nach {pos_player1_neu[2]}")
                message_output()

                game_field[pos_player1[0]][pos_player1[1]] = player1.char_move

                # übergibt den Tile der funktion resource_collect
                # player1.building_action('manashrine')
                player1.tile_action(features['board'][game_field[pos_player1_neu[0]][pos_player1_neu[1]]])  # 2*
                time.sleep(1)
                # player1.char_self wird auf die neue Position gesetzt
                game_field[pos_player1_neu[0]][pos_player1_neu[1]] = player1.char_self

                pos_player1 = pos_player1_neu
                # Spieler anzeigen
                time.sleep(1)
                board1.display_board(game_field)

                # TEST BREAK
                test_i += 1
                if test_i == 30:
                    break


def auto_fight():                           # ### OK
    """Beschreibung:

    Beide K.I. kämpfen bis eine keine Hitpoins hat, danach kommt eine Siegerauswertung

    :return:

    Details:
    Die Funktion start_game() übergibt an objecte in einem Tuple alle Objekte

    die Objekte werden in
        ki1 = objecte[0]
        ki2 = objecte[1]
        start_name = objecte[2]
    gespeichert
    """
    objecte = start_game_auto()

    ki1 = objecte[0]
    ki2 = objecte[1]
    start_name = objecte[2]

    while True:
        # Kampf Auswertung wenn lives gleich 0 sind die Funktion auto_attack() verhindert das lives unter 0 gehen kann
        if ki1.lives == 0 or ki2.lives == 0:
            if ki1.lives == 0:
                # Nachricht anzeigen
                message_output()
                message_output('***', ki2.name, '*** hat gewonnen')
                message_output()
                game_over()
            elif ki2.lives == 0:
                message_output()
                message_output('***', ki1.name, '*** hat gewonnen')
                message_output()
                game_over()
            break
        ################################################
        # ######################## Kampf ################
        # KI1 beginnt
        if start_name == 'ki1':
            message_output()
            # Funktion auto_attack
            damage = ki1.auto_attack(ki2)
            message_output(ki1.lives, 'HP', ki1.energy, ki1.energy_name, ki1.name, 'trifft', ki2.name, 'mit', damage, 'DMG')
            message_output(ki2.lives, 'HP', ki2.energy, ki2.energy_name, ki2.name)

            time.sleep(1)
            start_name = 'ki2'
        # KI2 beginnt
        elif start_name == 'ki2':
            message_output()
            damage = ki2.auto_attack(ki1)
            message_output(ki2.lives, 'HP', ki2.energy, ki1.energy_name, ki1.name, 'trifft', ki1.name, 'mit', damage, 'DMG')
            message_output(ki1.lives, 'HP', ki1.energy, ki2.energy_name, ki1.name)

            time.sleep(1)
            start_name = 'ki1'


def init():
    game_mode = game_mod()
    if game_mode == 'a':
        object_initialization_auto()
        auto_fight()
    else:
        start_game_self()


if __name__ == '__main__':
    init()
