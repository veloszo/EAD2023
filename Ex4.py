def primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        limite = int(numero**0.5) + 1
        for i in range(3, limite, 2):
            if numero % i == 0:
                return False
        return True
for num in range(1, 101):
    if primo(num):
        print(f"{num} é primo.")