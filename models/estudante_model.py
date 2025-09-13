class Estudante:

    def __init__(self, matricula, nome, idade, nota1, nota2):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (nota1 + nota2) / 2 #Calculo da média das notas