# Gabriel Mason Guerino - 10409928
# Gabriel Shihao Chen Yin - 10408981
# Fernando Pegoraro Bilia - 10402097
# João Vitor Tortorello - 10402674
# Mauricio Gabriel Gutierrez de Garcia - 10403130

# Arquivo de funções: contém todas as funções necessárias para o funcionamento do projeto

import sys
from collections import deque

class TGrafoND:
    def __init__(self, n, tipo_grafo):
        self.n = n  # Número de vértices
        self.tipo_grafo = tipo_grafo  # Tipo de grafo (1 = direcionado, 2 = não direcionado)
        self.adj = [[0 for _ in range(n)] for _ in range(n)]  # Matriz de adjacência
        self.num_arestas = 0  # Contador de arestas
        self.operacoes = []  # Histórico de operações
        self.predios = {}

    def existe_vertice(self, v):
        return 0 <= v < self.n

    def get_nome_predio(self, v):
        """Retorna o nome do prédio, garantindo que todos os vértices tenham nomes reais."""
        if v not in self.predios:
            nome = f"Prédio {v}"
            self.predios[v] = nome
            return nome
        return self.predios[v]

    def inserir_vertice_com_nome(self, nome_predio):
        n_vertice = self.n
        self.n += 1
        self.adj.append([0] * self.n)
        for i in range(self.n):
            self.adj[i].append(0)
        self.predios[n_vertice] = nome_predio
        self.operacoes.append(f"Vértice inserido: {n_vertice} ({nome_predio})")
        print(f"Vértice {n_vertice} com nome '{nome_predio}' inserido com sucesso.")

    def insereA(self, v, w, peso):
        if not self.existe_vertice(v) or not self.existe_vertice(w):
            print(f"Erro: O vértice {v} ou {w} não existe.")
            return
        if self.adj[v][w] == 0:
            self.adj[v][w] = peso
            if self.tipo_grafo == 2 and self.adj[w][v] == 0:
                self.adj[w][v] = peso
            self.num_arestas += 1
            self.operacoes.append(f"Aresta inserida: {v} - {w} com peso {peso}")

    def removeVertice(self, v):
        if not self.existe_vertice(v):
            print(f"Erro: O vértice {v} não existe.")
            return
        for i in range(self.n):
            if self.adj[v][i] > 0:
                self.num_arestas -= 1
                self.operacoes.append(f"Aresta removida: {v} - {i}")
            self.adj[v][i] = 0
            if self.tipo_grafo == 2:
                self.adj[i][v] = 0
        self.operacoes.append(f"Vértice removido: {v}")

    def removeAresta(self, v, w):
        if not self.existe_vertice(v) or not self.existe_vertice(w):
            print(f"Erro: O vértice {v} ou {w} não existe.")
            return
        if self.adj[v][w] > 0:
            self.adj[v][w] = 0
            if self.tipo_grafo == 2 and self.adj[w][v] > 0:
                self.adj[w][v] = 0
            self.num_arestas -= 1
            self.operacoes.append(f"Aresta removida: {v} - {w}")
            print("Aresta removida com sucesso.")
        else:
            print(f"Erro: A aresta entre {v} e {w} não existe.")

    def mostrarGrafo(self):
        print("Matriz de Adjacência:")
        for i in range(self.n):
            linha = [f"{peso if peso > 0 else '∞'}" for peso in self.adj[i]]
            print(f"Vértice {i}: {linha}")

    def carregarDoArquivo(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                linhas = f.readlines()
                self.tipo_grafo = int(linhas[0].strip())
                self.n = int(linhas[1].strip())
                self.adj = [[0 for _ in range(self.n)] for _ in range(self.n)]
                self.predios = {}
                
                # Tentar extrair nomes dos prédios, se disponíveis no arquivo
                for i in range(2, min(2 + self.n, len(linhas))):
                    linha = linhas[i].strip()
                    if ":" in linha:
                        partes = linha.split(":", 1)  # Divide apenas no primeiro ":"
                        try:
                            idx = int(partes[0].strip())
                            if 0 <= idx < self.n:
                                nome = partes[1].strip().strip('"')
                                self.predios[idx] = nome
                        except (ValueError, IndexError):
                            pass  # Ignora linhas mal formatadas
                    elif '"' in linha:
                        partes = linha.split(' ', 1)
                        try:
                            idx = int(partes[0].strip())
                            if 0 <= idx < self.n:
                                nome = partes[1].strip().strip('"')
                                self.predios[idx] = nome
                        except (ValueError, IndexError):
                            pass  # Ignora linhas mal formatadas
                
                num_arestas_esperadas = int(linhas[2 + self.n].strip())

                arestas_lidas = 0
                for linha in linhas:
                    valores = linha.strip().split()
                    if len(valores) == 3:
                        try:
                            v, w, peso = map(float, valores)
                            self.adj[int(v)][int(w)] = peso
                            if self.tipo_grafo == 2 and self.adj[int(w)][int(v)] == 0:
                                self.adj[int(w)][int(v)] = peso
                            arestas_lidas += 1
                        except (ValueError, IndexError):
                            pass  # Ignora linhas mal formatadas

                self.num_arestas = arestas_lidas
                
                # Garantir que todos os vértices tenham nomes
                for i in range(self.n):
                    if i not in self.predios:
                        self.predios[i] = f"Prédio {i}"

                if self.num_arestas != num_arestas_esperadas:
                    print(f"Alerta: Número de arestas lido ({self.num_arestas}) diferente do esperado ({num_arestas_esperadas})")
                else:
                    print(f"Arquivo carregado corretamente com {self.num_arestas} arestas.")
                    
                print(f"Total de prédios carregados: {self.n}")
                print("Nomes dos prédios:")
                for id_vertice, nome in sorted(self.predios.items()):
                    print(f"  {id_vertice}: {nome}")
                    
        except FileNotFoundError:
            print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        except Exception as e:
            print(f"Erro ao processar arquivo: {str(e)}")

    def gravarNoArquivo(self, arquivo):
        with open(arquivo, 'w') as f:
            f.write(f"Tipo do grafo: {self.tipo_grafo}\n")
            f.write(f"Vértices: {self.n}\n")
            f.write(f"Arestas: {self.num_arestas}\n")

            if self.operacoes:
                f.write("\nOperações realizadas:\n")
                for op in self.operacoes:
                    f.write(f"{op}\n")
                f.write("\n")

            f.write("\nMatriz de Adjacência (Estado Atual do Grafo):\n")
            for i in range(self.n):
                linha = [f"{peso if peso > 0 else '∞'}" for peso in self.adj[i]]
                f.write(f"Vértice {i}: {linha}\n")

            f.write("\nNomes dos Prédios (Atualizados):\n")
            for id_vertice, nome in self.predios.items():
                f.write(f"{id_vertice}: {nome}\n")

    def categoriaConexidade(self):
        visitado = [False] * self.n

        def dfs(v):
            visitado[v] = True
            for i in range(self.n):
                if self.adj[v][i] > 0 and not visitado[i]:
                    dfs(i)

        dfs(0)
        return "Conexo" if all(visitado) else "Desconexo"
    
    # Implementação do Algoritmo de Dijkstra para encontrar o caminho mais curto
    def dijkstra(self, origem, destino):
        if not self.existe_vertice(origem) or not self.existe_vertice(destino):
            print(f"Erro: O vértice {origem} ou {destino} não existe.")
            return None, float('inf')

        # Garantir que os vértices tenham nomes
        nome_origem = self.get_nome_predio(origem)
        nome_destino = self.get_nome_predio(destino)

        dist = [sys.maxsize] * self.n  # Inicializa distâncias como infinito
        dist[origem] = 0
        visitados = [False] * self.n
        antecessor = [None] * self.n

        for _ in range(self.n):
            u = self.min_dist(dist, visitados)
            visitados[u] = True

            for v in range(self.n):
                if self.adj[u][v] > 0 and not visitados[v] and dist[u] + self.adj[u][v] < dist[v]:
                    dist[v] = dist[u] + self.adj[u][v]
                    antecessor[v] = u

        # Reconstrução do caminho (usando IDs dos vértices)
        caminho_ids = []
        atual = destino
        while atual is not None:
            caminho_ids.insert(0, atual)
            atual = antecessor[atual]
        
        # Verificar se o caminho existe
        if not caminho_ids or caminho_ids[0] != origem:
            return [], float('inf')
            
        # Registrar operação no histórico
        nomes_caminho = [f"{v} ({self.get_nome_predio(v)})" for v in caminho_ids]
        operacao = f"Dijkstra: Menor caminho de {origem} ({nome_origem}) a {destino} ({nome_destino}): {' -> '.join(nomes_caminho)} (Distância: {dist[destino]:.2f})"
        self.operacoes.append(operacao)
            
        return caminho_ids, dist[destino]

    def min_dist(self, dist, visitados):
        min_val = sys.maxsize
        min_index = -1

        for v in range(self.n):
            if dist[v] < min_val and not visitados[v]:
                min_val = dist[v]
                min_index = v

        return min_index
    
    def grau_vertices(self):
        graus = {v: 0 for v in range(self.n)}
        for v in range(self.n):
            for w in range(self.n):
                if self.adj[v][w] is not None:
                    graus[v] += 1
        return graus

    def is_euleriano(self):
        graus = self.grau_vertices()
        return all(grau % 2 == 0 for grau in graus.values())

    def is_hamiltoniano(self):
        graus = self.grau_vertices()
        return all(grau >= self.n / 2 for grau in graus.values())
    
    def depthfs(self, origem):
        """Retorna a ordem de visita dos prédios a partir do vértice de origem usando DFS iterativo."""
        if not self.existe_vertice(origem):
            return []

        visitados = [False] * self.n
        ordem_visita = []
        pilha = [origem]

        while pilha:
            v = pilha.pop()
            if not visitados[v]:
                visitados[v] = True
                ordem_visita.append(v)
                # Adiciona os vizinhos em ordem reversa para manter a ordem de visita "natural"
                for w in range(self.n - 1, -1, -1):
                    if self.adj[v][w] > 0 and not visitados[w]:
                        pilha.append(w)
        return ordem_visita

    def Breadthfs(self, origem):
        """Retorna a ordem de visita dos prédios a partir do vértice de origem usando BFS."""
        if not self.existe_vertice(origem):
            return []  # Retorna lista vazia se o vértice não existe

        visitados = [False] * self.n
        fila = []
        ordem_visita = []

        fila.append(origem)
        visitados[origem] = True

        while fila:
            v = fila.pop(0)
            ordem_visita.append(v)
            for w in range(self.n):
                if self.adj[v][w] > 0 and not visitados[w]:
                    fila.append(w)
                    visitados[w] = True
        return ordem_visita
