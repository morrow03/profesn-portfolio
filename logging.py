import datetime
def log(zprava):
    '''
    Metoda nact
    :param zprava:
    :return:
    '''
    file = open('log.txt', 'a')
    file.write('{} -> {}'.format(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'), zprava))
    file.write('\n')
    file.close()