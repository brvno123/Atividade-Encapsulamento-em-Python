class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = None
        self.senha = senha  # Usa o setter com validação

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
            print("Senha definida com sucesso.")
        else:
            print("Erro: a senha deve ter pelo menos 6 caracteres.")

    def verificar_senha(self, tentativa):
        return tentativa == self.__senha

print("Criando usuário com senha válida:")
usuario1 = Usuario("joao@example.com", "abc123")
print(f"Email: {usuario1.email}")
print("Verificando senha correta:", usuario1.verificar_senha("abc123")) 
print("Verificando senha incorreta:", usuario1.verificar_senha("123456"))  
print()

print("Criando usuário com senha inválida:")
usuario2 = Usuario("maria@example.com", "123")
print(f"Email: {usuario2.email}")
print("Verificando senha:", usuario2.verificar_senha("123"))