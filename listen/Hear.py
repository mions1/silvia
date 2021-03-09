import speech_recognition as sr
from . import Understand

class Passive:

    def __init__(self, audio_channel=1, engine="google", language="it-IT"):
        self.language = language
        self.audio_channel = audio_channel
        self.engine = engine
        pass

    def run(self):
        r = sr.Recognizer()
        listen = Understand.Understand()

        while True:
            with sr.Microphone(device_index=int(self.audio_channel)) as source:
                print("Say something!")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, phrase_time_limit=8)

            if self.engine == "sphinx" or self.engine == "all":
                # recognize speech using Sphinx
                try:
                    speech = r.recognize_sphinx(audio, language=self.language)
                    print("Sphinx thinks you said " + speech)
                    listen.command_from_speech(speech)
                except sr.UnknownValueError:
                    print("Sphinx could not understand audio")
                except sr.RequestError as e:
                    print("Sphinx error; {0}".format(e))

            if self.engine == "google" or self.engine == "all":
                # recognize speech using Google Speech Recognition
                try:
                    # for testing purposes, we're just using the default API key
                    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                    # instead of `r.recognize_google(audio)`
                    speech = r.recognize_sphinx(audio, language=self.language)
                    print("Google Speech Recognition thinks you said " + speech)
                    listen.command_from_speech(speech)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
        pass