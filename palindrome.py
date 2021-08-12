# def is_palindrome(string: str) -> bool:
#     string = string.replace(" ", "").lower()
#     return string == string[::-1]

def is_prim(num: int) -> bool:
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count <= 2:
        print("Es primo")
    else:
        print("No es primo")


def run():
    num_1 = input("Ingresa el numero a verificar: ")
    return is_prim(int(num_1))


if __name__ == '__main__':
    run()