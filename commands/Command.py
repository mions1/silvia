from commands.Translate import Translate
from commands.Wikipedia import Wikipedia
from commands.Music import Music
from commands.Event import Event
import pickle, os

class Command:

    TOKEN = "SilvIA/token.pkl"

    def __init__(self):
        pass

    def recognize(self, text):
        """ Check what command is required
        :param text: [string] vocal command
        :return: [string] response to speech
        """
        print(text)

        txt = text.lower()
        if "come si dice" in txt:
            print("Translate")
            translater = Translate(txt)
            return translater.run()

        elif "cerchi" in txt or "cerca" in txt or "cercare" in txt:
            print("Search Engine")
            attrs = Command.get_search_engine_attr(txt)
            if attrs['engine'] == "wikipedia":
                wiki = Wikipedia(attrs["text"])
                return wiki.run()

        elif "musica" in txt or "canzoni" in txt or "canzone" in txt:
            print("Musica")
            music = Music(txt)
            return music.run()

        """
        if "/" in txt or "+" in txt or "-" in txt or "*" in txt:
            fts.compute(txt)
            anything = True




        elif anything == False:
            fts.unknow()
        """

        return False
        pass
    def esecuzione(self):
        pass
    def risposta(self):
        pass

    @staticmethod
    def get_search_engine_attr(text):
        """
        es. "Cerca <topic> su <search_engine>"
        :return:
        """
        attrs = dict()
        split = text.split()

        attrs["engine"] = split[split.index("su") + 1]
        search_words = ["cerca", "cercare", "cerchi", ]
        attrs["search_word"] = [s for s in split if s in search_words][0]

        attrs["text"] = split[split.index("su") + 2:] if split.index("su") == split.index(attrs["search_word"]) + 1 \
            else split[split.index(attrs["search_word"]) + 1:split.index("su")]

        return attrs
