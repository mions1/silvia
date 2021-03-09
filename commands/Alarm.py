from commands.builtin import Builtin as bin
import os
from datetime import date

# FIXME: IMPLEMENTA

class Alarm():

    def __init__(self, text):
        self.text = text
        self.tra_numero = None
        self.tra_oreminuti = None
        self.alle_ore = None
        self.alle_minuti = None
        pass

    def elaborazione(self):
        split = self.text.split()
        if "tra" in self.text:
            self.tra_numero = split[self.text.index("tra")+1]
            self.tra_oreminuti = split[self.text.index("tra")+2]
        elif "alle" in self.text:
            self.alle_ore = split[self.text.index("alle")+1]
            self.alle_minuti = split[self.text.index("alle")+3]

    def esecuzione(self):
        if self.alle_ore:
            alarm = date.ctime()

        pass

    def risposta(self):
        return ""

    def run(self):
        self.elaborazione()
        self.esecuzione()
        return self.risposta()