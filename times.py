from abc import abstractmethod


class TimePadrao:
    time_completo = False
    __time_com_boss = False
    __total_gg = 12
    __msg_auditoria = []
    __krosmasters = []
    fonte_dos_times = []

    def __init__(self, lista):
        self.fonte_dos_times = lista
        self.__krosmasters = []
        self.__msg_auditoria = []
        self.monta_time()

    def add_msg_auditoria(self, msg):
        print(msg)
        self.__msg_auditoria.append(msg)

    def monta_time(self):
        try:
            i = 0
            while self.__total_gg > 0:
                count = sum(x.get('nome') == self.fonte_dos_times[i]['nome'] for x in self.__krosmasters)
                if self.fonte_dos_times[i]['nivel'] <= self.__total_gg and count < self.fonte_dos_times[i]['qtd']:
                    if self.verifica_boss(i):
                        #   boss
                        if self.__time_com_boss:
                            #   não entra boss
                            i += 1
                        else:
                            #   entra boss
                            self.__time_com_boss = True
                            if self.__entra_no_time(i):
                                pass
                            else:
                                i += 1
                    else:

                        #   entra não boss
                        if self.__entra_no_time(i):
                            pass
                        else:
                             i += 1
                else:
                    #   nivel maior que o total de gg
                    self.add_msg_auditoria(
                        '❌ {} maior que {}gg'
                            .format(self.fonte_dos_times[i]['nome'], self.__total_gg))
                    i += 1
        except IndexError:
            self.add_msg_auditoria(
                '💀 ACABOU A LISTA DOS KROS 💀')
            self.__krosmasters = ['']
        if self.total_gg == 0:
            self.time_completo = True

    def __entra_no_time(self, contador):
        if self.__eh_aceitavel(contador):
            self.__krosmasters.append(self.fonte_dos_times[contador])
            self.__total_gg -= self.fonte_dos_times[contador]['nivel']
            self.add_msg_auditoria(
                '✅ {}. Sobram {}gg'.format(self.fonte_dos_times[contador]['nome'], self.__total_gg))
            self.fonte_dos_times.remove(self.fonte_dos_times[contador])
            return True
        else:
            return False

    @abstractmethod
    def verifica_boss(self, contador):
        pass

    def __eh_aceitavel(self, contador):
        return self.verifica_ban(contador) and self.verifica_lista(contador)

    @abstractmethod
    def verifica_ban(self, contador):
        pass

    @abstractmethod
    def verifica_lista(self, contador):
        pass

    @property
    def msg_auditoria(self):
        return self.__msg_auditoria

    @property
    def krosmasters(self):
        return self.__krosmasters

    @property
    def total_gg(self):
        return self.__total_gg

    @property
    def time_com_boss(self):
        return self.__time_com_boss

    @time_com_boss.setter
    def time_com_boss(self, time_com_boss):
        self.__time_com_boss = time_com_boss


class EternalPadrao(TimePadrao):
    estrelasAceitas = []

    def verifica_boss(self, contador):
        if self.fonte_dos_times[contador]['boss_eternal'] == 'boss':
            return True
        else:
            return False

    def verifica_ban(self, contador):
        if self.fonte_dos_times[contador]['eternal'] == 'ban':
            self.add_msg_auditoria(
                '❌ {} é ban'
                    .format(self.fonte_dos_times[contador]['nome']))
            return False
        else:
            return True

    def verifica_lista(self, contador):

        if self.fonte_dos_times[contador]['eternal'] in self.estrelasAceitas:
            return True
        else:
            self.add_msg_auditoria(
                '❌ {} não é das estrelas: {}'
                    .format(self.fonte_dos_times[contador]['nome'], self.estrelasAceitas))
            return False


class EternalUm(EternalPadrao):
    estrelasAceitas = ['1']


class EternalDois(EternalPadrao):
    estrelasAceitas = ['1', '2']


class EternalTres(EternalPadrao):
    estrelasAceitas = ['1', '2', '3']


class TimeSeason(TimePadrao):
    __seasonsAceitas = ['4', '3', '2', '1']

    def verifica_boss(self, contador):
        if self.fonte_dos_times[contador]['boss_season'] == 'boss':
            return True
        else:
            return False

    def verifica_ban(self, contador):
        if self.fonte_dos_times[contador]['season'] == 'ban':
            self.add_msg_auditoria(
                '❌ {} é ban'
                    .format(self.fonte_dos_times[contador]['nome']))
            return False
        else:
            return True

    def verifica_lista(self, contador):
        if self.fonte_dos_times[contador]['season'] in self.__seasonsAceitas:
            return True
        else:
            self.add_msg_auditoria(
                '❌ {} não é das seasons: {}'
                    .format(self.fonte_dos_times[contador]['nome'], self.__seasonsAceitas))
            return False
