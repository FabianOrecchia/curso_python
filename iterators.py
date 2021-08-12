# def fibonacci_recursivo(n):
#     if n == 0 or n == 1:
#         return 1

#     return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# n = int(input("ingrese la cantidad de terminos: "))

# for i in range(1 , n+1):
#     print(f" fibonacci {i} es {fibonacci_recursivo(i)}")

import time


class fiboIter():

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):

        if self.max == self.counter:
            raise StopIteration

        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            # la linea de codigo de abajo es igual que la de arriba
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux


if __name__ == '__main__':
    max = int(input("Ingresa numero: "))
    fibonacci = fiboIter(max)
    for element in fibonacci:
        print(element)
        time.sleep(1)
