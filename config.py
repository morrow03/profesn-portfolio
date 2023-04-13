import json
def konfigurace():
    file = open('config.json', 'r')
    data = json.load(file)
    dict = {}
    dict['ip'] = data['ip']
    dict['port'] = data['port']
    dict['adresa_start'] = data['adresa_start']
    dict['adresa_konec'] = data['adresa_konec']
    dict['port_start'] = data['port_start']
    dict['port_konec'] = data['port_konec']
    return dict