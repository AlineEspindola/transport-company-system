from funcionario import *
from produto import *
class Rota:

    def __init__(self, endereco_inicial, endereco_final, distancia, funcionario, motorista, transporte, produto, status, codigo):
        self.endereco_inicial=endereco_inicial
        self.endereco_final=endereco_final
        self.distancia=distancia
        Funcionario.funcionario=funcionario
        self.motorista=motorista
        Produto.produto=produto
        self.status=status
        self.transporte=transporte
        self.codigo=codigo
        self.quantidade_total=0
        self.peso_total=0
        self.espaco_total=0

    def getDistancia(self):
        return self.distancia
    def getEnderecoinicial(self):
        return self.endereco_inicial
    def getEnderecofinal(self):
        return self.endereco_final
    def getStatus(self):
        return self.status
    def getFuncionario(self):
        return Funcionario.funcionario
    def getMotorista(self):
        return self.motorista
    def getTransporte(self):
        return self.transporte
    def getCodigo(self):
        return self.codigo
    def getProduto(self):
        return Produto.produto
    def getQuantidadetotal(self):
        return self.quantidade_total
    def getPesototal(self):
        return self.peso_total
    def getEspacototal(self):
        return self.espaco_total

    def setDistancia(self, distancia):
        self.distancia=distancia
        return self.distancia
    def setEnderecoinicial(self, endereco_inicial):
        self.endereco_inicial=endereco_inicial
        return self.endereco_inicial
    def setEnderecofinal(self, endereco_final):
        self.endereco_final=endereco_final
        return self.endereco_final
    def setStatus(self, status):
        self.status=status
        return self.status
    def setFuncionario(self, funcionario):
        Funcionario.funcionario=funcionario
        return Funcionario.funcionario
    def setMotorista(self, motorista):
        self.motorista=motorista
        return self.motorista
    def setTransporte(self, transporte):
        self.transporte=transporte
        return self.transporte
    def setCodigo(self, codigo):
        self.codigo=codigo
        return self.codigo
    def setProduto(self, produto):
        Produto.produto=produto
        return Produto.produto
    def setQuantidadetotal(self, quantidade_total):
        self.quantidade_total=quantidade_total
        return self.quantidade_total
    def setPesototal(self, peso_total):
        self.peso_total=peso_total
        return self.peso_total
    def setEspacototal(self, espaco_total):
        self.espaco_total=espaco_total
        return self.espaco_total

    def consulta(self):
        print("ENDEREÇO INICIAL:", self.endereco_inicial)
        print("ENDEREÇO FINAL:", self.endereco_final)
        print("DISTÂNCIA:", self.distancia, "Km")
        print("QUANTIDADE TOTAL DE PRODUTOS:", self.quantidade_total)
        print("PESO TOTAL:", self.peso_total, "Kg")
        print("ESPAÇO TOTAL UTILIZADO:", self.espaco_total, "m³")
        print("STATUS:", self.status)
        print("FUNCIONÁRIO RESPONSÁVEL:", Funcionario.funcionario.getNome())
        print("MOTORISTA:", self.motorista)
        print("VEÍCULO:", self.transporte)
        print("CÓDIGO: #", self.codigo)

    def calcularEspacototal(self):
        i=0
        for x in Produto.produto:
            c=x.getComprimento()
            l=x.getLargura()
            p=x.getProfundidade()
            i=i+(x.getQuantidade()*(c*p*l))
        self.espaco_total=i

    def calcularPesototal(self):
        i=0
        for x in Produto.produto:
            i=i+(x.getPeso()*x.getQuantidade())
        self.peso_total=i

    def calcularQuantidadetotal(self):
        i=0
        for x in Produto.produto:
            i=i+x.getQuantidade()
        self.quantidade_total=i

