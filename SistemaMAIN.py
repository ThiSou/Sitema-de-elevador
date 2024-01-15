import time
import os

# o peso das pessoas foi definido como 100 kg 
# limite de pessoas no elevador de 10 pessoas 
# limite de peso do elvador de 1000kg
# o codigo começa interpretando que sempre a 5 pessoas no elevador e que todas elam pesam 60kg
# o atributo de peso maximo automaticamente faz o calculo do peso de todas as pessoas no elevador, levando em consideração o topico acima, o peso atual do elevador é 300kg
# o predio em questão so possui 10 andares, logo quando escolhem o andar 11 acima ou -1 abaixo, o "tratamento de erro" é retornado pelo metodo tratamentoDeErro


# Classe 
class Elevador: 
    # Objeto
    def __init__(self, andarAtual:int, andarDeChegada:int):
        #atributos 
        self.quantidadeDePessoas = 5
        self.pesoAtual = self.quantidadeDePessoas * 60
        self.andarAtual = andarAtual
        self.andarDeChegada = andarDeChegada
        self.pesoMaximo = 1000
        self.ultimoAndar = 10
        self.primeiroAndar = 0 

        # Metodo para de verificação se o elevador pode subir 
    
    def verificacaoParaSubir(self):
        """
        metodo utilizado para verificar se o elevador está cumprindo com as regras para a movimentação, utilizando as estruturas condicionais para ver se ultrapassa o limite de pessoas, o limite de peso e se o andar atual é diferente do andar que as pessoas desejam ir.
        """
        if self.pesoAtual > self.pesoMaximo:
            return False
        if self.quantidadeDePessoas > 10:
            return False
        if self.andarAtual == self.ultimoAndar:
            return False
        if self.andarAtual > self.ultimoAndar:
            return False
        if self.andarDeChegada > self.ultimoAndar:
            return False
        if self.andarDeChegada < self.andarAtual:
            return False
        return True
    
    # Metodo para de verificação se o elevador pode descer 
    
    def verificacaoParaDescer(self):
        """
         metodo utilizado para verificar se o elevador está cumprindo com as regras para a movimentação, utilizando as estruturas condicionais para ver se ultrapassa o limite de pessoas, o limite de peso e se o andar atual é diferente do andar que as pessoas desejam ir.
        """
        if self.pesoAtual > self.pesoMaximo:
            return False
        if self.quantidadeDePessoas > 10:
            return False
        if self.andarAtual == self.primeiroAndar:
            return False
        if self.andarDeChegada < self.primeiroAndar:
            return False
        if self.andarDeChegada > self.ultimoAndar:
            return False
        return True
    
    
    # metodo para descer 
    def subir(self):
        """
        Esse metodo simula o movimento de subida de um elevador, com aviso de abrimento e fechamento das portas e validações verificando o andar atual e o andar de chegada
        """
        for andar in range(self.andarAtual, self.andarDeChegada):
          print(f'{self.andarAtual} ↑')
          self.andarAtual += 1
          time.sleep(2)
          os.system('cls')

          if self.andarAtual == self.andarDeChegada:
            os.system('cls')
            print(f'{self.andarAtual} --')
            time.sleep(1)
            os.system('cls')
            print('Você chegou ao seu destino.')
            time.sleep(2.5)
            os.system('cls')
            self.andarAtual = self.andarAtual

            for i in range(5):
              print('\033[32;1m ← →\u001b[0m')
              time.sleep(0.8)
              os.system('cls')

            for i in range(5):
              print('\033[31;1m → ←\u001b[0m')
              time.sleep(0.8)
              os.system('cls')

      
    #metodo para subir
    def descer(self):
        """
       Esse metodo simula o movimento de descida de um elevador, com aviso de abrimento e fechamento das portas e validações verificando o andar atual e o andar de chegada
        """
       #validação com o metodo de verificação
        for andar in range(self.andarAtual, self.andarDeChegada, -1):
            print(f'{self.andarAtual} ↓')
            self.andarAtual -= 1
            time.sleep(2)
            os.system('cls')

        if self.andarAtual == self.andarDeChegada:
            os.system('cls')
            print(f'{self.andarAtual} --')
            time.sleep(1)
            os.system('cls')
            print('Você chegou ao seu destino.')
            time.sleep(2.5)
            os.system('cls')
            self.andarAtual = self.andarAtual

            for i in range(5):
                print('\033[32;1m ← →\u001b[0m')
                time.sleep(0.8)
                os.system('cls')

            for i in range(5):
                print('\033[31;1m → ←\u001b[0m')
                time.sleep(0.8)
                os.system('cls')

        
       
    def tratamentoDeErro(self):
            """
            Metodo responsável pelo tratamento de erro, caso uma das regras do elevador sejá quebrada, o retorno do metodo subir ou descer retornará o erro no terminal.
            """
            print( f'''Verificação de regras
            Peso maximo: 1000kg
            Peso Atual: {pessoas.pesoAtual}kg
            Limite de pessoas: 10 pessoas
            Quantidade Atual: {pessoas.quantidadeDePessoas} pessoas
            Andar Atual: {pessoas.andarAtual}º andar''' )
            
          

andarAtual = 0

while True: 
    andarParaIr = int(input(' 1 2 3\n 4 5 6\n 7 8 9\n  10\n  '))
    os.system('cls') 
    pessoas = Elevador(andarAtual, andarDeChegada=andarParaIr)
    if pessoas.verificacaoParaSubir():
        pessoas.subir()
        andarAtual = andarParaIr
    elif pessoas.verificacaoParaDescer():
        pessoas.descer()
        andarAtual = andarParaIr
    else:
        pessoas.tratamentoDeErro()