# 🚚 Sistema de Transportadora 🚚
Um projeto criado no curso técnico de informática para uma empresa fictícia de transportadora. É um sistema que serve para os clientes cadastrarem seus produtos e os funcionários receberem esses itens e colocarem na rota correta. Como o intuito era aprender, é apenas um sistema básico para aprimorar os conhecimentos na engenharia de software de forma geral.

![sistemadetransportadora](https://github.com/AlineEspindola/SistemadeTransportadora/assets/117865319/fe57a058-fd9b-4286-a1d4-27d6cbaff439)

## Como Executar 📁
Clone normalmente este repositório no Visual Studio. Baixe uma extensão que permite executar arquivos .exe, como exe Runner. No arquivo main.exe, clique com botão direito e escolha a opção "Run Executable".

## Como foi feito 🔍
Por meio das aulas de engenharia de software, fui construindo esse sistema.

Primeiramente, criei uma entrevista fictícia para montar os requisitos do software:

-  O que você quer no seu sistema? 
-  Quais informações você quer no cadastro do cliente? (nome, CPF, email, telefone, endereço)
-  Quais informações você quer no cadastro do funcionário? (nome, CPF, email, telefone, endereço)
-  Como o cliente se conectará com a transportadora? (sistematizado, mensagem)
-  Quais dados do objeto você quer? (fragilidade, peso, tamanho)
-  Quais informações da rota você quer? (distância, tempo, dificuldade, tráfego) 
-  Como o frete se relaciona com a rota? (distância)
-  Como você quer que seja como a interface (simples, complexa)
-  Como será a forma de pagamento (única ou diversa, cartão, pix, cheque, boleto)

Após isso, elaborei casos de uso e fiz o levantamento de requisitos, explicando as funções que teria no sistema. Elaborei um arquivo pdf dos requisitos que está no repositório junto com o restante dos arquivos e os casos de uso seguem abaixo. Se observarem, o software não irá atender todos os requisitos, por conta da duração da disciplina.

### 1. CASO DE USO: REALIZAR LOGIN
Ator(es): Funcionário e cliente

Fluxo principal:
1- Usuário abre programa
2- Sistema mostra a tela de login
3- Usuário digita login e senha nos campos apropriados
4- Sistema autentica o usuário e mostra a interface principal

Tratamento de Exceções
4- Login incorreto
4a1- Sistema exibe mensagem “login incorreto”
4a2- Sistema solicita login novamente
4a3- Usuário preenche o campo login
4a4- Sistema faz reconhecimento do campo

### 2. CASO DE USO: CADASTRAR FUNCIONÁRIO
Ator(es): Funcionário 

Pré-condição: Caso de uso: realizar login

Fluxo Principal:
1- Usuário clica na opção “Cadastro do Funcionário”
2- Sistema abre a página de cadastro e solicita CPF, nome, endereço, telefone, e-mail, nome de usuário e senha.
3- Usuário preenche os campos e seleciona o botão “Cadastrar”
4- Sistema mostra campo para inserir o código do funcionário
5- Usuário preenche o campo
6- Sistema salva o cadastro

Tratamento de exceções:
5- Cliente cadastrando como funcionário:
5a1- Sistema exibe uma mensagem “Colocar o código de funcionário da imprensa”
5a2- Usuário preenche o campo código
5a3- Sistema faz o reconhecimento do campo

3- CPF inválido:
3a1 Sistema exibe uma mensagem “CPF inválido”
3a2 Sistema solicita CPF novamente
3a3 Usuário preenche o campo CPF
3a4 Sistema faz o reconhecimento dos campos obrigatórios

3- Funcionário já cadastrado:
3b1 Sistema verifica que já existe o CPF cadastrado e exibe uma mensagem
informando que o usuário já está cadastrado

3- Nome de usuário já cadastrado:
3c1 Sistema verifica que já existe o nome de usuário cadastrado e exibe uma
mensagem que o nome de usuário já está em uso

### 3- CASO DE USO: CADASTRAR CLIENTE
Ator(es): Cliente

Pré-condição: Caso de uso: realizar login

Fluxo Principal:
1- Usuário clica na opção “Cadastro do Cliente”
2- Sistema abre a página de cadastro e solicita CPF, nome, endereço, telefone,
e-mail, nome de usuário e senha
3. Usuário preenche os campos e seleciona o botão “Cadastrar”
4. Sistema salva o cadastro

Tratamento de exceções
3- CPF inválido:
3a1 Sistema exibe uma mensagem “CPF inválido”
3a2 Sistema solicita CPF novamente
3a3 Usuário preenche o campo CPF
3a4 Sistema faz o reconhecimento dos campos obrigatórios

3- Cliente já cadastrado:
3b1 Sistema verifica que já existe o CPF cadastro e exibe uma mensagem
informando que o cliente já está cadastrado

3- Nome de usuário já cadastrado:
3c1 Sistema verifica que já existe o nome de usuário cadastrado e exibe uma
mensagem que o nome de usuário já está em uso.

### 4. CASO DE USO: CADASTRAR PRODUTO
Ator(es): Cliente

Pré-condição: Caso de uso: realizar login

Fluxo principal:
1- Usuário clica na opção “Produto”.
2- Usuário clica na opção “Cadastrar Produto”.
3- Sistema abre a página de cadastro e solicita nome do produto, nome do usuário, destino, peso, tamanho, fragilidade, quantidade, frete e forma de pagamento
4- Usuário preenche os campos e seleciona o botão “Cadastrar”
5- Sistema salva o cadastro

### 5. CASO DE USO: EXCLUIR PRODUTO
Ator(es): Cliente e funcionário

Pré-condição: Caso de uso: realizar login e Caso de uso: cadastrar produto

Fluxo principal:
1- Usuário clica na opção “Produto”.
2- Sistema exibe “Lista de produtos”
3- Usuário clica na opção “Excluir produto”
4- Usuário clica na opção "Confirmar exclusão”
5- Sistema exclui o produto

### 6. CASO DE USO: ALTERAR AS INFORMAÇÕES DA ROTA DO PRODUTO
Ator(es): Funcionário

Pré-condição: Caso de uso: realizar login e Caso de uso: consultar o produto

Fluxo Principal:
1- Usuário clica na opção “Produto”.
2- Sistema exibe “Lista de produtos”.
3- Usuário clica na opção “Alterar as informações do produto”
4- Usuário clica na informação da rota que deseja mudar
5- Usuário altera informação
6- Usuário clica em “salvar”
7- Sistema salva alteração

### 7. CASO DE USO: ALTERAR AS INFORMAÇÕES BÁSICAS DO PRODUTO
Ator(es): Cliente

Pré-condição: Caso de uso: realizar login e Caso de uso: consultar o produto

Fluxo Principal:
1- Usuário clica na opção “Produto”
2- Sistema exibe “Lista de produtos”
3- Usuário clica na opção “Alterar as informações do produto”
4- Usuário clica na informação que deseja mudar do produto
5- Usuário altera informação
6- Usuário clica em “salvar”
7- Sistema salva alteração

### 8. CASO DE USO: EXCLUIR CADASTRO DO FUNCIONÁRIO
Ator(es): Funcionário

Pré-condição: Caso de uso: realizar login

Fluxo Principal:
1- Usuário clica na opção “Cadastro do Funcionário”
2- Usuário clica na opção “Excluir cadastro”
3- Usuário clica na opção "Confirmar exclusão”
4- Sistema exclui o cadastro do funcionário

### 9. CASO DE USO: ALTERAR O CADASTRO DO FUNCIONÁRIO
Ator(es): Funcionário

Pré-condição: Caso de uso: realizar login e Caso de uso: consultar cadastro do funcionário

Fluxo Principal:
1- Usuário clica na opção “Cadastro do Funcionário”
2- Usuário clica na opção “Alterar cadastro”
3- Usuário clica na informação que deseja mudar
4- Usuário altera informação.
5- Usuário clica em “salvar”
6- Sistema salva alteração

### 10. CASO DE USO: ALTERAR CADASTRO DO CLIENTE
Ator(es): Cliente

Pré-condição: Caso de uso: realizar login e Caso de uso: consultar o cadastro do cliente

Fluxo Principal
1- Usuário clica na opção “Cadastro do Cliente”
2- Usuário clica na opção “Alterar cadastro”
4- Usuário clica na informação que deseja mudar
5- Usuário altera informação.
6- Usuário clica em “salvar”
7- Sistema salva alteração

### 11. CASO DE USO: EXCLUIR CADASTRO DO CLIENTE
Ator(es): Cliente

Pré-condição: Caso de uso: realizar login

Fluxo Principal
1- Usuário clica na opção “Cadastro do Cliente”.
2- Usuário clica na opção “Excluir cadastro”.
3- Usuário clica na opção "Confirmar exclusão”.
4- Sistema exclui o cadastro do cliente.

### 12. CASO DE USO: CONSULTAR O CADASTRO DE FUNCIONÁRIO
Ator(es): Funcionário

Pré-condição: Caso de uso: realizar login

Fluxo Principal
1- Usuário clica na opção “Cadastro do Funcionário”
2- Sistema exibe as informações do cadastro

### 13. CASO DE USO: CONSULTAR O CADASTRO DE CLIENTE
Ator(es): Cliente

Pré-condição: Caso de uso: realizar login

Fluxo Principal
1- Usuário clica na opção “Cadastro do cliente”
2- Sistema exibe as informações do cadastro

### 14. CASO DE USO: CONSULTAR O PRODUTO
Ator(es): Cliente e funcionário

Pré-condição: Caso de uso: realizar login

Fluxo Principal
1- Usuário clica na opção “Produto”.
2- Sistema exibe a “Lista de Produtos”
3- Usuário pesquisa o nome do produto no campo de busca
4- Usuário clica em um produto específico.
5- Sistema exibe as informações do produto

Também criei diagramas para visualizar melhor esses casos.

![diagrama1](https://github.com/AlineEspindola/SistemadeTransportadora/assets/117865319/aa405850-e930-432a-ab8c-a1ef1768b8fe)

![diagrama2](https://github.com/AlineEspindola/SistemadeTransportadora/assets/117865319/ccbf3aef-8910-4d16-882d-25b11f8355b9)

## Conclusão

O projeto de sistema de transportadora, desenvolvido durante o meu curso técnico de informática, proporcionou uma valiosa experiência na aplicação prática de conceitos de engenharia de software para mim. A abordagem, que incluiu entrevistas fictícias, levantamento de requisitos, casos de uso e diagramas, permitiu uma compreensão clara das necessidades dos usuários. Apesar das limitações da duração da disciplina, a elaboração dos casos de uso e diagramas ofereceu uma visão organizada das funcionalidades do sistema. A experiência adquirida, especialmente ao lidar com restrições de tempo, será fundamental para futuros projetos na área de desenvolvimento de software.

<hr>

<div align="center">
<h3>꧁ 🔴 Autoria: Aline Espindola 🔴 ꧂</h3>

[![Behance](https://img.shields.io/badge/-Behance-blue?style=for-the-badge&logo=behance&logoColor=white)](https://www.behance.net/line14)
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aline-espindola-72034b285)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&to=alineabreuespindola@gmail.com)
  
</div>

<hr>

### Licença: MIT






