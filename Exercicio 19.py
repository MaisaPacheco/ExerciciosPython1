#19). Um vendedor ganha uma comissão de uma venda da seguinte forma: Se a venda for … ● menor que R$1000,00, o vendedor não ganha nenhuma comissão; ● entre R$1.000,00 e R$5.000,00, o vendedor ganha uma comissão de 10% da venda; ● entre R$5.000,00 e R$10.000,00, a comissão será de 20% da venda; ● entre R$10.000,00 e R$50.000,00 a comissão será de 25% da venda; ● acima de R$50.000,00 a comissão será de 30% da venda. Faça um programa que informe o valor da comissão do vendedor para uma venda.

Venda=float(input('Venda: '))

if(Venda)<1000: print((Venda)*0)
if(Venda)>=1000 and (Venda)<=5000: print((Venda)*1.1)
if(Venda)>5000 and (Venda)<=10000: print((Venda)*1.2)
if(Venda)>10000 and (Venda)<=50000: print((Venda)*1.25)
if(Venda)>50000: print((Venda)*1.30)

