### Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
### Centro de Informática (CIn) (http://www.cin.ufpe.br)
### Graduando em Sistemas de Informação
### IF969 - Algoritmos e Estrutura de Dados

### Autor: Vinícius Luiz da Silva França (vlsf2)
### Email: vlsf2@cin.ufpe.br
### Data: 2020-10-30

### Copyright(c) 2020 Vinícius Luiz da Silva França

> - **1.**   **Contexto do problema**
>
>   1. Em 1997, havia 332 aeroportos no Estados Unidos, com isso, seria possível haver cerca de 54.946 rotas sem escala no território americano. OBS: Uma rota de um aeroporto A para B é considerado a mesma rota do aeroporto B para A
>
>   2. Porém, das 54.946 rotas sem escalas possíveis, apenas 2126 são utilizadas, ou seja, 96,13% das rotas possíveis não existem.
>
>   **2.**   **Detalhamento da base de dados (link da base e informações do que esta base contém);**
>
>   1. A base de dados “Pajek network: US Air flights, 1997” contém 2 arquivos importantes:
>
>   1. “USAir97” contém a quantidade de vértices (aeroportos) em acompanhada da quantidade de arestas (rotas sem escala), em seguida, contém todas as rotas existentes juntamente com seus pesos (distância em milhas); o grafo é ponderado e não-direcionado
>
>   2. “USAir97_nodename” contém todos os nomes dos aeroportos
>
>   **3.**   **O problema que foi resolvido;**
>
>   1. Nós encontramos a menor rota com escala entre 2 aeroportos não conectados. 
>
>   **4.**   **Como o problema foi resolvido;**
>
>   1. Dado dois aeroportos, verificamos se eles possuem uma rota sem escala, se não houver, o algoritmo de Dijkstra encontra a menor rota com escala entre dois aeroportos não conectados diretamente.
>   **5.** **As tecnologias utilizadas;**
>
>   1. A representação do grafo foi implementada por meio da matriz de adjacência
>
>   2.  Foi implementado também um dicionário que dado um vértice, visualizamos o nome dos seus adjacentes, assim, facilitando a busca.
>
>   **6.**   **Resultados encontrados; como avaliar os resultados encontrados? Você conseguiu colocar alguma medida que avalie a qualidade dos seus resultados? Se não encontrou, tudo bem, mas justifique.**
>
>   1. Em uma análise completa nas 52.986 rotas sem escalas não existentes, o algoritmo de Dijkstra conseguiu encontrar um menor caminho em **todas** elas, ou seja, para todo aeroporto A, conseguimos chegar a qualquer outro aeroporto B através do algoritmo. (100% de eficácia).
>
>   2. Em uma análise manual, foi encontrado voos longos com até 5 escalas, sendo esse o menor caminho.
>
>   **7.   Conclusão.**
>
>   1. Desde que todas as rotas existentes estejam bem distribuídas, conseguimos suprir a necessidade das rotas faltantes.
>
>   2. O algoritmo de Dijkstra mostra grande eficiência quando se trata de rotas aéreas, visto que um país – como o EUA – possui aeroportos bem distribuídos pelo seu território.
>
>   3. E quanto aos voos com muitas escalas? Dependendo da demanda dessa rota, é viável criar novas rotas para diminuir as escalas desse voo.
>
>    
