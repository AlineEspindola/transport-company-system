class Usuario:

    def __init__(self, cpf, nome, endereco, telefone, email, nome_de_usuario, senha):
        self.cpf=cpf
        self.nome=nome
        self.endereco=endereco
        self.telefone=telefone
        self.email=email
        self.nome_de_usuario=nome_de_usuario
        self.senha=senha

    def getCpf(self):
        return self.cpf
    def getNome(self):
        return self.nome
    def getEndereco(self):
        return self.endereco
    def getTelefone(self):
        return self.telefone
    def getEmail(self):
        return self.email
    def getNomedeusuario(self):
        return self.nome_de_usuario
    def getSenha(self):
        return self.senha

    def setCpf(self, cpf):
        self.cpf=cpf
        return self.cpf
    def setNome(self, nome):
        self.nome=nome
        return self.nome
    def setEndereco(self, endereco):
        self.endereco=endereco
        return self.endereco
    def setTelefone(self, telefone):
        self.telefone=telefone
        return self.telefone
    def setEmail(self, email):
        self.email=email
        return self.email
    def setNomedeusuario(self, nome_de_usuario):
        self.nome_de_usuario=nome_de_usuario
        return self.nome_de_usuario
    def setSenha(self, usuarios, senha):
        aux=0
        while aux==0:
            h=0
            for x in usuarios:
                if x.getSenha()==senha:
                    senha=str(input("SENHA JÁ EXISTENTE, DIGITE OUTRA: "))
                    h=1
            if h==0:
                aux=1
                self.senha=senha

    def consulta(self):
        print("NOME:", self.nome)
        print("CPF:", self.cpf)
        print("ENDEREÇO:", self.endereco)
        print("TELEFONE:", self.telefone)
        print("E-MAIL:", self.email)
        print("NOME DE USUÁRIO:", self.nome_de_usuario)

    def senhaUnica(self, usuarios):
        aux=0
        while aux==0:
            h=0
            for x in usuarios:
                if x.getSenha()==self.senha:
                    self.senha=str(input("OCORREU UM PROBLEMA NA SENHA, DIGITE OUTRA: "))
                    h=1
            if h==0:
                aux=1




