#21. O pessoal da empresa Caça-Clientes trabalha com ligações para números aleatórios. Eles recebem uma lista com vários intervalos de números para eles ligarem. Na lista recebida, você tem o prefixo do telefone, o primeiro sufixo e o último sufixo. Crie um script que liste todos os números dos telefones, ao serem informados, o prefixo e os sufixos. Porexemplo, suponha que o prefixo seja “3232” e que o primeiro prefixo seja “0001” e o último sufixo seja “0005”; logo o programa irá imprimir:

def gerador_telefones(lista):
    prefixo = lista[0]
    sufixo_inicial = int(lista[1])
    sufixo_final = int(lista[2])
    lista_sufixos = []
    lista_telefones = []

    for i in range(int(sufixo_inicial), int(sufixo_final+1)):
        num = i
        str_num = str(num)
        while len(str_num) < 4:
            str_num = "0"+str_num
        lista_sufixos.append(str_num)
    print(lista_sufixos)

    for i in range(len(lista_sufixos)):
        lista_telefones.append(f"{prefixo}-{lista_sufixos[i]}")

    print(lista_telefones)


gerador_telefones(['3232', '0001', '0005'])
gerador_telefones(['3232', '0012', '0032'])
gerador_telefones(['3232', '0120', '0129'])
gerador_telefones(['3232', '1100', '1115'])