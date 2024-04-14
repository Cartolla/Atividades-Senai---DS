print("-----------------------------------------------------\n"
      "\t\t\tVAMOS CONTROLAR UMA PESSOA!\n"
      "-----------------------------------------------------\n")

class Pessoa:
    def __init__(self, nome, idade, altura, peso, genero):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.pessoaFalando = False
        self.pessoaAndando = False
        self.pessoaDormindo = False
        self.pessoaComendo = False

    def falar(self):
        if not self.pessoaComendo and not self.pessoaDormindo:
            self.pessoaFalando = True
            print(f"{self.nome} está falando..\n")
            print(f"{self.nome} Falou: \n"
                  f"Oi, meu nome é {self.nome} e minha idade é {self.idade}, meu gênero é {self.genero}, "
                  f"e meu peso é {self.peso}, estou muito feliz por ter sido criada por você :)")

        else:
            print(f"{self.nome} está comendo ou dormindo.")

    def andar(self, destino):
        if not self.pessoaFalando and not self.pessoaDormindo and not self.pessoaComendo:
            self.pessoaAndando = True
            print(f"{self.nome} andou até {destino}.")

        else:
            print(f"{self.nome} está dormindo.")


    def dormir(self, lugar):
        if not self.pessoaFalando and not self.pessoaAndando and not self.pessoaComendo:
            self.pessoaDormindo = True
            print(f"{self.nome} adormeceu em {lugar}.")

        else:
            print(f"{self.nome} está comendo, dormindo ou andando.")

    def comer(self, alimento):
        if not self.pessoaFalando and not self.pessoaAndando and not self.pessoaDormindo:
            self.pessoaComendo = True
            print(f"{self.nome} está comendo {alimento}.")

        else:
            print(f"{self.nome} está andando, dormindo ou falando.")

    def pararcomer(self):
        self.pessoaComendo = False

    def parardormir(self):
        self.pessoaDormindo = False

    def pararandar(self):
        self.pessoaAndando = False

    def pararfalar(self):
        self.pessoaFalando = False

nome = "Lydia"
idade = 17
altura = 1.60
peso = 50.0
genero = "feminino"
pessoa = Pessoa(nome, idade, altura, peso, genero)

while True:

    print("Temos algumas opções, qual deseja?\n"
          "1 - Pessoa Falar\t 5 - Parar Falar\n"
          "2 - Pessoa Andar\t 6 - Parar Andar\n"
          "3 - Pessoa Dormir\t 7 - Parar Dormir\n"
          "4 - Pessoa Comer\t 8 - Parar Comer\n"
          "-------------------\n"
          "9 - Parar de executar\n")

    escolhaMenu = int(input("Digite a opção que deseja: "))

    if escolhaMenu == 1:
        pessoa.falar()

    elif escolhaMenu == 2:
        destino = "itamaraca"
        pessoa.andar(destino)

    elif escolhaMenu == 3:
        lugar = "sofa"
        pessoa.dormir(lugar)

    elif escolhaMenu == 4:
        alimento = "miojo"
        pessoa.comer(alimento)

    if escolhaMenu == 5:
        print("Parou de falar")
        pessoa.pararfalar()

    if escolhaMenu == 6:
        print("Parou de andar")
        pessoa.pararandar()

    if escolhaMenu == 7:
        print("Parou de dormir")
        pessoa.parardormir()

    if escolhaMenu == 8:
        print("Parou de comer")
        pessoa.pararcomer()

    elif escolhaMenu == 9:
        break