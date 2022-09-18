#23)  Neste script você irá ler o nome de 4 alunos e suas notas e determinar qual aluno possui a maior not

alunos_notas = {"Larissa": 10, "Daniel": 9, "Izabela": 5, "Giovana": 0}
maior_nota_aluno = max(alunos_notas, key=alunos_notas.get)
print (maior_nota_aluno)

#

alunos = []
aluno = {}


def maior_nota(lista_alunos):
    maior_nota = 0
    for aluno in lista_alunos:
        for nome, nota in aluno.items():
            if nota > maior_nota:
                maior_nota = nota
                melhor_aluno = nome

    return (melhor_aluno)


def programa():
    for i in range(4):
        nome = input(f"Qual o nome do aluno {i+1}?")
        nota = float(input(f"Qual a nota do aluno {i+1}?"))
        aluno[nome] = nota
        alunos.append(aluno)

    melhor_aluno = maior_nota(alunos)
    print(f"O aluno com maior nota é: {melhor_aluno}")


programa()