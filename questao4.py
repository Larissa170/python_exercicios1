if __name__ == '__main__':
    meses = input("Digite o número de meses do controle alimentar: ")
    quilos = input("Digite quantos quilos deseja perder: ")

    divisao = int(quilos) / int(meses)

    for i in range(int(meses)):
        print("Mês {} você irá perder {} Kg".format(1+i,divisao))

