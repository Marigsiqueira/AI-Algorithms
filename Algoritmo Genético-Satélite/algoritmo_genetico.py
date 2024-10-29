import numpy as np
import math 
    
# Calcular a avaliação 
def calcular_avaliacao(semi_eixo_maior):
     raio_terra = 6371
     mu = 398600 
     delta_v = math.sqrt(mu / semi_eixo_maior) 

     avaliacao = 1 / delta_v 
     return avaliacao


def calcular_semi_eixo_maior(caminho_arquivo, dias=10):
    semieixos_maiores = []
    avaliacoes = []
    
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

        
      
        for linha in linhas:
            if linha[0] == '2':  

                movimento_medio = linha[52:63].strip()
                movimento_medio = movimento_medio.replace(',','.').strip() 

                try:
                    movimento_medio_float = float(movimento_medio)
                except ValueError as e:
                    print(f"Erro ao converter '{movimento_medio}': {e}")
                    continue 
                
                semieixo_maior = (3.986 * (10**5))**(1/3) / ((2 * np.pi * (movimento_medio_float)) / 86400)**(2/3)
                semieixos_maiores.append(semieixo_maior)
                
                
                semieixo_maior = (3.986 * (10**5))**(1/3) / ((2 * np.pi * (movimento_medio_float)) / 86400)**(2/3)
                semieixos_maiores.append(semieixo_maior)
 
                if len(semieixos_maiores) >= dias:
                    break
 
    return semieixos_maiores
 

semieixos_amazonia = calcular_semi_eixo_maior("amazonia.txt", dias=10)
semieixos_cosmos = calcular_semi_eixo_maior("cosmos.txt", dias=10)
 

print("Semieixos maiores para o arquivo amazonia.txt:", semieixos_amazonia)
print("Semieixos maiores para o arquivo cosmos.txt:", semieixos_cosmos)


