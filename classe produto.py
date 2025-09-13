class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = None  
        self.set_preco(preco)  


    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if novo_preco < 0:
            print("Erro: o preço não pode ser negativo.")
        else:
            self.__preco = novo_preco

    preco = property(get_preco, set_preco)

produto = Produto("Notebook", 3000)

print(f"Produto: {produto.nome}, Preço: R${produto.preco}")

produto.preco = 2500
print(f"Preço atualizado: R${produto.preco}")

produto.preco = -500  # Isso deve exibir a mensagem de erro
print(f"Preço final: R${produto.preco}")