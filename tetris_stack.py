# ============================================
# Desafio Tetris Stack - Tema 3
# Disciplina: Estrutura de Dados
# Autor: Gabriel Santos Silva
# Linguagem: Python
# ============================================

class TetrisStack:
    def __init__(self):
        self.stack = []  # pilha vazia

    def empilhar(self, peca):
        """Adiciona uma peça ao topo da pilha."""
        self.stack.append(peca)
        print(f"Peça '{peca}' empilhada com sucesso!")

    def desempilhar(self):
        """Remove a peça do topo da pilha."""
        if not self.stack:
            print("⚠️ A pilha está vazia! Nenhuma peça para remover.")
        else:
            removida = self.stack.pop()
            print(f"Peça '{removida}' removida do topo da pilha.")

    def mostrar_pilha(self):
        """Exibe todas as peças empilhadas."""
        if not self.stack:
            print("A pilha está vazia!")
        else:
            print("\n🧱 Estado atual da pilha (base → topo):")
            for peca in self.stack:
                print(f"[ {peca} ]")
            print()

def menu():
    print("=" * 40)
    print("       🎮 DESAFIO TETRIS STACK - TEMA 3")
    print("=" * 40)
    print("1 - Empilhar peça")
    print("2 - Desempilhar peça")
    print("3 - Mostrar pilha")
    print("4 - Sair")
    print("=" * 40)

def main():
    pilha = TetrisStack()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            peca = input("Digite o nome da peça (I, O, T, L, Z...): ").upper()
            pilha.empilhar(peca)

        elif opcao == "2":
            pilha.desempilhar()

        elif opcao == "3":
            pilha.mostrar_pilha()

        elif opcao == "4":
            print("Encerrando o programa... Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()
