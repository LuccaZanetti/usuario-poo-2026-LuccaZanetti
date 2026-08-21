class Funcionario:
	def __init__(self, nome, matricula, salario_base):
		self.nome = nome
		self.matricula = matricula
		self.__salario_base = salario_base

	def get_salario_base(self):
		return self.__salario_base

	def set_salario_base(self, novo_salario):
		if novo_salario > 0:
			self.__salario_base = novo_salario

	def calcular_salario_final(self):
		return self.get_salario_base()


class Gerente(Funcionario):
	def __init__(self, nome, matricula, salario_base, bonus_gestao):
		super().__init__(nome, matricula, salario_base)
		self.bonus_gestao = bonus_gestao

	def calcular_salario_final(self):
		return self.get_salario_base() + self.bonus_gestao


class Desenvolvedor(Funcionario):
	def __init__(self, nome, matricula, salario_base, nivel):
		super().__init__(nome, matricula, salario_base)
		self.nivel = nivel

	def calcular_salario_final(self):
		adicional = 1500 if self.nivel == "Senior" else 0
		return self.get_salario_base() + adicional


gerente = Gerente("Ana", "G001", 8000, 2000)
desenvolvedor = Desenvolvedor("Carlos", "D001", 6000, "Senior")

gerente.__salario_base = -100

print(f"{gerente.nome}: R$ {gerente.calcular_salario_final():.2f}")
print(f"{desenvolvedor.nome}: R$ {desenvolvedor.calcular_salario_final():.2f}")
print(f"Salario base do gerente: R$ {gerente.get_salario_base():.2f}")
