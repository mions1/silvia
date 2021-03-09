import datetime
from datetime import date
from googleapiclient.discovery import build
from commands.builtin import Builtin as bin

class Event():
    """

    NEXT: Informazioni sui prossimi impegni da calendario.
    Puoi richiedere gli impegni odierni o di domani.
    es. "Che devo fare oggi?"

    SEARCH: Informazioni riguardo un particolare evento.
    es. "Quando ho parrucchiera?"

    TODO: CREATE: Crea un evento

    """
    NEXT = 1
    SEARCH = 2
    CREATE = 3

    def __init__(self, text, credentials, function=NEXT, date=datetime.datetime.utcnow().isoformat(), max_results=10, **kwargs):
        self.text = text
        self.function = function
        self.date = date
        self.__credentials = credentials
        self.__service = build("calendar", "v3", credentials=self.__credentials)
        self.wanted_events = None
        self.now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    def elaborazione(self):
        if self.function == Event.NEXT:
            today = date.today()
            self.wanted_date = today
            self.day = "oggi"
            if "domani" in self.text:
                tomorrow = (datetime.datetime.now() + datetime.timedelta(1)).strftime('%Y-%m-%d')
                self.wanted_date = tomorrow
                self.day = "domani"


        elif self.function == Event.SEARCH:
            self.service = build("calendar", "v3", credentials=self.__credentials)

            split = self.text.split()
            self.phrase = " ".join(split[split.index("quando") + 2:])
            print(self.phrase)


        elif self.function == Event.CREATE:
            pass


    def esecuzione(self):
        if self.function == Event.NEXT:
            print('Sto prendendo i prossimi 10 eventi')
            s = "Solo un attimo che controllo."
            bin.say(s)

            events_result = self.__service.events().list(calendarId='primary', timeMin=self.now, maxResults=20,
                                                         singleEvents=True, orderBy='startTime').execute()
            events = events_result.get('items', [])
            self.wanted_events = []

            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                try:
                    rel = start[:start.index("T")]
                    self.time = start[start.index("T") + 1:start.index(":") + 3]
                except ValueError:
                    rel = start
                    self.time = "per tutto il giorno"

                if rel == str(self.wanted_date):
                    self.wanted_events.append(event)

        elif self.function == Event.SEARCH:
            print('Sto prendendo i prossimi eventi')
            s = "Just a moment please\n"
            bin.say(s)

            events_result = self.service.events().list(calendarId='primary', timeMin=self.now, maxResults=50,
                                                       singleEvents=True, orderBy='startTime').execute()
            events = events_result.get('items', [])
            self.wanted_events = []

            for event in events:
                summ = event['summary']
                if summ.lower() in self.phrase:
                    self.wanted_events.append(event)

        elif self.function == Event.CREATE:
            pass


    def risposta(self):
        if self.function == Event.NEXT:
            if not self.wanted_events:
                print("Nessun evento per " + self.day)
                s = "Nessun impegno per " + self.day + ". Si sbocciaa!!"
                return s
            else:
                print(self.day + " hai ")
                s = self.day + " hai: \n"
                for ev in self.wanted_events:
                    print("alle " + self.time + " " + ev["summary"])
                    s += "alle " + self.time + " " + ev["summary"] + "\n"
                return s

        elif self.function == Event.SEARCH:
            if not self.wanted_events:
                print("Nessun impegno del genere.")
                s = "Non mi risulta come impegno."
                return s
            else:
                print("Hai: \n")
                s = "Hai "
                for ev in self.wanted_events:
                    try:
                        start = ev['start'].get('dateTime', ev['start'].get('date'))
                        day = ((start[:start.index("T")])).split("-")
                        day[0], day[1] = day[2], day[1]
                        day = "/".join(day[:2])
                        time = start[start.index("T") + 1:start.index(":") + 3]
                    except ValueError:
                        print(ev)
                        time = "per tutto il giorno"
                    s += "il " + day + " alle " + time + " " + ev["summary"] + "\n"
                    print(s)
                return s

        elif self.function == Event.CREATE:
            pass

    def run(self):
        self.elaborazione()
        self.esecuzione()
        return self.risposta()


    def create(self, title, when, location="", how_much=1, description=""):
        when = '2015-05-28T17:00:00-07:00'
        event = {
            'summary': title,
            'location': location,
            'description': description,
            'start': {
                'dateTime': when,
                'timeZone': 'Italia/Rome',
            },
            'end': {
                'dateTime': when+how_much,
                'timeZone': 'Italia/Rome',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 60},
                ],
            },
        }

        #event = self.__service.events().insert(calendarId='primary', body=event).execute()
        print(event)

        pass