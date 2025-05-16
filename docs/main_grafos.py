# Gabriel Mason Guerino - 10409928
# Gabriel Shihao Chen Yin - 10408981
# Fernando Pegoraro Bilia - 10402097
# João Vitor Tortorello - 10402674
# Mauricio Gabriel Gutierrez de Garcia - 10403130

# Arquivo texto para ser lido: grafo_mack.txt
# Arquivo texto de saída do grafo: "nome_desejado".txt

# Arquivo main: contém menu de opções que faz a interação com o usuário

from func_grafos import TGrafoND

def menu():
    grafo = None
    while True:
        print("\n--- GeoMack - Menu de Opções ---")
        print("1. Ler dados do arquivo texto desejado")
        print("2. Gravar dados no arquivo de saída")
        print("3. Inserir vértice")
        print("4. Inserir aresta")
        print("5. Remover vértice")
        print("6. Remover aresta")
        print("7. Mostrar conteúdo do grafo")
        print("8. Verificar grau de conexidade")
        print("9. Calcular menor caminho (Dijkstra)")
        print("10. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_arquivo = input("Digite o nome do arquivo de entrada: ")
            grafo = TGrafoND(0, 1)
            grafo.carregarDoArquivo(nome_arquivo)

        elif opcao == "2":
            if grafo:
                nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
                grafo.gravarNoArquivo(nome_arquivo_saida)
                print(f"Grafo exibido e gravado no arquivo de saída.")
            else:
                print("Grafo não carregado.")

        elif opcao == "3":
            if grafo:
                nome_predio = input("Digite o nome do prédio para o novo vértice: ").strip()
                if nome_predio:
                    grafo.inserir_vertice_com_nome(nome_predio)
                else:
                    print("Nome do prédio não fornecido. Vértice não inserido.")
            else:
                print("Grafo não carregado.")

        elif opcao == "4":
            if grafo:
                v = int(input("Digite o vértice de origem: "))
                w = int(input("Digite o vértice de destino: "))
                if not grafo.existe_vertice(v) or not grafo.existe_vertice(w):
                    print(f"Erro: O vértice {v} ou {w} não existe.")
                else:
                    peso = float(input("Digite o peso da aresta: "))
                    grafo.insereA(v, w, peso)
                    print("Aresta inserida com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "5":
            if grafo:
                v = int(input("Digite o vértice a ser removido: "))
                if not grafo.existe_vertice(v):
                    print(f"Erro: O vértice {v} não existe.")
                else:
                    grafo.removeVertice(v)
                    print(f"Vértice {v} removido com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "6":
            if grafo:
                v = int(input("Digite o vértice de origem: "))
                w = int(input("Digite o vértice de destino: "))
                grafo.removeAresta(v, w)
            else:
                print("Grafo não carregado.")

        elif opcao == "7":
            if grafo:
                print("Conteúdo do grafo:")
                grafo.mostrarGrafo()
            else:
                print("Grafo não carregado.")

        elif opcao == "8":
            if grafo:
                print(f"Grau de conexidade do grafo: {grafo.categoriaConexidade()}")
            else:
                print("Grafo não carregado.")
                
        elif opcao == "9":
            if grafo:
                # Mostrar os vértices disponíveis e seus nomes
                print("\nVértices disponíveis:")
                print("ID | NOME DO PRÉDIO")
                print("-" * 80)
                for i in range(grafo.n):
                    nome = grafo.get_nome_predio(i)
                    # Remove as aspas extras se existirem
                    nome = nome.strip('"')
                    print(f"{i:2} | {nome}")
                print("-" * 80)
                
                try:
                    origem = int(input("\nDigite o vértice de origem: "))
                    if grafo.existe_vertice(origem):
                        nome_origem = grafo.get_nome_predio(origem)
                        print(f"Prédio de origem selecionado: {nome_origem}")
                    else:
                        print(f"Erro: Vértice {origem} não existe.")
                        continue
                        
                    destino = int(input("Digite o vértice de destino: "))
                    if grafo.existe_vertice(destino):
                        nome_destino = grafo.get_nome_predio(destino)
                        print(f"Prédio de destino selecionado: {nome_destino}")
                    else:
                        print(f"Erro: Vértice {destino} não existe.")
                        continue
                    
                    if not grafo.existe_vertice(origem) or not grafo.existe_vertice(destino):
                        print(f"Erro: Vértice de origem {origem} ou destino {destino} não existe.")
                    else:
                        print(f"\nCalculando menor caminho de {origem} ({nome_origem}) para {destino} ({nome_destino})...")
                        caminho, distancia = grafo.dijkstra(origem, destino)
                        
                        if distancia == float('inf') or caminho is None or len(caminho) == 0:
                            print(f"Não existe caminho entre os vértices {origem} ({nome_origem}) e {destino} ({nome_destino}).")
                        else:
                            print(f"\nMenor caminho de {origem} ({nome_origem}) a {destino} ({nome_destino}):")
                            print(f"Distância total: {distancia:.2f}")
                            
                            print("\nCaminho completo:")
                            for i in range(len(caminho)):
                                v = caminho[i]
                                nome = grafo.get_nome_predio(v)
                                if i < len(caminho) - 1:
                                    proxV = caminho[i+1]
                                    peso = grafo.adj[v][proxV]
                                    print(f"  {v:2} ({nome}) --[{peso:.2f}]--> ", end="")
                                else:
                                    print(f"{v:2} ({nome})")
                except ValueError:
                    print("Por favor, insira números válidos para os vértices.")
            else:
                print("Grafo não carregado.")

        elif opcao == "10":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()