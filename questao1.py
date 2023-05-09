if __name__ == '__main__':

    for i in range(1, 12):
        print(i)

    numero = input("Digite um Mês de 1 à 12: ")
    num = int(numero)
    print("Mês atual", numero)
    soma = 0

    for i in range(1,num):
        soma = soma + num

    print("A soma dos valores menores que o mes atual é:  ", soma)

    if num > 0 and num < 12:
        print("Próximo mês é ", num+1)
    elif num == 12:
        print("Próximo mês é 1")

    if num % 2 == 0:
        print("Mês atual é par")
    else:
        print("Mês atual é ímpar")
