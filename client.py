import socket
import re
import commands
import time
import logging


class Klient:
    def __init__(self, socket, adresa, server):
            '''
            vytvoření klienta
            :param socket: socket uživatele
            :param adresa: adresa uživatele
            :param server: odkaz na server
            '''
            self._socket: socket.socket = socket
            self._adresa_port: tuple = adresa
            self._server = server
            self._cmd = {
                'TRANSLATELOCL': commands.localni_preklad(self),
                'TRANSLATESCAN': commands.scanovani_site(self),
                'TRANSLATEPING': commands.ping(self)
            }

    def klient_prikaz(self):
            '''
            program zkontroluje příkaz a pokusí se ho přeložit, pokud je příkaz správně zapsán, pokusí se ho přeložit. V opačném případě vypíše neznámý příkaz
            '''
            cmd = self._socket.recv(128).decode('utf-8').strip()
            result = re.match(r'^([A-Z]+)"(.+)"$', cmd)
            if result is not None and result.group(1) in self._cmd:
                self._cmd[result.group(1)].spustit(result.group(2))
            else:
                logging.log('TRANSLATEDERR"NEZNAMY PRIKAZ"')
                self.poslat('TRANSLATEDERR"NEZNAMY PRIKAZ"')
            time.sleep(0.001)
            self._socket.close()

    def poslat(self, zprava):
        '''
        metoda překoduje zpravu (utf-8) a zavolá metodu na odeslání
        :param zprava: zpráva pro uživatel
        '''
        zprava_bytes = bytes(zprava, 'utf-8')
        self._socket.send(zprava_bytes)

    def slovnicek(self):
        '''
        Metoda vrací slovníček daného serveru
        :return: slovníček
        '''
        return self._server._slovnicek