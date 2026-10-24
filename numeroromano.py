
# Converte o número romano para inteiro
def converte(numeroEmRomano):

    # Valores dos números romanos
    tabela = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Começa o total em zero
    acumulador = 0

    # Guarda o valor do símbolo que está à direita
    ultimovizinhodireita = 0

    # Percorre o número romano de trás para frente
    for i in reversed(range(len(numeroEmRomano))):

        # Pega o símbolo atual
        numCorrente = numeroEmRomano[i]

        # Busca o valor do símbolo na tabela
        atual = tabela.get(numCorrente, 0)

        # Por padrão, soma o valor
        multiplicador = 1

        # Se o símbolo atual for menor que o da direita, subtrai
        if atual < ultimovizinhodireita:
            multiplicador = -1

        # Adiciona ou tira o valor do total
        acumulador += atual * multiplicador

        # Guarda o valor atual para comparar com o próximo
        ultimovizinhodireita = atual

    # Retorna o resultado da conversão
    return acumulador
