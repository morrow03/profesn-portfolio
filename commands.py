import time
import config
import logging
import server
import ipaddress
import client
import socket

class Cmd:
    def __init__(self, klient) -> None:
        self._klient = klient

    def spustit(self, slovicko):
        raise None

class localni_preklad(Cmd):
    def __init__(self, klient) -> None:
        super().__init__(klient)

    def spustit(self, slovicko):
        '''
        metoda se pokusí přeložit dané slovíčko, pokud ho nezná vypíše chybovou hlášku
        :param slovicko: slovíčko, které se má přeložit
        '''
        preklad = self._klient.slovnicek()[slovicko]
        self._klient.poslat('TRANSLATEDSUC"{preklad}"'.format(preklad = preklad))
        logging.log('TRANSLATEDSUC"{preklad}"'.format(preklad = preklad))


class ping(Cmd):
    def __init__(self, klient) -> None:
        super().__init__(klient)

    def spustit(self, slovicko):
        '''
        metoda odpovídá, pokud jí někdo pingne
        :param slovicko: je povinne vyplneni nejakeho slovicka
        '''
        self._klient.poslat('TRANSLATEPONG"Lukas prekladac"')
        logging.log('TRANSLATEPONG"Lukas prekladac"')

class scanovani_site(Cmd):
    def __init__(self, klient) -> None:
        super().__init__(klient)

    def spustit(self, slovicko):
        '''
        Metoda zkouší jednotlivé adresy a porty, dokud nevyčerpá adresy a porty, nebo dokud mu nějaký program neodpoví
        :param slovicko: slovíčko, které chceme přeložit
        '''
        konfigurace = config.konfigurace()
        adresa_start = ipaddress.IPv4Address(server.Server.konfigurace['adresa_start'])
        adresa_aktualni = ipaddress.IPv4Address(server.Server.konfigurace['adresa_start'])
        adresa_konec = ipaddress.IPv4Address(server.Server.konfigurace['adresa_konec'])
        port_start = int(server.Server.konfigurace['port_start'])
        port_aktualni = int(server.Server.konfigurace['port_start'])
        port_konec = int(server.Server.konfigurace['port_konec'])

        cykl = True
        while adresa_aktualni <= adresa_konec and cykl:
            soket = None
            try:
                soket = socket.socket()
                soket.settimeout(0.2)
                soket.connect((str(adresa_aktualni), port_aktualni))
                slovicko_byt = bytes('TRANSLATELOCL"{slovicko}"'.format(slovicko=slovicko), 'utf-8')
                soket.send(slovicko_byt)
                odpoved = soket.recv(70).decode('utf-8')
                if(odpoved[0:13] == 'TRANSLATEDSUC'):
                    self._klient.poslat(odpoved)
                    cykl = False
            except:
                pass
            finally:
                soket.close()

            if(port_aktualni <= port_konec):
                port_aktualni += 1
            if(port_aktualni > port_konec and adresa_aktualni <= adresa_konec):
                adresa_aktualni += 1
                port_aktualni = port_start