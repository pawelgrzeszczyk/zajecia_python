# Napisz klase, ktora bedzie przechowywac adresy e-mail. Konstruktor ma przyjmowac napis, bedacy adresem.
# Jesli zostanie podany niewlasciwy adres, konstruktor ma zglaszac wyjatek odpowiedniej klasy.
import re

class AdresEx(Exception):
    pass


class Adres(object):
    mail = None

    def __init__(self, mail):

        regex_email = re.compile(
            r'''(?P<adres>
              (?P<login>[\w+.]+)      # login, np. m.j.panczyk+umcs.pl
              @                       # znak @
              (?P<domena>\w+(\.\w+)+) # domena, np. gmail.com
            )''',
            re.IGNORECASE | re.VERBOSE
        )

        if re.match(regex_email, mail):
            print mail
            self.mail = mail
        else:
            raise AdresEx("wyjatek - niepoprawny adres")

try:
    a = Adres("adssd@onet.pl")
except Exception as ex:
    print ex


