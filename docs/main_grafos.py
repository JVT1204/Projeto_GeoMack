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
        print("9. Sair")
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
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()