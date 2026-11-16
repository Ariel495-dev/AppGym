def make_question():
    question = """
¿Cuál es la universidad más antigua de Europa, fundada en 1088, que sigue en funcionamiento actualmente?

a) Universidad de París
b) Universidad de Bolonia
c) Universidad de Oxford    
"""
    print(question)

    choice = input("Escoge tu respuesta (a, b ó c): ")
    while choice != 'a' and choice != 'b' and choice != 'c':
        choice = input("Por favor, escoge una respuesta válida (a, b ó c): ")


    if choice == 'b':
        print("¡ENHORABUENA! ¡HAS ACERTADO! Ganaste 149 puntos")
    else:
        print("¡Fallaste! Pero no pasa nada, ¡sigue intentándolo!")

def make_question2():
    question2 = """
¿Cuál es el resultado de SUMAR estos números?
463
661
"""
    print(question2)
    answer = None
    while answer is None:  # Se prefiere 'is' a '==' para comparar con None
        try:
            answer = int(input("Dime tu respuesta: "))
        except ValueError:
            print("¡No has introducido un número válido!")

    if answer == 463+661:
        print("Respuesta correcta")
    else:
        print("Lo sentimos, respuesta incorrecta")
if __name__ == '__main__':
    make_question()
    make_question2()




