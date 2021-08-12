# ##asi se importa el modulo Data  
# from datetime import datetime


# ##sirve para saber cuanto tiempo tarda en ejecutar una funcion e imprimir en pantalla.
# def execution_time(func):
#     def wrapper():
#         initial_time =  datetime.now()
#         func()
#         final_time = datetime.now()
#         time_elapsed = final_time - initial_time
#         print(f"Pasaron {time_elapsed.total_seconds()} segundos")
#     return wrapper

# @execution_time
# def random_func():
#     for _ in range(1, 1000000):
#         pass

# random_func()




# ###########################################################3

# def whit_custom_message(message):
#     def with_message(function):
#         print(f"{message}: ")
#         def wrapper(*args, **kwargs):
#             function(*args, **kwargs)
#         return wrapper
#     return with_message

# @whit_custom_message("hello")
# def multiply(a, b):
#     c = a * b
#     print(f"the result of {a} * {b} is {c}")



# def funcion_a(funcion_b):
#     def funcion_c():
#         print('Antes de la ejecución de la función a decorar')
#         funcion_b()
#         print('Después de la ejecución de la función a decorar')

#     return funcion_c

# @funcion_a
# def saluda():
#     print("hola")

# saluda()



def message_decorator(fun):
    def wrapper():
        print("Hello everyone, let's count how many letters has your name.\n")
        nums = fun()
        print(f"\nYour name has {nums} letters")
    return wrapper


# @message_decorator
def greet():
    name = input("Enter your name here: ")
    num = len(name)
    return num
    

greet()