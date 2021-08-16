my_set = {}
# La forma correcta de crear un set es parecida a la de los diccionarios, pero sin los dos puntos.
# my_set = { 1 , False, 5.4}
print(type(my_set))
# Primero se habia creado un diccionario, y luego con la funcion set se transforma en un SET
my_set = set()
print(type(my_set))

my_set.add(1)
# La funcion add() agrega elementos al SET, pero solo agrega de a 1 elemento por cada vez q se utiliza
print(my_set)

my_set.update({False, 2, 76, 3, 3, 4, 5, 6, "hello"})
# La forma de agregar varios elementos al set es con el metodo .update()
print(my_set)

my_set.discard(19)
# El metodo .discard() elimina el dato que le pasamos como parametro pero si no esta sigue el proceso, el metodo .remove() elimina el dato que le mandamos como parametro pero si no lo encuentra larga un error.
print(my_set)
# #Aca larga un error, por que dentro del Set no se encuentra el 19.
# my_set.remove(19)
# print(my_set)

my_set.pop()
# El metodo Pop borra un elemento aleatorio dentro del set.
print(my_set)


my_set.clear()
# Borra todos los elementos dentro del set.
print(my_set)
