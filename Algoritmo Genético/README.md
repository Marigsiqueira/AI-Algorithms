 <h1>Problema da Otimização da Carga do Caminhão</h1>
    
    <h2>Descrição</h2>
    <p>Uma empresa de entregas precisa carregar um caminhão com produtos, buscando maximizar o lucro da operação. Cada produto tem características específicas como nome, valor e o espaço que ocupa dentro do caminhão.</p>
    <p>O objetivo é encontrar a melhor combinação de produtos que devem ser transportados, considerando o limite de espaço disponível no caminhão, de forma a obter o maior lucro possível.</p>
    
    <h2>Detalhes do Problema</h2>
    <ul>
        <li>O caminhão possui uma capacidade máxima de 3m³.</li>
        <li>A soma dos volumes de todos os produtos disponíveis é 4,79m³, o que torna impossível carregar todos os produtos de uma vez.</li>
        <li>A tarefa do algoritmo é selecionar os produtos que serão transportados, respeitando o limite de espaço, enquanto maximiza o valor total dos produtos escolhidos.</li>
    </ul>

    <h2>Solução</h2>
    <p>Foi implementado um Algoritmo Genético para resolver este problema de otimização, conhecido como o <strong>Problema da Mochila</strong> (Knapsack Problem). O algoritmo genético utiliza operações inspiradas na seleção natural, como:</p>
    <ul>
        <li><strong>Crossover (cruzamento)</strong>: combinação de cromossomos de dois "pais" para gerar uma nova solução.</li>
        <li><strong>Mutação</strong>: alteração de alguns genes de um cromossomo para explorar novas soluções.</li>
        <li><strong>Seleção</strong>: escolha dos melhores indivíduos da população para garantir que as melhores soluções sejam mantidas e aprimoradas ao longo das gerações.</li>
    </ul>

    <h2>Produtos</h2>
    <table border="1" cellspacing="0" cellpadding="10">
        <thead>
            <tr>
                <th>Produto</th>
                <th>Espaço (m³)</th>
                <th>Valor (R$)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Geladeira Dako</td>
                <td>0.751</td>
                <td>999.90</td>
            </tr>
            <tr>
                <td>Iphone 6</td>
                <td>0.0000899</td>
                <td>2911.12</td>
            </tr>
            <tr>
                <td>TV 55</td>
                <td>0.400</td>
                <td>4346.99</td>
            </tr>
            <tr>
                <td>TV 50</td>
                <td>0.290</td>
                <td>3999.90</td>
            </tr>
            <tr>
                <td>TV 42</td>
                <td>0.200</td>
                <td>2999.00</td>
            </tr>
            <tr>
                <td>Notebook Dell</td>
                <td>0.200</td>
                <td>2999.00</td>
            </tr>
            <tr>
                <td>Ventilador Panasonic</td>
                <td>0.496</td>
                <td>199.90</td>
            </tr>
            <tr>
                <td>Microondas Electrolux</td>
                <td>0.0424</td>
                <td>308.66</td>
            </tr>
            <tr>
                <td>Microondas LG</td>
                <td>0.0544</td>
                <td>429.90</td>
            </tr>
            <tr>
                <td>Microondas Panasonic</td>
                <td>0.0319</td>
                <td>299.29</td>
            </tr>
            <tr>
                <td>Geladeira Brastemp</td>
                <td>0.635</td>
                <td>849.00</td>
            </tr>
            <tr>
                <td>Geladeira Consul</td>
                <td>0.870</td>
                <td>1199.89</td>
            </tr>
            <tr>
                <td>Notebook Lenovo</td>
                <td>0.498</td>
                <td>1999.90</td>
            </tr>
            <tr>
                <td>Notebook Asus</td>
                <td>0.527</td>
                <td>3999.00</td>
            </tr>
        </tbody>
    </table>
