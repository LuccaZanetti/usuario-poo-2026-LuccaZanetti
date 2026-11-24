
# ==============================================================================
# PROJETO FINAL DO BIMESTRE - JUCEMIR BURGERS
# Integrantes: Lucas Franco e Lucca Zanetti
# Turma: 2A TI
# ==============================================================================


class Produto:

    def __init__(self, nome, preco):
        self.__nome = "Produto sem nome"
        self.__preco = 0.0

        self.set_nome(nome)
        self.set_preco(preco)

    # GETTERS

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    # SETTERS COM VALIDACAO E EXCECOES

    def set_nome(self, nome):
        if not isinstance(nome, str) or len(nome.strip()) < 3:
            raise ValueError("O nome deve possuir pelo menos 3 caracteres.")

        self.__nome = nome.strip()

    def set_preco(self, preco):
        if (
            not isinstance(preco, (int, float))
            or isinstance(preco, bool)
            or preco < 0
        ):
            raise ValueError("O preco deve ser um numero nao negativo.")

        self.__preco = float(preco)


# ==============================================================================
# CARDAPIO DA JUCEMIR BURGERS
# ==============================================================================

cardapio = [
    Produto("X-Burguer", 25.00),
    Produto("X-Salada", 28.00),
    Produto("X-Bacon", 32.00),
    Produto("X-Tudo", 38.00),
    Produto("Batata Frita", 15.00),
    Produto("Refrigerante", 8.00)
]


# ==============================================================================
# FUNCAO PARA EXIBIR O CARDAPIO
# ==============================================================================

def exibir_cardapio():

    print("\n========== JUCEMIR BURGERS ==========")
    print("                CARDAPIO")
    print("=====================================")

    for i, produto in enumerate(cardapio, start=1):
        print(
            f"{i} - {produto.get_nome()} "
            f"| R$ {produto.get_preco():.2f}"
        )

    print("=====================================")


# ==============================================================================
# FUNCAO PARA VALIDAR ENTRADAS NUMERICAS
# ==============================================================================

def ler_numero(mensagem, minimo, maximo):

    while True:
        try:
            valor = int(input(mensagem))

            if valor < minimo or valor > maximo:
                print(
                    f"Opcao invalida! Digite um numero "
                    f"entre {minimo} e {maximo}."
                )
                continue

            return valor

        except ValueError:
            print("Entrada invalida! Digite apenas numeros inteiros.")

        except (EOFError, KeyboardInterrupt):
            print("\nOperacao interrompida pelo usuario.")
            return None


# ==============================================================================
# FUNCAO PARA REALIZAR UM PEDIDO
# ==============================================================================

def realizar_pedido():

    exibir_cardapio()

    opcao = ler_numero(
        "\nDigite o numero do produto desejado: ",
        1,
        len(cardapio)
    )

    if opcao is None:
        return

    try:
        produto = cardapio[opcao - 1]

        print("\nPedido realizado com sucesso!")
        print(f"Produto: {produto.get_nome()}")
        print(f"Valor: R$ {produto.get_preco():.2f}")

    except IndexError:
        print("Produto nao encontrado! Confira as opcoes do cardapio.")

    except Exception:
        print("Nao foi possivel realizar o pedido. Tente novamente.")


# ==============================================================================
# FUNCAO PARA CALCULAR A MEDIA DOS PRECOS
# ==============================================================================

def calcular_media():

    try:
        total = sum(produto.get_preco() for produto in cardapio)

        media = total / len(cardapio)

        print(f"\nMedia dos precos: R$ {media:.2f}")

    except ZeroDivisionError:
        print("Nao foi possivel calcular a media: cardapio vazio.")

    except Exception:
        print("Ocorreu um problema ao calcular a media dos precos.")


# ==============================================================================
# MENU PRINCIPAL COM BLINDAGEM
# ==============================================================================

def menu_principal():

    while True:

        print("\n=====================================")
        print("       BEM-VINDO A JUCEMIR BURGERS")
        print("=====================================")
        print("1 - Ver cardapio")
        print("2 - Realizar pedido")
        print("3 - Consultar media dos precos")
        print("4 - Testar validacao de produto")
        print("5 - Sair")
        print("=====================================")

        opcao = ler_numero("Escolha uma opcao: ", 1, 5)

        if opcao is None:
            break

        try:

            if opcao == 1:
                exibir_cardapio()

            elif opcao == 2:
                realizar_pedido()

            elif opcao == 3:
                calcular_media()

            elif opcao == 4:

                print("\n--- TESTE DE VALIDACAO ---")

                nome = input("Digite o nome do produto: ")

                try:
                    preco = float(input("Digite o preco do produto: "))

                    novo_produto = Produto(nome, preco)

                    print("\nProduto cadastrado com sucesso!")
                    print(f"Nome: {novo_produto.get_nome()}")
                    print(f"Preco: R$ {novo_produto.get_preco():.2f}")

                except ValueError:
                    print(
                        "Dados invalidos! Verifique o nome "
                        "e o preco e tente novamente."
                    )

            elif opcao == 5:
                print("\nObrigado por visitar a Jucemir Burgers!")
                print("Volte sempre!")
                break

        except Exception:
            print(
                "Ops! Ocorreu um problema inesperado "
                "nesta operacao. Tente novamente."
            )


# ==============================================================================
# EXECUCAO DO PROGRAMA
# ==============================================================================

if __name__ == "__main__":

    try:
        menu_principal()

    except Exception:
        print("O sistema encontrou um problema. Reinicie o programa.")

    finally:
        print("\nSistema Jucemir Burgers finalizado.")
