from commands.builtin import Builtin as bin
import os


class Music():

    def __init__(self, text):
        self.text = text
        self.state = os.system("pgrep mpv")
        self.say = ""
        pass

    def elaborazione(self):
        if "metti" in self.text or "mettere" in self.text:
            if self.state == 0:
                self.say = "La faccio ripartire subito"
                bin.say(self.say)
                os.system("kill -CONT $(pgrep mpv)")
            else:
                self.say = "Okay, metto subito qualcosa "+bin.getName()
                bin.say(self.say)
                os.system("mpv /home/ubuntu-simone/Musica/downloaded/* &")
        elif "togli" in self.text or "spegni" in self.text:
            if self.state == 0:
                self.say = "La tolgo subito "+bin.getName()
                bin.say(self.say)
                os.system("kill -STOP $(pgrep mpv)")
            else:
                self.say = "Drogato, la musica già non c'è"
                bin.say(self.say)

    def esecuzione(self):
        pass

    def risposta(self):
        return ""

    def run(self):
        self.elaborazione()
        self.esecuzione()
        return self.risposta()