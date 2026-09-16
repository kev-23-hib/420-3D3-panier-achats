from sujet import Sujet

class Panier(Sujet):
    def __init__(self):
        super().__init__() # initilise notre liste d'observateurs
        self._articles = []

    def ajouter_article(self, article) :
        # TODO prendre le code de app.py pour ajouter un article et notifier les observateurs
        pass

    def retirer_article(self, article):
        # TODO prendre le code de app.py pour retirer un article et notifier les observateurs
        pass

    def get_donnees(self) :
        return {
            "articles": self._articles
            }