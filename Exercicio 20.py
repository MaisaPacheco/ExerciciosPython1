#20) Crie um programa para calcular o valor a ser pago para um determinado produto para a empresa NaoQueroMuitoSeuDinheiro. O pessoal desta empresa pediu o seguinte: ● Vamos coletar três valores: ○ O valor inicial da parcela. ○ O valor percentual de cada parcela. ○ A quantidade de parcelas. ● Para cada parcela a ser paga, o cálculo é o seguinte: valor_parcela = valor_anterior + (valor_anterior * percentual) ● No caso da primeira parcela, o valor anterior é o valor inicial. Crie um programa que irá mostrar cada parcela e o seu valor. Por exemplo: se o valor inicial for $100,00, o valor do percentual for 0,10, e a quantidade de parcelas for 2; logo nosso programa irá mostrar: Parcela 1: $ 110.0 Parcela 2: $ 121.0

str_valor_inicialparcela = input ('Qual valor da parcela?')
str_valor_percentualparcela = input ('Qual valor percentual de cada parcela?')
str_quantidade_parcelas = input ('Qual a quantidade de parcelas?')

valor_inicialparcela = float (str_valor_inicialparcela)
valor_percentualparcela = float (str_valor_percentualparcela)
quantidade_parcelas = int (str_quantidade_parcelas)

parcela_atual = 1

while parcela_atual <= quantidade_parcelas :
    if parcela_atual == 1:
        valor_parcela = valor_inicialparcela + (valor_inicialparcela * valor_percentualparcela)
    else:
        valor_parcela = valor_parcela + (valor_parcela * valor_percentualparcela)
    print ("Parcela " + str (parcela_atual) + ": $ "+ str (valor_parcela))
    parcela_atual +=1