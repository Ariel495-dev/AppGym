
def simple_for():
    for i in range(66):
        print(i)
def simple_for_with_begin():
    for i in range(51,119):
        print(i)
def simple_for_with_increment():
    for i in range(51,119,3):
        print(i)

def multiplication_table(mult):
    for i in range(1,11):
        print(i * mult)

def multiples():
    for i in range(31,78):
        if(i % 5==0):
            print(i)


def look_for_dino(dino_name):
    """
    Busca un dinosaurio en la lista predefinida.

    Parámetros:
        dino_name (str): Nombre del dinosaurio a buscar.

    Devuelve:
        bool: True si se encuentra, False en caso contrario.
    """
    dinosaurs = ["Triceratops", "Tiranosaurio", "Diplodocus", "Pterodáctilo", "Velocirraptor"]

    for dino in dinosaurs:
        if dino == dino_name:
            return True

    return False

def find_dino2(dinosaur):
    return dinosaur in ["Triceratops", "Diplodocus", "Pterodáctilo"]

def len_example():
    list1 = ["Alice", "Bob"]
    size1 = len(list1)
    print("El tamaño de la primera lista es: " + str(size1))

    list2 = [None, None, None, None]
    size2 = len(list2)
    print("El tamaño de la segunda lista es: " + str(size2))

    list3 = [[1, 2], [3, 4]]
    size3 = len(list3)
    print("El tamaño de la tercera lista es: " + str(size3))

def retrieve_value(index):
    lista = [4, 8, -35, "Pepe Depura", 6]

    if 0 <= index < len(lista):
        return lista[index]
    else:
        return None


if __name__ == '__main__':
 simple_for_with_increment()