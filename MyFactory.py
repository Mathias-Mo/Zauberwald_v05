import importlib


class MyFactory:
    """Beschreibung:

    Klassen werden automatisch importiert
    class_name  Class name der in der Datei steht
    props       eine Liste der Eigenschaften

    Details:
        Beispiel:
        MyFactory.instanciate('Wizard', character_props['Wizard']['Suny'])
        character_props['Wizard']['Suny'] ergibt eine Liste mit Eigenschaften die bei der Erstellung erforderlich sind
        (Initialiesator(Konstraktor) Wizard)
    """

    @staticmethod
    def instanciate(class_name, props):

        module_ = importlib.import_module(class_name)
        class_ = getattr(module_, class_name)
        return class_(props)
