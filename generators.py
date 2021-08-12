# def my_gen():
#     print("hello world")
#     n = 0 
#     yield n

#     print("hello heaven")
#     n = 1 
#     yield n 

#     print("bye people")
#     n = 2 
#     yield 2

# a = my_gen()

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

import time

def fibo_gen(max=None):
    n1 = 0 
    n2 = 1 
    counter = 0 
        
    while counter < max:
        if counter == 0:
            counter+=1
            yield n1
        elif counter == 1:
            counter+=1
            yield n2
        else:
            aux = n1+n2
            n1,n2 = n2, aux
            counter+=1
            yield aux

if __name__ == "__main__":
    max = int(input("Ingresa un numero: "))
    fibonacci = fibo_gen(max)
    for element in fibonacci:
        print(element)
        time.sleep(1)
        
