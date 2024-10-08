def calcular_semi_eixo_maior(caminho_arquivo, dias=10):
    semieixos_maiores = []
    
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        
      
        for linha in linhas:
            if linha[0] == '2':  
                movimento_medio = linha[52:63].strip()
                
                
                semieixo_maior = (3.986 * (10**5))**(1/3) / ((2 * np.pi * float(movimento_medio)) / 86400)**(2/3)
                semieixos_maiores.append(semieixo_maior)
 
                if len(semieixos_maiores) >= dias:
                    break
 
    return semieixos_maiores
 

semieixos_amazonia = calcular_semi_eixo_maior("amazonia.txt", dias=10)
semieixos_cosmos = calcular_semi_eixo_maior("cosmos.txt", dias=10)
 

print("Semieixos maiores para o arquivo amazonia.txt:", semieixos_amazonia)
print("Semieixos maiores para o arquivo cosmos.txt:", semieixos_cosmos)