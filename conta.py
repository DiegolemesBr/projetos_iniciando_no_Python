

class Conta:
    def __init__(self,numero, titular, saldo, limite):
        print("construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))
        
    def depositar(self,valor):
        self.__saldo += valor
    def pode_sacar(self,valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel
    def sacar(self,valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self,limite):
        self.__limite = limite
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo
    @titular.setter
    def titular(self,titular):
        self.__titular = titular
    @staticmethod
    def Codigo_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
    