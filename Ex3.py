def findNumber(a, b, c):
    return min(a, b, c)

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

menor = findNumber(numero1, numero2, numero3)

print(f"O menor número é :{menor}")