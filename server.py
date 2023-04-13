import socket
import client
import threading
import config

class Server:
    konfigurace = config.konfigurace()

    def __init__(self):
        '''
        založení serveru
        '''
        ip_adresa = Server.konfigurace['ip']
        port = Server.konfigurace['port']
        adresa_start = Server.konfigurace['adresa_start']
        adresa_konec = Server.konfigurace['adresa_konec']
        port_start = Server.konfigurace['port_start']
        port_konec = Server.konfigurace['port_konec']
        self._socket: socket.socket() = socket.socket()
        self._adresa_port: tuple = (ip_adresa, port)
        self._run = False
        self._slovnicek = {
            'I': 'já',
            'you': 'ty',
            'he': 'on',
            'she': 'ona',
            'it': 'ono',
        }

    def server_start(self):
        '''
        server se zapne a dokud program beží, přijímá klienty a komunikuje s nimi
        '''
        self._socket.bind(self._adresa_port)
        self._socket.listen()
        self._run = True
        while self._run:
                klient_socket, klient_adresa = self._socket.accept()
                klient = client.Klient(klient_socket, klient_adresa, self)
                thread = threading.Thread(target = klient.klient_prikaz)
                thread.start()
        self._run = False