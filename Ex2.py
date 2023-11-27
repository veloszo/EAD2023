import math

def calcular_area_triangulo(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    area = calcular_area_triangulo(a, b, c)
    print(f"Os valores formam um triângulo e a área é: {area}")
else:
    print("Os valores informados não formam um triângulo. Valores informados: a =", a, ", b =", b, ", c =", c)