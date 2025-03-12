class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir_dados(self):
        print("Nome: " + self.nome)
        print("Idade: " + str(self.idade))

    def duplicado(self):
        print("Nome: " + self.nome)
        print("Idade: " + str(self.idade))



