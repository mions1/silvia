from datetime import datetime
import random
from gtts import gTTS
import sys, os

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


class Builtin():
    """ Handle built-in action, as greetings or what time is it and so on

    """

    # Names which Silvia can call me
    # TODO: you can add weight, or categories (maybe categories are better)
    NAME = ["Simo", "Simone",
            "Tesoro", "Carissimo", "Bellissimo", "amò",
            "zì", "zio", "ci",
            "signorino", "capo",
            "tossico",
            ]

    def __init__(self, text):
        """
        :param text: [string] vocal command
        """
        self.text = text.lower()
        pass

    def recognize_and_execute(self):
        """ Check if text is a built-in command. If it is, execute!
        :return: [bool] True if it is a built-in command, False otherwise
        """
        if self.greetings():
            return self.greet()
        if self.whattimeisit():
            return Builtin.current_time()
        else:
            return False

    def greetings(self):
        """ Check if command is a greet
        :return: True if it is, False otherwise
        """
        if "ciao" in self.text.split()[0] or \
                "Silvia ciao" in self.text or \
                "Tesoro ciao" in self.text:
            return True
        return False

    def whattimeisit(self):
        """ Check if command is what time is it
        :return: True if it is, False otherwise
        """
        if "che ore sono" in self.text or \
                "che ora è" in self.text:
            return True
        return False

    @staticmethod
    def greet():
        """ Handle greet response
        :return: [string] a random greet
        """
        greets = ["Ciao", "Ciao Simo", "Ciao love",
                  "Ciao carissimo", "Bella zì",
                  ]
        return random.choice(greets)

    @staticmethod
    def current_time():
        """ Handle what time is it response. Get current time in a speaking format
        :return: [string] current time to say (es. "Sono le <ore> e <minuti>")
        """
        now = datetime.now()
        hour = now.strftime("%H")
        minute = now.strftime("%M")
        return "Sono le " + str(hour) + " e " + str(minute)

    @staticmethod
    def unknown():
        """ Handle when Silvia doesn't know how to reply
        :return: [string] a random unknown response
        """
        unknow = ["Non ho capito "+Builtin.getName()+", ripeti per favore",
                  "Non so come farlo "+Builtin.getName(),
                  "Dovresti aggiornarmi "+Builtin.getName()+", non lo sò fare",
                  ]
        return random.choice(unknow)

    @staticmethod
    def say(text, lang="it"):
        """ TTS.
        Create a file.mp3 with text and play it
        :param text: [string] text to speech
        :param lang: [string] speech language tag (es. it)
        :return: None
        """
        if text == "" or type(text)=="bool":
            return
        file = "file.mp3"
        tts = gTTS(text, lang, slow=False)
        print("Saying "+text)
        tts.save(file)
        os.system("mpg123 " + file)

    @staticmethod
    def getName():
        """ Get a random name from NAMES
        :return: [string] a random name
        """
        return random.choice(Builtin.NAME)