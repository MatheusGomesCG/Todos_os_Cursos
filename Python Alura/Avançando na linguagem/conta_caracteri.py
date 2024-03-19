class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        mensagem = f"O Saldo do {self.__titular} é R${self.__saldo:.2f}"
        print(mensagem.replace(".",","))
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @staticmethod
    def contaTitular():
        print("001")