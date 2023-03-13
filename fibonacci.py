# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def verifica_fibonacci(num):

    a, b = 0, 1

    while b < num:
        a, b = b, a + b
    return b == num

while True:
    try:
        num = int(input("Insira um número inteiro: "))
        if verifica_fibonacci(num):
            print(num, "Este número faz parte da sequência de Fibonacci.")
            break
        else:
            print(num, "Este número não está na sequência de Fibonacci. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")
