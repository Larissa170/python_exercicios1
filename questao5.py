if __name__ == '__main__':
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    if int(idade) > 18:
        print("{} é maior de 18 e tem {} anos.".format(nome,idade))
    else:
        print("{} não é maior de 18 e tem {} anos.".format(nome, idade))
