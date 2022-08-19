def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
            return divisors

def run():
    num = int(input("Ingresa un numero: "))
    print(divisors(numm))
    print("termino mi programa")


if _name_ == '_main_':
    run()