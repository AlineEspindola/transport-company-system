from usuario import *
class Funcionario(Usuario):

    def __init__(self, cpf, nome, endereco, telefone, email, nome_de_usuario, senha, salario):
        super().__init__(cpf, nome, endereco, telefone, email, nome_de_usuario, senha)
        self.salario=salario

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario=salario
        return self.salario

    def consulta(self):
        print("NOME:", self.nome)
        print("CPF:", self.cpf)
        print("ENDEREÇO:", self.endereco)
        print("TELEFONE:", self.telefone)
        print("E-MAIL:", self.email)
        print("NOME DE USUÁRIO:", self.nome_de_usuario)
        print("SALÁRIO: R$", self.salario)
