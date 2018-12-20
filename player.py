from data import features
from data import character_props as probs


def message_output(*args):          # OK
    """Beschreibung:

    dient zur Znzeige von Nachrichten

    :param args:
    :return: None

    Details:
    Alle Nachrichten die als Parameter(*args) eingegeben wurden
    werden mit hilfe der for Schleife in result gespeichert und dann per print(result) ausgegeben
    """
    result = ""
    for arg in args:
        result += str(arg) + " "
    print(result)


def get_valid_name():               # OK
    """Beschreibung:

    Foirdert den User auf einen Namen einzutragen und
    Überprüfung ob etwas vom User eingegeben wurde
    Falls keine Eigabe, leerzeichen oder ein zu langer name, eigegeben wurde
        ruft sicht die Funktion wieder auf(rekrusiv)


    :return: name des Users
    """
    name_player = input(f'gib einen Namen ein\n')
    if not name_player:
        print('Keine Eingabe, versuch es nocheinmal')
        return get_valid_name()
    elif name_player.strip() == '':
        print('Du hast keine Buchstaben eingegeben')
        return get_valid_name()
    elif len(name_player) > 20:
        print('Name ist zu lang')
        return get_valid_name()
    else:
        return name_player


def greeting():             # OK
    """Beschreibung:

    Dient zum besonderen aussehen

    :return: gibt die eingegebenen Zeichen decodiert aus

    Details:

    print(b'\xe2\x95\x94'.decode('utf-8')) ergibt ╔ die linke obere Ecke
    print(b'\xe2\x95\x91'.decode('utf-8')) ergibt ║
    somit lassen sich "Rahmen bauen"
    """

    dic = {
    '\\' : b'\xe2\x95\x9a',
    '-'  : b'\xe2\x95\x90',
    '/'  : b'\xe2\x95\x9d',
    '|'  : b'\xe2\x95\x91',
    '+'  : b'\xe2\x95\x94',
    '%'  : b'\xe2\x95\x97',
    }

    def decode(x):
        return (''.join(dic.get(i, i.encode('utf-8')).decode('utf-8') for i in x))

    print(decode('+--------------------------------------%'))
    print(decode('|   Willkommen bei uns im Zauberwald   |'))
    print(decode('\\--------------------------------------/'))


def game_over():                # OK
    """Beschreibung:
    ist das Spiel beendet soll eine Ausgabe erscheinen



    :return: gibt die eingegebenen Zeichen decodiert aus

    Details:
    siehe greeting() Funktion
    """

    dic = {
    '\\' : b'\xe2\x95\x9a',
    '-'  : b'\xe2\x95\x90',
    '/'  : b'\xe2\x95\x9d',
    '|'  : b'\xe2\x95\x91',
    '+'  : b'\xe2\x95\x94',
    '%'  : b'\xe2\x95\x97',
    }

    def decode(x):
        return (''.join(dic.get(i, i.encode('utf-8')).decode('utf-8') for i in x))

    print(decode('+-------------------------------------%'))
    print(decode('|              Game Over              |'))
    print(decode('\\-------------------------------------/'))


def auto():             #OK
    """Beschreibung

    Hier kann der User zwischen
    (a) das Spiel läuft dann eigenständig ab und endet mit Game Over
    oder
    (s) hier kann der User selber spielen
    wählen


    :return: a, s oder funktion neuaufruf(rekrusion)

    Details:

    Zuerst wird mit hilfe der Funktion greeting() eine besonderes Willkommen angeziegt
    danach wird der user aufgefordert (a) oder (s) einzugeben
    ist die Eingabe korrekt wird a oder s zurückgegeben
    ist die Eingabe anders ruft sich die Funktion wieder auf(rekrusion)
    """

    greeting()
    game_mode = input(f"{features['message']['game_mode']}\n")
    if game_mode == 'a' or game_mode == 's':
        return game_mode
    else:
        return auto()


def choose_class():     #ok
    """Beschreibung

    Der User kann hier eine Spieler Klasse auswählen

    :return: gibt den Klassen namen zurück

    Details:
    User wird aufgefordert sich eine Spielerklasse auszuwählen
        ist die ausgewählte Klasse in der Liste
        wird der User mit der Funktion get_valid_name(), aufgeforder einen Namen einzugeben
    bei einer falschen Eingabe, erscheint eine fehler Meldung und die Funktion ruft sich wieder auf
    """
    class_name = input(f'Bitte ein Klasse wählen:\n{", ".join(features["class"]["all_class"])}\n')
    if class_name in features["class"]:
        name_player = get_valid_name()
        probs[features["class"][class_name]][class_name]['name'] = name_player
    else:
        print('falsche Eingabe, versuch es bitte noch einmal')
        return choose_class()

    return class_name




