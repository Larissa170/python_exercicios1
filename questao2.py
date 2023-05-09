if __name__ == '__main__':
    temperaturas = []
    for i in range(5):
        temperatura = input("Digite uma temperatura:")
        temperaturas.append(temperatura)

    menor_temperatura = 0.00
    soma_temperatura = 0.00
    qtd_negativa= 0
    qtd_positiva = 0
    for i in range(5):

        if i == 0:
            menor_temperatura = float(temperaturas[i])
        elif float(temperaturas[i]) < menor_temperatura:
            menor_temperatura = float(temperaturas[i])

        if float(temperaturas[i]) > 0 and float(temperaturas[i]) < 20:
            soma_temperatura = float(temperaturas[i])

        if float(temperaturas[i]) < 0:
            qtd_negativa = qtd_negativa + 1
        else:
            qtd_positiva = qtd_positiva + 1

    media_temp = soma_temperatura / 5

    print("A menor temperatura é:", menor_temperatura)
    print("A média das temperaturas entre 0 e 20 é: ", media_temp)
    print("São {} temperaturas negatigas e {} temperaturas positivas".format(qtd_negativa,qtd_positiva))