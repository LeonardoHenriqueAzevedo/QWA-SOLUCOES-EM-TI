# Problema: Contratação
# Utilizando orientação a objetos criar uma aplicação que insira uma pessoa em uma
# lista e valide os dados da pessoa.

# A estrutura que representará a pessoa deve possuir os seguintes atributos:
# Nome
# Sobrenome
# CPF
# Data de Nascimento

# Todas as informações são obrigatórias.


# Caso alguma informação não seja preenchida deve-se apresentar uma mensagem
# informando que a informação específica é obrigatória e que a pessoa não foi adicionada à lista.
# Ex: de mensagem: "A data de nascimento é obrigatória. O Cliente não foi adicionado à lista".


# Não deve ser possível adicionar pessoas com o mesmo CPF. Validar quantidade total de candidatos por vaga.


# Associar candidato por vaga. A listagem de pessoas deve conter as informações:


# Nome
# Sobrenome
# CPF
# Data de nascimento
# É maior de idade?
# Vaga


# A empresa XPTO precisa fazer um sistema de cadastro de candidatos para seu programa de Trainee.
# O cadastro será feito em 2 momentos, mas na mesma tela.

# 1º será para adicionar as informações do candidato.

# 2º agrupar os candidatos preenchidos no passo anterior em uma tabela/grid para ao clicar no botão de SALVAR enviar para gravar
# todos de uma única vez.

# Inicialmente o usuário precisará fazer o cadastro de acordo com o nº de vagas disponíveis na empresa, o primeiro processo
# será de 5 vagas, a quantidade máxima de candidatos por vaga será 3, caso o usuário tente cadastrar mais candidatos do que
# vagas o sistema precisa validar e avisar que o nº de candidatos já atingiu o limite permitido.

# As informações necessárias para inserir um candidato é Nome, Sobrenome, CPF e Data de nascimento e Vaga, todas as
# informações são obrigatórias, caso não for preenchido o usuário deve ser avisado sobre qual campo está com problema
# e o mesmo candidato não pode ser inserido 2 vezes.

# A tabela que irá agrupar os candidatos vai conter as informações Nome, Sobrenome, CPF, Data de Nascimento, Idade,
# É maior de idade? e Vaga (ao qual o candidato foi associado). E por fim um botão para confirmar o cadastro de todos os
# candidatos e avisar ao usuário que os candidatos foram cadastrados com sucesso.
import datetime

print("Sistema de Cadastro de Candidatos")
print("=========================================")

lista_nomes = []
lista_sobrenomes = []
lista_cpfs = []
lista_datanasc = []
lista_maior_idade = []
lista_vaga = []

# Capturando data atual
data = datetime.datetime.now()
data_atual = data.date()

contador = 0
quantidade_vagas = 5
max_vagas = quantidade_vagas * 3
candidatos = int(input(
    f"Quantos candidatos deseja cadastrar (Máximo de {max_vagas} candidatos): "))

if candidatos > max_vagas:
    print(
        f"Erro! Não pode cadastrar mais que {max_vagas} candidatos nesse momento")
    candidatos = int(input(
        f"Quantos candidatos deseja cadastrar (Máximo de {max_vagas} candidatos): "))

print(f"Cadastrando {candidatos} candidatos")

while contador < candidatos:
    # Nome
    nome = input(
        f"Informe o nome do {contador + 1}° candidato: ")
    while nome == "":
        nome = input(
            f"Erro! Informe novamente o nome do {contador + 1}° candidato: ")
    lista_nomes.append(nome)

    # Sobrenome
    sobrenome = input(
        f"Informe o sobrenome do candidato: ")
    while sobrenome == "":
        sobrenome = input(
            f"Erro! Informe novamente o sobrenome do candidato: ")
    lista_sobrenomes.append(sobrenome)

    # CPF
    cpf = input(
        f"Informe o CPF do candidato: ")
    while cpf == "":
        cpf = input(
            f"Erro! Informe novamente o CPF do candidato: ")
    cpf = float(cpf)
    for i in lista_cpfs:
        if i == cpf:
            cpf = input(
                f"Erro! Esse CPF já existe em nossos dados, informe novamente o CPF do candidato: ")
    lista_cpfs.append(cpf)

    # Data de Nascimento
    dia = int(input(
        f"Informe o dia em que o candidato: "))
    mes = int(input(
        f"Informe o mês em que o candidato: "))
    ano = int(input(
        f"Informe o ano em que o candidato: "))
    dataNasc = datetime.date(ano, mes, dia)
    lista_datanasc.append(dataNasc)

    # Maior de Idade
    diferenca_datas = (data_atual - dataNasc)
    idade = diferenca_datas.days / 365
    if idade >= 18:
        lista_maior_idade.append("Maior de Idade")
    else:
        lista_maior_idade.append("Menor de Idade")

    # Vaga
    vaga = input(
        f"Informe a vaga que o candidato foi associado: ")
    while vaga == "":
        vaga = input(
            f"Erro! Informe novamente a vaga que o candidato foi associado: ")
    lista_vaga.append(vaga)

    print("Candidato Cadastrado com Sucesso!")

    contador += 1

print("Todos os Candidatos foram cadastros!")

revisar = input("Gostaria de revisar todos os candidatos cadastrados? [S/N] ")
while revisar == "":
    revisar = input(
        f"Erro! Gostaria de revisar todos os candidatos cadastrados? [S/N] ")

if revisar[0].capitalize() == "S":
    print("Oi")
if revisar[0].capitalize() == "N":
    print("Finalizando sistema de cadastro de candidatos!")
