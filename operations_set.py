# Creamos dos sets:
set = {1, 2, 3, 4}
set_1 = {4, 5, 6, 7}

# Esta seria la union entre los sets, el numero 4 se repite en ambos set, pero la operacion solo deja uno dentro de un nuevo set ejemplo set_2 , se hace con el operador PIP
set_2 = set | set_1
print(f"Esta es la union entre sets: \n {set_2}")
# El metodo para realizar una union entre dos sets es set.union(set2)
print(set.union(set_1))

# Ahora vamos a realizar una interseccion, en este caso solo nos quedamos con la parte que tienen en comun. En este caso seria el numero "4". La operacion se realiza mediante el operador "&"
set_3 = set & set_1
print(f"Esta  es la interseccion entre sets: \n {set_3}")
# El metodo para realizar la interseccion es "set.interseccion(set2)"
print(set.intersection(set_1))


# Aca vamos a hacer una resta o diferencia, la cual consiste en tomar dos sets y de uno quitar todos los elementos que tiene el otro.
set_4 = set - set_1
print(
    f"Esta es el resultado de aplicar la diferencia (set - set_1): \n {set_4}")
set_4a = set_1 - set
print(
    f"Esta es el resultado de aplicar la diferencia (set_1 - set): \n {set_4a}")
# El metodo para realizar la diferencia entre dos sets es "set.difference(set2)"
print(set.difference(set_1))
print(set_1.difference(set))

# Y por ultimo vamos a ver la diferencia simetrica, es el resultado de quedarme con los elementos de ammbos sets pero sin los que se comparten. lo contrario de la interseccion. y se realiza con el operador " ^ ". En este caso sacaria del conjunto el numero 4 que es el unico que tienen en commun.
set_5 = set ^ set_1
print(f"Esta es el resultado de aplicar la diferencia simetrica: \n {set_5 }")
# El metodo para la diferencia asimetrica se llama "set.symmetric_difference(set2)""
print(set.symmetric_difference(set_1))

# Vamos a probar ahora con metodos para realizar las mismas operaciones de arriba.
