def calcIdade(dias):
    anos = dias // 365
    meses = (dias % 365) // 30
    diasR = (dias % 365) % 30
    return anos, meses, diasR


idadeDias = int(input("Digite a idade em dias: "))

anos, meses, dias = calcIdade(idadeDias)

print(f"A idade é {anos} anos, {meses} meses e {dias} dias.")