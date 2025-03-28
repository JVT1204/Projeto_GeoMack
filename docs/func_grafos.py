# Gabriel Mason Guerino - 10409928
# Gabriel Shihao Chen Yin - 10408981
# Fernando Pegoraro Bilia - 10402097
# João Vitor Tortorello - 10402674
# Mauricio Gabriel Gutierrez de Garcia - 10403130

# Arquivo de funções: contém todas as funções necessárias para o funcionamento do projeto

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
                num_arestas_esperadas = int(linhas[2 + self.n].strip())

                arestas_lidas = 0
                for linha in linhas:
                    valores = linha.strip().split()
                    if len(valores) == 3:
                        v, w, peso = map(float, valores)
                        self.adj[int(v)][int(w)] = peso
                        if self.tipo_grafo == 2 and self.adj[int(w)][int(v)] == 0:
                            self.adj[int(w)][int(v)] = peso
                        arestas_lidas += 1

                self.num_arestas = arestas_lidas

                if self.num_arestas != num_arestas_esperadas:
                    print(f"Alerta: Número de arestas lido ({self.num_arestas}) diferente do esperado ({num_arestas_esperadas})")
                else:
                    print(f"Arquivo carregado corretamente com {self.num_arestas} arestas.")
        except FileNotFoundError:
            print(f"Erro: Arquivo '{arquivo}' não encontrado.")

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
