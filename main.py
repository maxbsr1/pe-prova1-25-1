def q1():
    
    primeira_dose = int(input("Digite o ano da 1 dose: "))
    intervalo = int(input("Digite o período de intervalo em ano(s): "))

    for i in range(1,5):
        proxima_dose = primeira_dose + (i * intervalo)
        print(proxima_dose, end= " ")
def q2():
    
    def eh_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    while True:
        numero = int(input("Digite um valor: "))
        if numero == -1:
            break
        if eh_primo(numero):
            print("Primo")
        else:
            print("Não")

def q3():
    
    total = 0.0
    quantidade = 0

    while True:
        valor = float(input("Digite um valor: "))
        if valor < 0:
            break
        total += valor
        quantidade += 1

    media = total / quantidade if quantidade > 0 else 0.0

    print(f"{total:.2f}")
    print(f"{media:.2f}")

def q4():
    
    dias = int(input("Digite a quantidade de dias: "))
    km = int(input("Digite a km rodada: "))

    if dias <= 0:
        print("Valor inválido")
    else:
        diaria = 90 * dias
        km_limite = 100 * dias
        km_extra = max(0, km - km_limite)
        taxa_extra = km_extra * 12
        total = diaria + taxa_extra
        print(f"{total:.2f}")


def q5():
    
    escala = input("Digite a escala de temperatura (C, F ou K): ").upper()
    valor = float(input("Digite o valor da temperatura: "))

    if escala == "C":
        if valor < -273.15:
            print("Valor de temperatura abaixo do minimo")
        else:
            f = (valor * 9/5) + 32
            k = valor + 273.15
            print(f"{f:.2f} F")
            print(f"{k:.2f} K")

    elif escala == "F":
        if valor < -459.67:
            print("Valor de temperatura abaixo do minimo")
        else:
            c = (valor - 32) * 5/9
            k = (valor + 459.67) * 5/9
            print(f"{c:.2f} C")
            print(f"{k:.2f} K")

    elif escala == "K":
        if valor < 0.0:
            print("Valor de temperatura abaixo do minimo")
        else:
            c = valor - 273.15
            f = (valor * 9/5) - 459.67
            print(f"{c:.2f} C")
            print(f"{f:.2f} F")

    else:
        print("Escala inválida")

if __name__=="__main__":
    q5()  # teste sua questão manualmente aqui
