def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
            return divisors

def run():
    
    num = int(input("Ingresa un numero: "))
    print(divisors(num))
    print("termino mi programa")

if __name__ == '__main__':
    run()