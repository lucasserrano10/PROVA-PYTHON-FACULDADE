from time import sleep
vinhos = ['MERLOT', 'BRANCO', 'SAUVIGNON']
preco = [25, 100, 59]

def mensagemFinal(nome,endereco,total,frete):
    print(f' {nome},\n O SEU PRODUTO SERÁ ENTREGUE NO ENDEREÇO {endereco}\n NO VALOR TOTAL DE {total}R$ \n COM O FRETE DE {frete}R$')

def boasVindas():
    print(f'=' * 30)
    print(f'      VINHERIA AGNELLO')
    print(f'=' * 30)


def verificarNumero(msg,msgerro):
    saida = input(msg)
    while not saida.isnumeric():
        print(msgerro)
        saida = input(msg)
    print('BOA ESCOLHA !')
    print(f'=' * 30)
    return int(saida)


def mostrarVinhos():
    print(f'AQUI ESTÁ NOSSAS OPÇÕES DE VINHOS !')
    for i in range(len(vinhos)):
        print(f'{i + 1} --- {vinhos[i]} --- {preco[i]}R$')
    print(f'=' * 30)


def verificarIdade(number):
    idade = 2024 - number
    return idade


def maisCaro():
    print(f'=' * 60)
    caro = preco[0]
    indice_caro = 0
    for i,preco_vinho in enumerate(preco):
        if preco_vinho > caro:
            caro = preco_vinho
            indice_caro = i
    print(f'O VINHO MAIS CARO DE NOSSA VINHERIA É O {vinhos[indice_caro]} --- {caro}R$')
    print(f'=' * 60)

def maisBarato():
    barato = preco[0]
    indice_mais_barato = 0
    for i,preco_vinho in enumerate(preco):
        if preco_vinho < barato:
            barato = preco_vinho
            indice_mais_barato = i
    print(f'O VINHO MAIS BARATO DE NOSSA VINHERIA É O {vinhos[indice_mais_barato]} --- {barato}R$')
    print(f'=' * 60)

def calcularFrete(total):
    frete = 0
    if total < 500:
        print(f'VOCÊ NÃO GANHOU FRETE GRÁTIS, FALTAM {500 - total}R$ EM COMPRAS')
        frete += 25
    else:
        print('VOCÊ GANHOU FRETE GRÁTIS !')
    return frete

def realizarCompra():
    total = 0
    boasVindas()
    nome = str(input('NOME ->'))
    endereco = str(input('DIGITE O ENDEREÇO DE ENTREGA ->'))
    anoNascimento = int(input('DIGITE SEU ANO DE NASCIMENTO  [YYYY] ->'))
    check = verificarIdade(anoNascimento)
    if check >= 18:
        maisCaro()
        maisBarato()
        mostrarVinhos()
        while True:
            opcao = str(input('ESCOLHA O VINHO QUE GOSTOU PELO [NOME] ->')).strip().upper()
            while True:
                if not opcao in vinhos:
                    print('NÃO EXISTE NO NOSSO CATÁLOGO !')
                    opcao = str(input('ESCOLHA O VINHO QUE GOSTOU PELO [NOME] ->')).strip().upper()
                else:
                    break
            quantidade = verificarNumero('DIGITE A QUANTIDADE DE GARRAFAS NECESSÁRIA DE VINHO ->', 'erro!, DIGITE NÚMERO')
            if opcao == 'MERLOT':
                total += quantidade * preco[0]
            elif opcao == 'BRANCO':
                total += quantidade * preco[1]
            else:
                total += quantidade * preco[2]
            continuar_encerrar = ['CONTINUAR','ENCERRAR']
            escolha_continuar_encerrar = str(input('DESEJA CONTINUAR OU ENCERRAR DIGITE UMA DAS OPÇÕES ->')).strip().upper()
            if not escolha_continuar_encerrar in continuar_encerrar:
                print('OPÇÃO INVÁLIDA')
                escolha_continuar_encerrar = str(input('DESEJA CONTINUAR OU ENCERRAR DIGITE UMA DAS OPÇÕES ->')).strip().upper()
            if escolha_continuar_encerrar == continuar_encerrar[1]:
                break



        frete = calcularFrete(total)
        print(f'='*30)
        print(f'<<< RESUMO DO PEDIDO >>>')
        print(f'=' * 30)
        sleep(1)
        print('GERANDO PEDIDO')
        sleep(3)
        mensagemFinal(nome,endereco,total,frete)
    else:
        print('='*30)
        print('MENOR DE IDADE NÃO PODE CONSUMIR BEBIDA COM ÁLCOOL')


realizarCompra()