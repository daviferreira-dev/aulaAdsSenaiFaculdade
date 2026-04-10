class Pessoa:
    def __init__(self, nome:None, idade:None): #Construtora
        if nome is None: 
            nome = input("Digite seu nome: ")
        if idade is None: 
            idade = int(input("Digite sua idade: "))
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá {self.nome} você tem {self.idade}")     

# pessoa1 = Pessoa("Jão", 18)
# pessoa1.apresentar()
pessoaRandom = Pessoa("Ana", 21)
pessoaRandom.apresentar()
pessoa1 = Pessoa()
pessoa1.apresentar()