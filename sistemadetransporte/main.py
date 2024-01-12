from funcionario import Funcionario
from cliente import Cliente
from produto import Produto
from rota import Rota

frete=30
cliente1=Cliente("123", "Aline Espindola", "Rua Y", 8293642, "A@gmail.com", "A", "1")
produto1=Produto(1, "Cama", "Rua V", 5, 2, 6, "Baixa", 34, "Pix", cliente1, 1, "Rua X", "Pendente", frete)
produto2=Produto(2, "Porta", "Rua A", 3, 6, 6, "Baixa", 10, "Pix", cliente1, 1, "Rua X", "Pendente", frete)
funcionario1=Funcionario("123", "Sidney Espindola", "Rua P", 8245642, "S@gmail.com", "S", "1", 9500)

clientes=[cliente1]
produtos=[produto1, produto2]
funcionarios=[funcionario1]
rotas=[]

qr=0
qc=1
qp=2
qf=1

d="x"
dc="x"
df="x"
dl="x"

while d!="s" and d!="S":
    if dl!="f" and dl!="F" and dl!="c" and dl!="C":
        print("---------------------------------------------------------------------------------------")
        print("|                           SISTEMA DE TRANSPORTADORA                                 |")
        print("---------------------------------------------------------------------------------------")
        print("CADASTRO COMO FUNCIONÁRIO (F)           CADASTRO COMO CLIENTE (C)             LOGIN (L)")
        print("SAIR (S)")
        print("")
        d=str(input("DIGITE SUA RESPOSTA: "))

    #----------------------------------CADASTRO DO CLIENTE------------------------------------------
    if d=="c" or d=="C":
        if dc=="d" or dc=="D":
            dc="x"
        if dl!="c" and dl!="C":
            print("--------------------------------------------------------------------------------------")
            cpf=str(input("DIGITE SEU CPF: "))
            nome=str(input("DIGITE SEU NOME COMPLETO: "))
            endereco=str(input("DIGITE SEU ENDEREÇO: "))
            telefone=int(input("DIGITE SEU TELEFONE: "))
            email=str(input("DIGITE SEU E-MAIL: "))
            nome_de_usuario=str(input("DIGITE SEU NOME DE USUÁRIO: "))
            senha=str(input("DIGITE SUA SENHA: "))
            qc=qc+1
            if qc==1:
                cliente1=Cliente(cpf, nome, endereco, telefone, email, nome_de_usuario, senha)
                clientes.append(cliente1)
            elif qc==2:
                cliente2=Cliente(cpf, nome, endereco, telefone, email, nome_de_usuario, senha)
                cliente2.senhaUnica(clientes)
                clientes.append(cliente2)
            elif qc==3:
                cliente3=Cliente(cpf, nome, endereco, telefone, email, nome_de_usuario, senha)
                cliente3.senhaUnica(clientes)
                clientes.append(cliente3)
            elif qc==4:
                cliente4=Cliente(cpf, nome, endereco, telefone, email, nome_de_usuario, senha)
                cliente4.senhaUnica(clientes)
                clientes.append(cliente4)
            elif qc==5:
                cliente5=Cliente(cpf, nome, endereco, telefone, email, nome_de_usuario, senha)
                cliente5.senhaUnica(clientes)
                clientes.append(cliente5)
        dl="x"

        #-----------------------------------INTERFACE DO CLIENTE-------------------------------------------
        while dc!="d" and dc!="D":
           print("---------------------------------------------------------------------------------------")
           print("|                  BEM-VINDO, CLIENTE! O QUE GOSTARIA DE FAZER?                       |")
           print("---------------------------------------------------------------------------------------")
           print("CONSULTAR CADASTRO (C)          ALTERAR CADASTRO (A)               DELETAR CADASTRO (E)")
           print("CADASTRAR PRODUTO (S)           CONSULTAR PRODUTO (P)               ALTERAR PRODUTO (R)")
           print("DELETAR PRODUTO (L)             DESLOGAR (D)")
           print("")
           dc=str(input("DIGITE SUA RESPOSTA: "))

           #-------------------------------CONSULTA DO CADASTRO DO CLIENTE-------------------------------------
           if dc=="c" or dc=="C":
               print("---------------------------------------------------------------------------------------")
               senha=str(input("DIGITE SUA SENHA PARA CONSULTAR SEU CADASTRO: "))
               print("")
               for x in clientes:
                   if x.getSenha()==senha:
                       x.consulta()

           #-----------------------------------CADASTRO DO PRODUTO---------------------------------------------
           elif dc=="S" or dc=="s":
               print("---------------------------------------------------------------------------------------")
               senha=str(input("DIGITE SUA SENHA PARA CADASTRAR O PRODUTO: "))
               print("")
               for x in clientes:
                   if x.getSenha()==senha:
                       cliente=x
                       nome=str(input("NOME DO PRODUTO: "))
                       destino=str(input("DESTINO: "))
                       endereco_de_origem=str(input("ENDEREÇO DE ORIGEM: "))
                       peso=float(input("PESO: "))
                       largura=float(input("LARGURA: "))
                       comprimento=float(input("COMPRIMENTO: "))
                       profundidade=float(input("PROFUNDIDADE: "))
                       fragilidade=str(input("FRAGILIDADE: "))
                       quantidade=int(input("QUANTIDADE: "))
                       forma_de_pagamento=str(input("FORMA DE PAGAMENTO: "))
                       qp=qp+1
                       codigo=qp
                       if qp==1:
                           produto1=Produto(codigo, nome, destino, peso, largura, comprimento, fragilidade, quantidade, forma_de_pagamento, cliente, profundidade, endereco_de_origem, "Pendente", frete)
                           produtos.append(produto1)
                       elif qp==2:
                           produto2=Produto(codigo, nome, destino, peso, largura, comprimento, fragilidade, quantidade, forma_de_pagamento, cliente, profundidade, endereco_de_origem, "Pendente", frete)
                           produtos.append(produto2)
                       elif qp==3:
                           produto3=Produto(codigo, nome, destino, peso, largura, comprimento, fragilidade, quantidade, forma_de_pagamento, cliente, profundidade, endereco_de_origem, "Pendente", frete)
                           produtos.append(produto3)
                       elif qp==4:
                           produto4=Produto(codigo, nome, destino, peso, largura, comprimento, fragilidade, quantidade, forma_de_pagamento, cliente, profundidade, endereco_de_origem, "Pendente", frete)
                           produtos.append(produto4)
                       elif qp==5:
                           produto5=Produto(codigo, nome, destino, peso, largura, comprimento, fragilidade, quantidade, forma_de_pagamento, cliente, profundidade, endereco_de_origem, "Pendente", frete)
                           produtos.append(produto5)
                       print("")
                       print("O CÓDIGO DO PRODUTO É #",codigo,", VOCÊ PODERÁ CONSULTAR, ALTERAR E DELETAR O PRODUTO COM")
                       print("ESSE CÓDIGO")
                       print("")
                       print("CADASTRADO COM SUCESSO!")

           #------------------------------------CONSULTA DO PRODUTO--------------------------------------------
           elif dc=="p" or dc=="P":
               print("---------------------------------------------------------------------------------------")
               codigo=int(input("DIGITE O CÓDIGO DO PRODUTO PARA CONSULTÁ-LO: "))
               print("")
               for x in produtos:
                   if x.getCodigo()==codigo:
                       x.consulta()

           #-------------------------------DELETAR O CADASTRO DO CLIENTE---------------------------------------
           elif dc=="E" or dc=="e":
               print("---------------------------------------------------------------------------------------")
               senha=str(input("DIGITE SUA SENHA PARA DELETAR SEU CADASTRO: "))
               print("")
               for x in clientes:
                   if x.getSenha()==senha:
                       clientes.remove(x)
               dc="d"
               print("DELETADO COM SUCESSO!")

           #---------------------------------------DELETAR O PRODUTO-------------------------------------------
           elif dc=="l" or dc=="L":
               print("---------------------------------------------------------------------------------------")
               codigo=int(input("DIGITE O CÓDIGO DO PRODUTO PARA DELETÁ-LO: "))
               print("")
               for x in produtos:
                   if x.getCodigo()==codigo:
                       produtos.remove(x)
                       print("DELETADO COM SUCESSO!")

           #--------------------------------ALTERAR O CADASTRO DO CLIENTE--------------------------------------
           elif dc=="A" or dc=="a":
               print("---------------------------------------------------------------------------------------")
               senha=str(input("DIGITE SUA SENHA PARA ALTERAR SEU CADASTRO: "))
               print("")
               for x in clientes:
                   if x.getSenha()==senha:
                       cliente=x
                       print("O QUE VOCÊ GOSTARIA DE ALTERAR?")
                       print("")
                       print("CPF (C)   NOME (N)   ENDEREÇO (E)    TELEFONE (T)    E-MAIL (M)     NOME DE USUÁRIO (U)")
                       print("SENHA (S)")
                       print("")
                       dca=str(input("DIGITE SUA RESPOSTA: "))
                       print("")
                       if dca=="c" or dca=="C":
                           cpf=str(input("DIGITE O NOVO CPF: "))
                           cliente.setCpf(cpf)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dca=="n" or dca=="N":
                           nome=str(input("DIGITE SEU NOVO NOME: "))
                           cliente.setNome(nome)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dca=="E" or dca=="e":
                           endereco=str(input("DIGITE SEU NOVO ENDEREÇO: "))
                           cliente.setEndereco(endereco)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dca=="T" or dca=="t":
                           telefone=int(input("DIGITE SEU NOVO TELEFONE: "))
                           cliente.setTelefone(telefone)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dca=="M" or dca=="m":
                           email=str(input("DIGITE SEU NOVO E-MAIL: "))
                           cliente.setEmail(email)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dca=="U" or dca=="u":
                           nome_de_usuario=str(input("DIGITE SEU NOVO NOME DE USUÁRIO: "))
                           cliente.setNomedeusuario(nome_de_usuario)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dca=="S" or dca=="s":
                           senha=str(input("DIGITE SUA NOVA SENHA: "))
                           cliente.setSenha(clientes, senha)
                           print("")
                           print("ALTERADO COM SUCESSO!")

           #-------------------------------------ALTERAR PRODUTO-----------------------------------------------
           elif dc=="R" or dc=="r":
               print("---------------------------------------------------------------------------------------")
               codigo=int(input("DIGITE O CÓDIGO DO PRODUTO PARA ALTERÁ-LO: "))
               print("")
               for x in produtos:
                   if x.getCodigo()==codigo:
                       produto=x
                       print("O QUE VOCÊ GOSTARIA DE ALTERAR?")
                       print("")
                       print("NOME DO PRODUTO (N)         DESTINO (D)          ENDERECO DE ORIGEM (E)         PESO(P)")
                       print("LARGURA (L)                 COMPRIMENTO (C)      PROFUNDIDADE (R)       FRAGILIDADE (F)")
                       print("QUANTIDADE (Q)              FORMA DE PAGAMENTO (O)")
                       print("")
                       dcp=str(input("DIGITE SUA RESPOSTA: "))
                       print("")
                       if dcp=="N" or dcp=="n":
                           nome_do_produto=str(input("DIGITE UM NOVO NOME PARA O PRODUTO: "))
                           produto.setNomedoproduto(nome_do_produto)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dcp=="d" or dcp=="D":
                           destino=str(input("DIGITE UM NOVO DESTINO: "))
                           produto.setDestino(destino)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dcp=="E" or dcp=="e":
                           endereco_de_origem=str(input("DIGITE UM NOVO ENDEREÇO DE ORIGEM: "))
                           produto.setEnderecodeorigem(endereco_de_origem)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dcp=="P" or dcp=="p":
                           peso=float(input("DIGITE UM NOVO PESO: "))
                           produto.setPeso(peso)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dcp=="L" or dcp=="l":
                           largura=float(input("DIGITE UMA NOVA LARGURA: "))
                           produto.setLargura(largura)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dcp=="c" or dcp=="C":
                           comprimento=float(input("DIGITE UM NOVO COMPRIMENTO: "))
                           produto.setComprimento(comprimento)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dcp=="r" or dcp=="R":
                           profundidade=float(input("DIGITE UMA NOVA PROFUNDIDADE: "))
                           produto.setProfundidade(profundidade)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dcp=="F" or dcp=="f":
                           fragilidade=str(input("DIGITE UMA NOVA FRAGILIDADE: "))
                           produto.setFragilidade(fragilidade)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dcp=="Q" or dcp=="q":
                           quantidade=int(input("DIGITE UMA NOVA QUANTIDADE: "))
                           produto.setQuantidade(quantidade)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dcp=="O" or dcp=="o":
                           forma_de_pagamento=str(input("DIGITE UMA NOVA FORMA DE PAGAMENTO: "))
                           produto.setFormadepagamento(forma_de_pagamento)
                           print("")
                           print("ALTERADO COM SUCESSO!")

    #---------------------------------CADASTRO DO FUNCIONÁRIO------------------------------------------
    elif d=="f" or d=="F":
        if df=="d" or df=="D":
            df="x"
        if dl!="f" and dl!="F":
            print("--------------------------------------------------------------------------------------")
            cpf=str(input("DIGITE SEU CPF: "))
            nome=str(input("DIGITE SEU NOME COMPLETO: "))
            endereco=str(input("DIGITE SEU ENDEREÇO: "))
            telefone=int(input("DIGITE SEU TELEFONE: "))
            salario=float(input("DIGITE SEU SALÁRIO: "))
            email=str(input("DIGITE SEU E-MAIL: "))
            nome_de_usuario=str(input("DIGITE SEU NOME DE USUÁRIO: "))
            senha=str(input("DIGITE SUA SENHA: "))
            qf=qf+1
            if qf==1:
                funcionario1=Funcionario(cpf, nome, endereco, telefone, email, nome_de_usuario, senha, salario)
                funcionarios.append(funcionario1)
            elif qf==2:
                funcionario2=Funcionario(cpf, nome, endereco, telefone, email, nome_de_usuario, senha, salario)
                funcionario2.senhaUnica(funcionarios)
                funcionarios.append(funcionario2)
            elif qf==3:
                funcionario3=Funcionario(cpf, nome, endereco, telefone, email, nome_de_usuario, senha, salario)
                funcionario3.senhaUnica(funcionarios)
                funcionarios.append(funcionario3)
            elif qf==4:
                funcionario4=Funcionario(cpf, nome, endereco, telefone, email, nome_de_usuario, senha, salario)
                funcionario4.senhaUnica(funcionarios)
                funcionarios.append(funcionario4)
            elif qf==5:
                funcionario5=Funcionario(cpf, nome, endereco, telefone, email, nome_de_usuario, senha, salario)
                funcionario5.senhaUnica(funcionarios)
                funcionarios.append(funcionario5)
        dl="x"

        #---------------------------------INTERFACE DO FUNCIONÁRIO-----------------------------------------
        while df!="d" and df!="D":
           print("---------------------------------------------------------------------------------------")
           print("|                BEM-VINDO, FUNCIONÁRIO! O QUE GOSTARIA DE FAZER?                     |")
           print("---------------------------------------------------------------------------------------")
           print("CONSULTAR CADASTRO (C)          ALTERAR CADASTRO (A)               DELETAR CADASTRO (T)")
           print("CADASTRAR ROTA (R)              CONSULTAR ROTA (O)                     ALTERAR ROTA (L)")
           print("DELETAR ROTA (E)                CONSULTAR PRODUTOS (P)                DEFINIR FRETE (F)")
           print("CONSULTAR FRETE (S)             DESLOGAR (D)")
           print("")
           df=str(input("DIGITE SUA RESPOSTA: "))

           #------------------------------CONSULTA DO CADASTRO DO FUNCIONÁRIO---------------------------------
           if df=="c" or df=="C":
               print("---------------------------------------------------------------------------------------")
               senha=str(input("DIGITE SUA SENHA PARA CONSULTAR SEU CADASTRO: "))
               print("")
               for x in funcionarios:
                   if x.getSenha()==senha:
                       x.consulta()

           #------------------------------DELETAR O CADASTRO DO FUNCIONÁRIO-----------------------------------
           elif df=="t" or df=="T":
               print("---------------------------------------------------------------------------------------")
               senha=str(input("DIGITE SUA SENHA PARA DELETAR: "))
               print("")
               for x in funcionarios:
                   if x.getSenha()==senha:
                       funcionarios.remove(x)
               df="d"
               print("DELETADO COM SUCESSO!")

           #------------------------------ALTERAR O CADASTRO DO FUNCIONÁRIO-----------------------------------
           elif df=="A" or df=="a":
               print("---------------------------------------------------------------------------------------")
               senha=str(input("DIGITE SUA SENHA PARA ALTERAR SEU CADASTRO: "))
               print("")
               for x in funcionarios:
                   if x.getSenha()==senha:
                       funcionario=x
                       print("O QUE VOCÊ GOSTARIA DE ALTERAR?")
                       print("")
                       print("CPF (C)   NOME (N)   ENDEREÇO (E)    TELEFONE (T)    E-MAIL (M)     NOME DE USUÁRIO (U)")
                       print("SALÁRIO (L)          SENHA (S)")
                       print("")
                       dfa=str(input("DIGITE SUA RESPOSTA: "))
                       print("")
                       if dfa=="c" or dfa=="C":
                           cpf=str(input("DIGITE O NOVO CPF: "))
                           funcionario.setCpf(cpf)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfa=="n" or dfa=="N":
                           nome=str(input("DIGITE SEU NOVO NOME: "))
                           funcionario.setNome(nome)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfa=="E" or dfa=="e":
                           endereco=str(input("DIGITE SEU NOVO ENDEREÇO: "))
                           funcionario.setEndereco(endereco)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfa=="T" or dfa=="t":
                           telefone=int(input("DIGITE SEU NOVO TELEFONE: "))
                           funcionario.setTelefone(telefone)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfa=="M" or dfa=="m":
                           email=str(input("DIGITE SEU NOVO E-MAIL: "))
                           funcionario.setEmail(email)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfa=="U" or dfa=="u":
                           nome_de_usuario=str(input("DIGITE SEU NOVO NOME DE USUÁRIO: "))
                           funcionario.setNomedeusuario(nome_de_usuario)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfa=="L" or dfa=="l":
                           salario=float(input("DIGITE SEU NOVO SALÁRIO: "))
                           funcionario.setSalario(salario)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfa=="S" or dfa=="s":
                           senha=str(input("DIGITE SUA NOVA SENHA: "))
                           funcionario.setSenha(clientes, senha)
                           print("")
                           print("ALTERADO COM SUCESSO!")

           #-----------------------------------CONSULTAR PRODUTOS---------------------------------------------
           elif df=="p" or df=="P":
               for x in produtos:
                   print("---------------------------------------PRODUTO-----------------------------------------")
                   x.consulta()

           #--------------------------------------DEFINIR FRETE-----------------------------------------------
           elif df=="f" or df=="F":
               print("---------------------------------------------------------------------------------------")
               frete=float(input("DIGITE O PREÇO DO FRETE: "))
               print("")
               print("DEFINIDO O FRETE COM SUCESSO!")

           #-------------------------------------CONSULTAR FRETE----------------------------------------------
           elif df=="s" or df=="S":
               print("---------------------------------------------------------------------------------------")
               print("FRETE: R$", frete)

           #------------------------------------CADASTRO DA ROTA----------------------------------------------
           elif df=="R" or df=="r":
               print("---------------------------------------------------------------------------------------")
               senha=str(input("DIGITE SUA SENHA PARA CADASTRAR A ROTA: "))
               print("")
               produtosdarota=[]
               for x in funcionarios:
                   if x.getSenha()==senha:
                       funcionario=x
                       qr=qr+1
                       codigorota=qr
                       endereco_inicial=str(input("DIGITE O ENDEREÇO INICIAL: "))
                       endereco_final=str(input("DIGITE O ENDEREÇO FINAL: "))
                       distancia=int(input("DIGITE A DISTÂNCIA TOTAL: "))
                       status=str(input("DIGITE O STATUS DA ROTA: "))
                       motorista=str(input("DIGITE O NOME DO MOTORISTA: "))
                       transporte=str(input("DIGITE O TIPO DE TRANSPORTE: "))
                       q=int(input("DIGITE A QUANTIDADE DE PRODUTOS QUE DESEJA COLOCAR NA ROTA: "))
                       c=0
                       while c<q:
                           codigo=int(input("DIGITE O CÓDIGO DO PRODUTO: "))
                           for x in produtos:
                               if x.getCodigo()==codigo:
                                   produtosdarota.append(x)
                                   x.setStatus(status)
                           c=c+1
                       if qr==1:
                           produtosdarota1=produtosdarota
                           rota1=Rota(endereco_inicial, endereco_final, distancia, funcionario, motorista, transporte, produtosdarota1, status, codigorota)
                           rota1.calcularQuantidadetotal()
                           rota1.calcularPesototal()
                           rota1.calcularEspacototal()
                           rotas.append(rota1)
                       elif qr==2:
                           produtosdarota2=produtosdarota
                           rota2=Rota(endereco_inicial, endereco_final, distancia, funcionario, motorista, transporte, produtosdarota2, status, codigorota)
                           rota2.calcularQuantidadetotal()
                           rota2.calcularPesototal()
                           rota2.calcularEspacototal()
                           rotas.append(rota2)
                       elif qr==3:
                           produtosdarota3=produtosdarota
                           rota3=Rota(endereco_inicial, endereco_final, distancia, funcionario, motorista, transporte, produtosdarota3, status, codigorota)
                           rota3.calcularQuantidadetotal()
                           rota3.calcularPesototal()
                           rota3.calcularEspacototal()
                           rotas.append(rota3)
                       elif qr==4:
                           produtosdarota4=produtosdarota
                           rota4=Rota(endereco_inicial, endereco_final, distancia, funcionario, motorista, transporte, produtosdarota4, status, codigorota)
                           rota4.calcularQuantidadetotal()
                           rota4.calcularPesototal()
                           rota4.calcularEspacototal()
                           rotas.append(rota4)
                       elif qr==5:
                           produtosdarota5=produtosdarota
                           rota5=Rota(endereco_inicial, endereco_final, distancia, funcionario, motorista, transporte, produtosdarota5, status, codigorota)
                           rota5.calcularQuantidadetotal()
                           rota5.calcularPesototal()
                           rota5.calcularEspacototal()
                           rotas.append(rota5)
                       print("")
                       print("O CÓDIGO DA ROTA É #", codigorota, ", VOCÊ PODERÁ CONSULTAR, ALTERAR E DELETAR A ROTA COM")
                       print("ESSE CÓDIGO")
                       print("")
                       print("CADASTRADO COM SUCESSO!")

           #------------------------------------CONSULTA DA ROTA----------------------------------------------
           elif df=="o" or df=="O":
               print("---------------------------------------------------------------------------------------")
               codigo=int(input("DIGITE O CÓDIGO DA ROTA PARA CONSULTÁ-LA: "))
               print("")
               for x in rotas:
                   if x.getCodigo()==codigo:
                       x.consulta()
                       for y in x.getProduto():
                           print("------------------------------------PRODUTO--------------------------------------------")
                           y.consulta()

           #------------------------------------ALTERAR A ROTA------------------------------------------------
           elif df=="l" or df=="L":
               print("---------------------------------------------------------------------------------------")
               codigo=int(input("DIGITE O CÓDIGO DA ROTA PARA ALTERÁ-LA: "))
               print("")
               for x in rotas:
                   if x.getCodigo()==codigo:
                       rota=x
                       print("DIGITE O QUE DESEJA ALTERAR?")
                       print("")
                       print("ENDEREÇO INICIAL (E)   ENDEREÇO FINAL (F)  DISTÃNCIA (D)  MOTORISTA (M)  TRANSPORTE (T)")
                       print("STATUS (S)")
                       print("")
                       dfr=str(input("DIGITE SUA RESPOSTA: "))
                       print("")
                       if dfr=="E" or dfr=="e":
                           endereco_inicial=str(input("DIGITE O NOVO ENDEREÇO INICIAL: "))
                           rota.setEnderecoinicial(endereco_inicial)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfr=="F" or dfr=="f":
                           endereco_final=str(input("DIGITE UM NOVO ENDEREÇO FINAL: "))
                           rota.setEnderecofinal(endereco_final)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfr=="D" or dfr=="d":
                           distancia=int(input("DIGITE UMA NOVA DISTÂNCIA: "))
                           rota.setDistancia(distancia)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfr=="M" or dfr=="m":
                           motorista=str(input("DIGITE UM NOVO NOME DE MOTORISTA: "))
                           rota.setMotorista(motorista)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfr=="t" or dfr=="T":
                           transporte=str(input("DIGITE UM NOVO TIPO DE TRANSPORTE: "))
                           rota.setTransporte(transporte)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                       elif dfr=="s" or dfr=="S":
                           status=str(input("DIGITE UM NOVO STATUS: "))
                           rota.setStatus(status)
                           print("")
                           print("ALTERADO COM SUCESSO!")
                           for y in rota.getProduto():
                               y.setStatus(status)

           #------------------------------------DELETAR A ROTA------------------------------------------------
           elif df=="E" or df=="e":
               print("---------------------------------------------------------------------------------------")
               codigo=int(input("DIGITE O CÓDIGO DA ROTA PARA DELETÁ-LA: "))
               print("")
               print("DELETADO COM SUCESSO!")
               for x in rotas:
                   if x.getCodigo()==codigo:
                       rotas.remove(x)

    #----------------------------------------LOGIN-----------------------------------------------------
    while d=="l" or d=="L":
        print("---------------------------------------------------------------------------------------")
        print("O QUE VOCÊ É? ")
        print("")
        print("FUNCIONÁRIO (F)                                                             CLIENTE (C)")
        print("")
        dl=str(input("DIGITE SUA RESPOSTA: "))
        if dl=="F" or dl=="f":
            print("")
            senha=str(input("DIGITE SUA SENHA: "))
            for x in funcionarios:
                if x.getSenha()==senha:
                    d="f"
        elif dl=="c" or dl=="C":
            print("")
            senha=str(input("DIGITE SUA SENHA: "))
            for x in clientes:
                if x.getSenha()==senha:
                    d="c"





