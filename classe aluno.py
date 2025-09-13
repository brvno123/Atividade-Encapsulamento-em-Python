class Aluno:
    def __init__(self, nome, nota=0):
        self.nome = nome
        self.__nota = nota 

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
            print(f"Nota atribuída com sucesso: {valor}")
        else:
            print("Erro: a nota deve estar entre 0 e 10.")

aluno = Aluno("Carlos")

print(f"Aluno: {aluno.nome}, Nota inicial: {aluno.nota}")

aluno.nota = 8
print(f"Nota atual: {aluno.nota}")

aluno.nota = 12 
print(f"Nota final: {aluno.nota}")
