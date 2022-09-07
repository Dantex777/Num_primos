def run():
    number = int(input('Escribe un numero: '))
    print('Es primo'if (isPrime(number)) else'No es primo')

def isPrime(num):
    return ((factorial(num - 1) + 1) % num) == 0 if num > 1 else False

def factorial(num):
    return 1 if num <= 1 else (num * factorial(num - 1))

if __name__ == '__main__':
    run()