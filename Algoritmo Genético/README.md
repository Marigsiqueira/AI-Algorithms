Problema da Otimização da Carga do Caminhão
Descrição
Uma empresa de entregas precisa carregar um caminhão com produtos, buscando maximizar o lucro da operação. Cada produto tem características específicas como nome, valor e o espaço que ocupa dentro do caminhão.

O objetivo é encontrar a melhor combinação de produtos que devem ser transportados, considerando o limite de espaço disponível no caminhão, de forma a obter o maior lucro possível.

Detalhes do Problema
O caminhão possui uma capacidade máxima de 3m³.
A soma dos volumes de todos os produtos disponíveis é 4,79m³, o que torna impossível carregar todos os produtos de uma vez.
A tarefa do algoritmo é selecionar os produtos que serão transportados, respeitando o limite de espaço, enquanto maximiza o valor total dos produtos escolhidos.
Solução
Foi implementado um Algoritmo Genético para resolver este problema de otimização, conhecido como o Problema da Mochila (Knapsack Problem). O algoritmo genético utiliza operações inspiradas na seleção natural, como:

Crossover (cruzamento): combinação de cromossomos de dois "pais" para gerar uma nova solução.
Mutação: alteração de alguns genes de um cromossomo para explorar novas soluções.
Seleção: escolha dos melhores indivíduos da população para garantir que as melhores soluções sejam mantidas e aprimoradas ao longo das gerações.
