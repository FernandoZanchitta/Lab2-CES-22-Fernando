from abc import ABC, abstractmethod


class Solicitacoes(ABC):  # Command
    @abstractmethod
    def execute(self):
        pass


class VerificarSaldos(Solicitacoes):  # Concrete Command
    def __init__(self, conta):
        self.conta = conta

    def execute(self):
        self.conta.verificar_saldo()


class RealizarTransferencias(Solicitacoes):  # Concrete Command
    def __init__(self, conta):
        self.conta = conta

    def execute(self):
        self.conta.realizar_transferencias()


class VerificarExtratos(Solicitacoes):  # Concrete Command
    def __init__(self, conta):
        self.conta = conta

    def execute(self):
        self.conta.verificar_extrato()


class ContaBancaria:  # Receiver
    def verificar_saldo(self):
        print("Verificando Saldo...")

    def verificar_extrato(self):
        print("Verificando Extrato...")

    def realizar_transferencias(self):
        print("Realizando Transferencias...")


class Agente:  # Invoker (Chamador)
    def __init__(self):
        self.__solicitacoes = []

    def executar_pedido(self, pedido):
        self.pedido = pedido
        pedido.execute()


# Cliente

conta = ContaBancaria()
verificar_saldo = VerificarSaldos(conta)
verificar_extrato = VerificarExtratos(conta)
realizar_transferencia = RealizarTransferencias(conta)

# Invoker
agent = Agente()
agent.executar_pedido(verificar_saldo)
agent.executar_pedido(verificar_extrato)
agent.executar_pedido(realizar_transferencia)
