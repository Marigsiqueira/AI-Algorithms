from random import random

#Classe produto que armazena os produtos

class Produto():
    def __init__(self, nome, espaco, valor): 
      self.nome = nome
      self.espaco = espaco
      self.valor = valor


    #Método para exibir informações dos produtos
    def __str__(self):
        return f'{self.nome} - Espaço: {self.espaco} m³, Valor: R${self.valor:.2f}'


#Classe para armazenar individuos

class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos 
        self.nota_avaliacao = 0
        self.geracao = geracao
        self.cromossomo = []

        #Inicialização do cromossomo para receber 0 ou 1 de forma aleatória
        for i in range(len(espacos)):
            if random() < 0.5: 
                self.cromossomo.append("0")
            else:
                self.cromossomo.append('1')



if __name__ == '__main__':
    lista_produtos = []
    lista_produtos.append(Produto('Geladeira Dako', 0.751, 999.90))
    lista_produtos.append(Produto('Iphone 6', 0.0000899, 2911.12))
    lista_produtos.append(Produto('TV 55', 0.400, 4346.99))
    lista_produtos.append(Produto('TV 50', 0.290, 3999.90))
    lista_produtos.append(Produto('TV 42', 0.200, 2999.00))
    lista_produtos.append(Produto('Notebook Dell', 0.200, 2999.00))
    lista_produtos.append(Produto('Ventilador Panasonic', 0.496, 199.90))   
    lista_produtos.append(Produto('Microondas Electrolux', 0.0424, 308.66))
    lista_produtos.append(Produto('Microondas LG', 0.0544, 429.90))
    lista_produtos.append(Produto('Microondas Panasonic', 0.0319, 299.29))
    lista_produtos.append(Produto('Geladeira Brastemp', 0.635, 849.00))
    lista_produtos.append(Produto('Geladeira Consul', 0.870, 1199.89))
    lista_produtos.append(Produto('Notebook Lenovo', 0.498, 1999.90))
    lista_produtos.append(Produto('Notebook Asus', 0.527, 3999.00)) 

    #for produto in lista_produtos:
    #    print(produto)

    espacos = []
    valores = []
    nomes = []

    #Adicionar informações de cada produto na lista espacos, valores e nomes
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    limite = 3   #Limite de espaço no caminhâo 3m³


    #Mostrar espacos, valores e cromossomo com solucao aleatoria
    individuo1 = Individuo(espacos, valores, limite)
    print("Espaços = %s" %str(individuo1.espacos))
    print("Valores = %s" %str(individuo1.valores))
    print("Cromossomo= %s" %str(individuo1.cromossomo))


