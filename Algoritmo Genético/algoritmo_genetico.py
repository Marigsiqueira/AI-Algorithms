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
        self.espaco_usado = 0
        self.geracao = geracao
        self.cromossomo = []

        #Inicialização do cromossomo para receber 0 ou 1 de forma aleatória
        for i in range(len(espacos)):
            if random() < 0.5: 
                self.cromossomo.append("0")
            else:
                self.cromossomo.append('1')
    
    #Função de Fitness
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == '1':
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
        if soma_espacos > self.limite_espacos:
            nota = 1 #Rebaixando nota do individuo
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos

#Função Crossover
    def crossover(self, outro_individuo):
        corte = round(random() *len(self.cromossomo)) #Ponto que define qual parte do cromossomo dos pais irá ser utilizada para gear um novo filho
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]

        filhos = [Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1),
                  Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)]
        filhos[0].cromossomos = filho1
        filhos[1].cromossomos = filho2
        return filhos
    

    #Função Mutação
    def mutacao(self, taxa_mutacao):
        print("Antes %s" % self.cromossomo)
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        print('Depois: %s' % self.cromossomo)
        return self


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


   #Cria individuo, idenfica quais itens da lista de produtos ele irá levar, faz a avaliação Fitness e imprime nota e espaço usado
    individuo1 = Individuo(espacos, valores, limite)
    print("\n Indivíduo 1")
    for i in range(len(lista_produtos)):
        if individuo1.cromossomo[i] == '1':
            print("Nome: %s R$: %s" % (lista_produtos[i].nome, lista_produtos[i].valor))   
    individuo1.avaliacao()
    print('Nota = %s' % individuo1.nota_avaliacao)
    print ('Espaco usado %s' % individuo1.espaco_usado)


    individuo2 = Individuo(espacos, valores, limite)
    print("\n Indivíduo 2")
    for i in range(len(lista_produtos)):
        if individuo2.cromossomo[i] == '1':
            print("Nome: %s R$: %s" % (lista_produtos[i].nome, lista_produtos[i].valor))   
    individuo2.avaliacao()
    print('Nota = %s' % individuo2.nota_avaliacao)
    print ('Espaco usado %s' % individuo2.espaco_usado)


    #Teste Crossover
    individuo1.crossover(individuo2) #Fazer combinação entre os dois indivíduos - Indivíduo2 é outro_individuo

    #Teste Mutação
    individuo1.mutacao(0.05)
    individuo2.mutacao(0.05)
