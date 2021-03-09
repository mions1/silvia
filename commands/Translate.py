from . import Command
from google.cloud import translate_v2 as translate
from commands import builtin as bin

class Translate():
    LANGUAGES = {
        'af': 'africano',
        'sq': 'albanese',
        'ar': 'arabo',
        'hy': 'armeno',
        'bn': 'Bengali',
        'ca': 'catalano',
        'zh': 'cinese',
        'zh-cn': 'Chinese (Mandarin/China)',
        'zh-tw': 'Chinese (Mandarin/Taiwan)',
        'zh-yue': 'Chinese (Cantonese)',
        'hr': 'croato',
        'cs': 'Czech',
        'da': 'Danish',
        'nl': 'tedesco',
        'en': 'inglese',
        'en-au': 'English (Australia)',
        'en-uk': 'English (United Kingdom)',
        'en-us': 'English (United States)',
        'eo': 'Esperanto',
        'fi': 'Finnish',
        'fr': 'French',
        'de': 'German',
        'el': 'Greek',
        'hi': 'Hindi',
        'hu': 'Hungarian',
        'is': 'Icelandic',
        'id': 'Indonesian',
        'it': 'italiano',
        'ja': 'giapponese',
        'ko': 'Korean',
        'la': 'Latin',
        'lv': 'Latvian',
        'mk': 'Macedonian',
        'no': 'Norwegian',
        'pl': 'Polish',
        'pt': 'portoghese',
        'pt-br': 'Portuguese (Brazil)',
        'ro': 'Romanian',
        'ru': 'Russian',
        'sr': 'Serbian',
        'sk': 'Slovak',
        'es': 'spagnolo',
        'es-es': 'Spanish (Spain)',
        'es-us': 'Spanish (United States)',
        'sw': 'Swahili',
        'sv': 'Swedish',
        'ta': 'Tamil',
        'th': 'Thai',
        'tr': 'Turkish',
        'vi': 'Vietnamese',
        'cy': 'Welsh'
    }

    def __init__(self, text):
        self.text = text
        pass

    def elaborazione(self):
        split = self.text.split()
        pre = "come si dice".split()
        self.phrase = " ".join(split[len((self.text[:self.text.index(" ".join(pre))]).split()) + len(pre):-2])
        self.language = split[-1]
        self.lang_tag = self.get_tag(self.language)
        pass

    def esecuzione(self):
        translate_client = translate.Client()

        translation = translate_client.translate(
            self.phrase, target_language=self.lang_tag)
        self.from_lang_tag = translation["detectedSourceLanguage"]
        from_language = self.get_lang(self.from_lang_tag)
        print(u'Language from: {}'.format(from_language + "=" + self.from_lang_tag))
        print(u'Language to: {}'.format(self.language + "=" + self.lang_tag))
        print(u'Text: {}'.format(self.phrase))
        print(u'Translation: {}'.format(translation['translatedText']))

        # s = phrase+" " if len(phrase.split()) < 4 else ""
        # s += "in "+language+" si dice "
        # say(s)
        self.translation = translation['translatedText']
        pass

    def risposta(self):
        return self.phrase+" in "+self.language+" si dice "+self.translation

    def run(self):
        self.elaborazione()
        self.esecuzione()
        return self.risposta()

    def get_tag(self, language="inglese"):
        for key in Translate.LANGUAGES:
            if Translate.LANGUAGES[key] == language:
                return key
        return None

    def get_lang(self, tag="en"):
        return Translate.LANGUAGES[tag]