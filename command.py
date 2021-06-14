from abc import ABC, abstractmethod


class Order(ABC): #Command

    @abstractmethod
    def execute(self):
        pass

class BankBalance(Order): #ConcreteCommand
    def __init__(self,bank_account):
        self.bank_account=bank_account
    
    def execute(self):
        self.bank_account.getMyBalance()

class BankStatement(Order): #ConcreteCommand
    def __init__(self,bank_account):
        self.bank_account=bank_account
    
    def execute(self):
        self.bank_account.getMyStatement() 

class BankTransference(Order): #ConcreteCommand
    def __init__(self,bank_account):
        self.bank_account=bank_account
    
    def execute(self):
        receiver=input('Digite a conta que receberá a transferência:\n')
        value=float(input('Digite o valor da transferência:\n'))
        password=input('Digite sua senha:\n')
        self.bank_account.makeOneTransfer(receiver,value,password)

class BankAppAccount: #Receiver

    def __init__(self,balance,bank_statement,password):
        self.balance=balance
        self.bank_statement=bank_statement
        self.password=password
    
    def getMyBalance(self):
        print('\n\nSeu saldo é {:.2f}\n\n'.format(self.balance))
        wait=input('Aperte uma tecla para continuar...\n')
        print('\n\n\n')
    
    def getMyStatement(self):
        print(50*'-')

        print('\nExtrato Bancário\n')

        print(50*'-')


        for transaction in self.bank_statement:
            print('\n'+transaction+'\n')

        print(50*'-')
        wait=input('Aperte uma tecla para continuar...\n')
        print('\n\n\n')

    def makeOneTransfer(self,receiver,value,password):

        if self.password==password:
            if value < self.balance:
                self.balance-=value
                self.bank_statement.append('Transferência de R$ {:.2f} para a conta {}.'.format(value,receiver))
            else:
                print('\nVocê não possui saldo para realizar essa transação.\n')
        else:
            print('\n'+'Senha Rejeitada'+'\n')
        
        wait=input('Aperte uma tecla para continuar...\n')
        print('\n\n\n')

class Agent: #Invoker (chamador)
    def __init__(self):
        self.__order_queue=[]
    
    def place_order(self,order):
        self.__order_queue.append(order)

    def execute_order(self):
        while self.__order_queue:
            self.order=self.__order_queue.pop(0)
            self.order.execute()
            



#Cliente


#Informações da conta do cliente

balance=1557.90 #A conta do cliente comecará com 1557 reais e 90 centavos
statement=['Transferência de R$ 67.00 para a conta 12321-3',
           'Transferência de R$ 50.00 para a conta 78245-8'] #O histórico bancário
password='123456789' #A senha

#Criação da conta do cliente
client_account=BankAppAccount(balance,statement,password)


#Possíveis Requisições do Cliente
get_balance_order=BankBalance(client_account)
make_a_transfer_order=BankTransference(client_account)
get_statement_order=BankStatement(client_account)

#Invoker:

agent=Agent()


#Colocando as acões na lista de ordens
agent.place_order(get_balance_order)
agent.place_order(make_a_transfer_order)
agent.place_order(get_statement_order)
agent.place_order(get_balance_order)

#Executando as ordens
agent.execute_order()





