import json
from datetime import datetime

ARQ_LIVROS = "livros.json"
ARQ_ALUGUEIS = "alugueis.json"


def carregar(arquivo):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)


def cadastrar_livro(titulo, autor, quantidade):
    livros = carregar(ARQ_LIVROS)
    
    livro = {
        "id": len(livros) + 1,
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }
    
    livros.append(livro)
    salvar(ARQ_LIVROS, livros)
    print("Livro cadastrado!")

def listar_livros():
    livros = carregar(ARQ_LIVROS)
    for l in livros:
        print(f"{l['id']} - {l['titulo']} ({l['autor']}) | Estoque: {l['quantidade']}")


def alugar_livro(id_livro, cliente):
    livros = carregar(ARQ_LIVROS)
    alugueis = carregar(ARQ_ALUGUEIS)

    for livro in livros:
        if livro["id"] == id_livro:
            if livro["quantidade"] > 0:
                livro["quantidade"] -= 1

                aluguel = {
                    "livro_id": id_livro,
                    "cliente": cliente,
                    "data_aluguel": datetime.now().strftime("%d/%m/%Y"),
                    "devolvido": False
                }

                alugueis.append(aluguel)

                salvar(ARQ_LIVROS, livros)
                salvar(ARQ_ALUGUEIS, alugueis)

                print("Livro alugado com sucesso!")
                return
            else:
                print("Sem estoque disponível!")
                return

    print("Livro não encontrado!")

def devolver_livro(id_livro, cliente):
    livros = carregar(ARQ_LIVROS)
    alugueis = carregar(ARQ_ALUGUEIS)

    for aluguel in alugueis:
        if aluguel["livro_id"] == id_livro and aluguel["cliente"] == cliente and not aluguel["devolvido"]:
            aluguel["devolvido"] = True

            for livro in livros:
                if livro["id"] == id_livro:
                    livro["quantidade"] += 1

            salvar(ARQ_LIVROS, livros)
            salvar(ARQ_ALUGUEIS, alugueis)

            print("Livro devolvido!")
            return

    print("Aluguel não encontrado!")

def listar_alugueis():
    alugueis = carregar(ARQ_ALUGUEIS)
    for a in alugueis:
        status = "Devolvido" if a["devolvido"] else "Em aberto"
        print(f"Livro ID: {a['livro_id']} | Cliente: {a['cliente']} | {status}")


def menu():
    while True:
        print("\n--- SISTEMA DE ALUGUEL ---")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Alugar livro")
        print("4 - Devolver livro")
        print("5 - Listar alugueis")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            t = input("Título: ")
            a = input("Autor: ")
            q = int(input("Quantidade: "))
            cadastrar_livro(t, a, q)

        elif op == "2":
            listar_livros()

        elif op == "3":
            id_l = int(input("ID do livro: "))
            c = input("Cliente: ")
            alugar_livro(id_l, c)

        elif op == "4":
            id_l = int(input("ID do livro: "))
            c = input("Cliente: ")
            devolver_livro(id_l, c)

        elif op == "5":
            listar_alugueis()

        elif op == "0":
            break

        else:
            print("Opção inválida!")


menu()