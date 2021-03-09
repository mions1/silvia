import wikipediaapi

class Wikipedia():


    def __init__(self, page="Silvia"):
        wiki = wikipediaapi.Wikipedia('it')
        self.page = page
        self.__wiki = wiki

    def elaborazione(self):
        pass

    def esecuzione(self):
        self.set_page(self.page)
        pass

    def risposta(self):
        res = ""
        if not self.exist:
            res = "La pagina non esiste simo, I'm sorry"
        else:
            print("Title: " + self.title)
            print("Summary: " + self.summary)
            res = self.title + ": " + self.summary
            res = (res[:150])
        return res

    def run(self):
        self.elaborazione()
        self.esecuzione()
        return self.risposta()

    def set_page(self, page):
        self.page = self.__wiki.page(page[0].capitalize())
        self.exist = self.page.exists()
        if self.exist:
            self.title = self.page.title
            self.summary = self.page.summary