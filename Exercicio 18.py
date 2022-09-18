#18) Faça um programa que leia a nota de um aluno. Garanta que a nota seja um valor inteiro entre zero e 100. Se o valor não estiver neste intervalo, informe que a nota é inválida. Se a nota for maior que 60, informa que o aluno foi aprovado; caso contrário, informa que ele foi reprovado.

Nota=int(input('Nota: '))


if(Nota)>=60 and (Nota)<100:print('Aprovado')
if(Nota)<60 and (Nota)>0:print('Reprovado')
if(Nota)>100:print('Nota inválida')
if(Nota)<0:print('Nota inválida')

