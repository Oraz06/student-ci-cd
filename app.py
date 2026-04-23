import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0-ге бөлуге болмайды")
    return a / b

def power(a, b):
    return a ** b

def max_num(a, b):
    return max(a, b)

def is_even(a):
    return a % 2 == 0

def sqrt_num(a):
    if a < 0:
        raise ValueError("Теріс санның түбірі болмайды")
    return math.sqrt(a)

if __name__ == "__main__":
    print("Қосу:", add(2, 3))
    print("Азайту:", subtract(5, 3))
    print("Көбейту:", multiply(2, 3))
    print("Бөлу:", divide(10, 2))
    print("Дәреже:", power(2, 3))
    print("Максимум:", max_num(5, 3))
    print("Жұп па:", is_even(4))
    print("Түбір:", sqrt_num(16))