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

    # SETTERS COM VALIDACAO

    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            self.__nome = nome.strip()
        else:
            print("Erro: o nome deve ter pelo menos 3 caracteres.")
            print("O nome anterior foi mantido.")

    def set_preco(self, preco):
        if (
            isinstance(preco, (int, float))
            and not isinstance(preco, bool)
            and preco >= 0
        ):
            self.__preco = float(preco)
        else:
            print("Erro: o preco deve ser um numero nao negativo.")
            print("O preco anterior foi mantido.")


# ==============================================================================
# TESTE DE VALIDACAO DO PROJETO FINAL
# ==============================================================================

if __name__ == "__main__":

    print("=== TESTANDO A CLASSE BASE DO PROJETO FINAL ===")

    # 1. Teste de instanciação com dados validos

    objeto_valido = Produto("X-Burguer", 25.00)

    print(
        f"Produto criado: {objeto_valido.get_nome()} "
        f"- R$ {objeto_valido.get_preco():.2f}"
    )

    # 2. Teste de instanciação com preco invalido

    print("\n--- Teste 1: Tentativa de criar com preco negativo ---")

    objeto_invalido = Produto("Hamburguer", -15.00)

    print(
        f"Resultado mantido com seguranca: "
        f"R$ {objeto_invalido.get_preco():.2f}"
    )

    # 3. Teste de alteracao via Setter com dado invalido

    print("\n--- Teste 2: Tentativa de alterar o nome para um texto curto ---")

    objeto_valido.set_nome("AB")

    print(f"Nome do produto protegido: {objeto_valido.get_nome()}")

    # 4. Teste de alteracao do preco com dado valido

    print("\n--- Teste 3: Alteracao para um preco valido ---")

    objeto_valido.set_preco(30.00)

    print(f"Novo preco: R$ {objeto_valido.get_preco():.2f}")

    print("\n=== TESTES FINALIZADOS ===")

