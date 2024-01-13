from cliente import *
class Produto:

    def __init__(self, codigo, nome_do_produto, destino, peso, largura, comprimento, fragilidade, quantidade, forma_de_pagamento, cliente, profundidade, endereco_de_origem, status, frete):
        self.nome_do_produto=nome_do_produto
        self.destino=destino
        self.peso=peso
        self.largura=largura
        self.comprimento=comprimento
        self.fragilidade=fragilidade
        self.quantidade=quantidade
        self.forma_de_pagamento=forma_de_pagamento
        Cliente.cliente=cliente
        self.profundidade=profundidade
        self.endereco_de_origem=endereco_de_origem
        self.codigo=codigo
        self.status=status
        self.frete=frete

    def getCodigo(self):
        return self.codigo
    def getNomedoproduto(self):
        return self.nome_do_produto
    def getDestino(self):
        return self.destino
    def getPeso(self):
        return self.peso
    def getLargura(self):
        return self.largura
    def getComprimento(self):
        return self.comprimento
    def getFragilidade(self):
        return self.fragilidade
    def getQuantidade(self):
        return self.quantidade
    def getFormadepagamento(self):
        return self.forma_de_pagamento
    def getProfundidade(self):
        return self.profundidade
    def getCliente(self):
        return Cliente.cliente
    def getEnderecodeorigem(self):
        return self.endereco_de_origem
    def getStatus(self):
        return self.status
    def getFrete(self):
        return self.frete

    def setCodigo(self, codigo):
        self.codigo=codigo
        return self.codigo
    def setNomedoproduto(self, nome_do_produto):
        self.nome_do_produto=nome_do_produto
        return self.nome_do_produto
    def setDestino(self, destino):
        self.destino=destino
        return self.destino
    def setPeso(self, peso):
        self.peso=peso
        return self.peso
    def setLargura(self, largura):
        self.largura=largura
        return self.largura
    def setComprimento(self, comprimento):
        self.comprimento=comprimento
        return self.comprimento
    def setFragilidade(self, fragilidade):
        self.fragilidade=fragilidade
        return self.fragilidade
    def setQuantidade(self, quantidade):
        self.quantidade=quantidade
        return self.quantidade
    def setFormadepagamento(self, forma_de_pagamento):
        self.forma_de_pagamento=forma_de_pagamento
        return self.forma_de_pagamento
    def setProfundidade(self, profundidade):
        self.profundidade=profundidade
        return self.profundidade
    def setCliente(self, cliente):
        Cliente.cliente=cliente
        return Cliente.cliente
    def setEnderecodeorigem(self, endereco_de_origem):
        self.endereco_de_origem=endereco_de_origem
        return self.endereco_de_origem
    def setStatus(self, status):
        self.status=status
        return self.status
    def setFrete(self, frete):
        self.frete=frete
        return self.frete

    def consulta(self):
        print("NOME DO PRODUTO:", self.nome_do_produto)
        print("CLIENTE:", Cliente.cliente.getNome())
        print("DESTINO:", self.destino)
        print("ENDEREÇO DE ORIGEM:", self.endereco_de_origem)
        print("PESO:", self.peso, "Kg")
        print("COMPRIMENTO:", self.comprimento, "m")
        print("LARGURA:", self.largura, "m")
        print("PROFUNDIDADE:", self.profundidade, "m")
        print("FRAGILIDADE:", self.fragilidade)
        print("QUANTIDADE:", self.quantidade)
        print("FRETE: R$", self.frete)
        print("FORMA DE PAGAMENTO:", self.forma_de_pagamento)
        print("STATUS:", self.status)
        print("CÓDIGO: #", self.codigo)
