
# 1. rimango sempre in ascolto tramite hear
# 2. quando sento qualcosa, lo mando a "understand"
# 3. se understand rileva che sto parlando con SilvIA, chiama prima i comandi built-in. Se non è un built-in, chiama command
# 4. command elabora la domanda per capire a chi compete e, se trova, restituisce la classe giusta
# 5. la classe, a seconda della richiesta, darà la rispota/farà l'azione

import speech_recognition as sr
import sys, os, argparse

default_engine = "google"
default_lang = "it"
default_idx = 6
default_mode = "audio"  # text or audio

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity. FIXME: add levels", action="store_true", default=False)
    parser.add_argument("-t", "--text", type=str, help="textual command", default="")
    parser.add_argument("-l", "--lang", type=str, help="id language to speak. default: "+default_lang, default=default_lang)
    parser.add_argument("--idx", type=int, help="audio input index. default: "+str(default_idx), default=default_idx)
    parser.add_argument("--engine", type=str, help="audio recognizer engine. default: "+default_engine, default=default_engine)
    parser.add_argument("-m", "--mode", help="mode to interact. default: "+default_mode, default=default_mode)
    args = parser.parse_args()
    return args

parser = args()

engine = parser.engine
lang = parser.lang
index = parser.idx
mode = parser.mode

text = "Cosa devo fare oggi"
text = "che ore sono"

parser = args()

#lang = "it"
#mode = "text"


# init
os.system("export GOOGLE_APPLICATION_CREDENTIALS=/home/ubuntu-simone/Development/Git/SilvIA/silvia-44915d55b3ef.json")

# obtain audio from the microphone
r = sr.Recognizer()

understand = under.Understand()

if mode == "audio":

    #hear = Hear(audio_channel=default_idx, engine=default_engine, language=default_lang)
    #hear.run()

    while True:
        with sr.Microphone(device_index=int(index)) as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=8)

        if engine == "sphinx" or engine == "all":
            # recognize speech using Sphinx
            try:
                print("Sphinx thinks you said " + r.recognize_sphinx(audio, language="it-IT"))
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
                #fts.unknow()
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

        if engine == "google" or engine == "all":
            # recognize speech using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                text = r.recognize_google(audio, language="it-IT")
                print("Google Speech Recognition thinks you said " + text)
                # FIXME: Do something
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                #fts.unknow()
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

else:
    while True:
        text = input("")
        # TODO: Do something
