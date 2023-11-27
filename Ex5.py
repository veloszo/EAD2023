def inverterLetras(frase):
    letrasInvertidas = [letra[::-1] for letra in frase.split()]
    novaFrase = ' '.join(letrasInvertidas)
    return novaFrase


fraseUsuario = input("Digite a frase que deseja inverter: ")
fraseInvertida = inverterLetras(fraseUsuario)
print(f"Frase Original: {fraseUsuario}")
print(f"Frase Invertida: {fraseInvertida}")