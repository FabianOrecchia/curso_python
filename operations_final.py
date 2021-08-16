def remove_duplicates(some_list):
    whitout_duplicates = []
    for element in some_list:
        if element not in whitout_duplicates:
            whitout_duplicates.append(element)
    return whitout_duplicates

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))
    
    # Aqui vemos como remplazamos la funcion remove_duplicates solo con la funcion set(some_list)
    set_1 = set(random_list)
    print(set_1)


if __name__ == "__main__":
    run()