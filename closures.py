# hola 3 -> holaholahola

# def make_repetear_of(n):
#     def repetear(string):
#         assert type(string) == str, "Solo puedes utilizar cadenas"
#         return string * n
#     return repetear

# def run():
#     repeat_5 = make_repetear_of(5)
#     print(repeat_5("Hola"))

def make_division_by(n):
    def make_divisor(x):
        return x / n
    return make_divisor

def run():
    #PRIMERO = se ejecuta primero la funcion make_division_by(n), con el numero 3 como valor de "n", 
    #SEGUNDO = Se va hasta la funcion make_division_by(3), y se ejecuta ahora una funcion dentro de la misma la cual se llama make_divisor(x), y contiene un numero "x" tambien, el cual se va a dividir por "n". y esto lo retorna como resultado.
    # es decir va a dividir x/n,  y al final retorna la funcion, osea que division_by_3 va a contener la funcion make_divisor() para luego crear un print y ejecutar division_by_3(18)

    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))



if __name__ == "__main__":
    run()