# Projeto_GeoMack

## Integrantes

- Gabriel Mason Guerino - 10409928
- Gabriel Shihao Chen Yin - 10408981
- Fernando Pegoraro Bilia - 10402097
- João Vitor Tortorello - 10402674
- Mauricio Gabriel Gutierrez de Garcia - 10403130

## Descrição e Objetivo do projeto

Projeto para a matéria Teoria dos Grafos na Universidade Presbiteriana Mackenzie que tem como objetivo modelar o campus Higienópolis Mackenzie como um grafo para entender melhor as conexões entre os prédios, avaliar
possíveis melhorias na infraestrutura e identificar rotas mais eficientes para deslocamento
dentro do campus.

Nosso objetivo é criar um sistema eficiente de caminho mínimo para o campus Higienópolis Mackenzie, o que pode facilitar a vida de calouros ou pessoas que não frequentam diariamente a universidade e se sente perdido ao transitar pelo lugar.

Como requisito do projeto, foi pedido pelo professor da disciplina de Teoria de Grafos que destaque um dos Objetivos do Desenvolvimento Sustentável (ODS - https://odsbrasil.gov.br/), e o escolhido foram: 

- 9 (Indústria, inovação e infraestrutura), já que o estudo da conectividade do campus pode ajudar no planejamento de melhorias estruturais, promovendo um ambiente acadêmico mais eficiente e acessível
- 11 (Cidades e Comunidades Sustentáveis), em que a análise da mobilidade dentro do campus contribui para um espaço mais organizado e sustentável, reduzindo deslocamentos desnecessários e otimizando a circulação dos alunos.

## Definições:

#### Arquivo texto (`grafo_mack`) criado com a finalidade de simular em forma de grafo o campus Higienópolis Mackenzie
#### Estrutura do arquivo:
### 1. Tipo do Grafo - Primeira linha

0 – grafo não orientado sem peso;

1 – grafo não orientado com peso no vértice;

2 – grafo não orientado com peso na aresta;

3 – grafo não orientado com peso nos vértices e arestas;

4 – grafo orientado sem peso;

5 – grafo orientado com peso no vértice;

6 – grafo orientado com peso na aresta;

7 – grafo orientado com peso nos vértices e arestas.

### 2. Número de vértices
### 3. Lista de vértices (próximas n linhas) - `[número_do_vértice] [nome_predio]`
- Vértices (Nodos): Cada prédio ou outra dependência da universidade será representada como um vértice no grafo.
### 4. Número de arestas
### 5. Lista de arestas (próximas n linhas) - `[vértice_origem] [vértice_destino] [peso]`
- Arestas: As arestas representarão as conexões diretas entre os prédios, com pesos correspondentes à distância física (em metros).

## Imagem grafo (Rede Metroviária de São Paulo)

![alt](/assets/Imagem_graphOnline_GeoMack.png)