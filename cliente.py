from usuario import *
class Cliente(Usuario):

    def __init__(self, cpf, nome, endereco, telefone, email, nome_de_usuario, senha):
        super().__init__(cpf, nome, endereco, telefone, email, nome_de_usuario, senha)

