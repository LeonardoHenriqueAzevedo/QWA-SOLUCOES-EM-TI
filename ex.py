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

candidatos = input(
    f"Quantos candidatos deseja cadastrar (Máximo de {max_vagas} candidatos): ")
while candidatos == "":
    candidatos = input(
        f"\033[1;31mErro! Informe novamente quantos candidatos deseja cadastrar (Máximo de {max_vagas} candidatos): \033[m")
candidatos = int(candidatos)

if candidatos > max_vagas:
    print(
        f"\033[1;31mErro! Não pode cadastrar mais que {max_vagas} candidatos nesse momento\033[m")
    candidatos = int(input(
        f"Quantos candidatos deseja cadastrar (Máximo de {max_vagas} candidatos): "))

print(f"Cadastrando {candidatos} candidatos")

while contador < candidatos:
    # Nome
    nome = input(
        f"Informe o nome do {contador + 1}° candidato: ")
    while nome == "":
        nome = input(
            f"\033[1;31mErro! Informe novamente o nome do {contador + 1}° candidato: \033[m")
    lista_nomes.append(nome)

    # Sobrenome
    sobrenome = input(
        f"Informe o sobrenome do candidato: ")
    while sobrenome == "":
        sobrenome = input(
            f"\033[1;31mErro! Informe novamente o sobrenome do candidato: \033[m")
    lista_sobrenomes.append(sobrenome)

    # CPF
    cpf = input(
        f"Informe o CPF do candidato: ")
    while cpf == "":
        cpf = input(
            f"\033[1;31mErro! Informe novamente o CPF do candidato: \033[m")
    cpf = float(cpf)
    for i in lista_cpfs:
        while i == cpf:
            cpf = float(input(
                f"\033[1;31mErro! Esse CPF já existe em nossos dados, informe novamente o CPF do candidato: \033[m"))
    lista_cpfs.append(cpf)

    # Data de Nascimento
    dia = input(
        f"Informe o dia em que o candidato nasceu: ")
    while dia == "":
        dia = input(
            f"\033[1;31mErro! Informe novamente o dia em que o candidato nasceu: \033[m")
    dia = int(dia)

    mes = input(
        f"Informe o mês em que o candidato nasceu: ")
    while mes == "":
        mes = input(
            f"\033[1;31mErro! Informe novamente o mês em que o candidato nasceu: \033[m")
    mes = int(mes)

    ano = input(
        f"Informe o ano em que o candidato nasceu: ")
    while ano == "":
        ano = input(
            f"\033[1;31mErro! Informe novamente o ano em que o candidato nasceu: \033[m")
    ano = int(ano)

    dataNasc = datetime.date(ano, mes, dia)
    lista_datanasc.append(dataNasc)

    # Maior de Idade
    diferenca_datas = (data_atual - dataNasc)
    idade = diferenca_datas.days / 365
    if idade >= 18:
        lista_maior_idade.append("Sim")
    else:
        lista_maior_idade.append("Não")

    # Vaga
    vaga = input(
        f"Informe a vaga que o candidato foi associado: ")
    while vaga == "":
        vaga = input(
            f"\033[1;31mErro! Informe novamente a vaga que o candidato foi associado: \033[m")
    lista_vaga.append(vaga)

    print("\033[1;32mCandidato Cadastrado com Sucesso!\033[m")

    contador += 1

print("=====================================================================")
print("\033[1;32mTodos os Candidatos foram cadastros!\033[m")

revisar = input("Gostaria de revisar todos os candidatos cadastrados? [S/N]: ")
while revisar == "":
    revisar = input(
        f"\033[1;31mErro! Gostaria de revisar todos os candidatos cadastrados? [S/N]: \033[m")

if revisar[0].capitalize() == "S":
    contador = 0
    print("")
    while contador < candidatos:
        print("========================================")
        print(f"Nome: {lista_nomes[contador]}")
        print(f"Sobrenome: {lista_sobrenomes[contador]}")
        print(f"CPF: {lista_cpfs[contador]}")
        print(f"Data de Nascimento: {lista_datanasc[contador]}")
        print(f"Maior de Idade: {lista_maior_idade[contador]}")
        print(f"Vaga: {lista_vaga[contador]}")
        print("========================================")
        contador += 1

if revisar[0].capitalize() == "N":
    print("Finalizado sistema de cadastro de candidatos!")
