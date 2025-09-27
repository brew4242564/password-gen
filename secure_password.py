import re
import random
import word_list
import sys
words = word_list.make_list() # variable global que nos arma la lista de palabras que utilizaremos

def validate_password(password):
    """
    Valida si la contraseña cumple con los siguientes criterios:
    - Al menos una letra minúscula
    - Al menos una letra mayúscula
    - Al menos un dígito
    - Al menos un carácter especial
    - Longitud entre 8 y 32 caracteres
    """
    patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[^\s]{8,32}$"
    return bool(re.match(patron, password))



def case(word):
    """
    Aleatorizamos el uso de mayusculas y minusculas
    """
    my_list = list(word)
    for i, letter in enumerate(my_list):
        if random.randint(0,1) == 1:    
            my_list[i] = letter.lower()
        else:
            my_list[i] = letter.upper()
    return "".join(my_list)

def make_password(my_list):
    for i in range(len(my_list)):
        my_list[i] = case(my_list[i])
    simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    return f"{random.choice(simbolos)}{random.randint(0,9)}".join(my_list)

def custom_password(word1, word2, word3):
    """
    tomando 3 palabras elegidas por el usuario, generamos una contraseña segura si se cumplen las condiciones.
    """
    if (len(word1) + len(word2) + len(word3)) <= 28 and (len(word1) + len(word2) + len(word3)) >= 8:
        my_list = [word1, word2, word3]
        return make_password(my_list)
    else:
        print(f"Longitud total invalida (Minimo 8 caracteres, maximo 28 caracteres)\n longitud:{len(word1) + len(word2) + len(word3)}")


def pausa():
    """
    muy necesario para poder leer las entradas.
    """
    input("\nPresiona ENTER para regresar al menú...")

def menu():
    print("===========================================")
    print("+             Password-Gen                +")
    print("===========================================")
    print("1. Crear lista de contraseñas seguras")
    print("2. Crear contraseña segura personalizada")
    print("3. Validar contraseña")
    print("4. Salir")

def select():
    """
    Aqui se ejecutan todas las operaciones del programa.
    """    
    opc = "aux"
    while opc != 0:
        menu()
        opc = input("\n Ingresa una opcion: ")
        match opc:
            case "1":
                pass_list = []
                i = 0
                cant = int(input("Ingresa la cantidad de contraseñas a generar: "))
                while i < cant:
                    i += 1
                    pass_list.append(f"{i}. {make_password(my_list = random.choices(words, k=3))}")
                print("Contraseñas generadas: ")
                print("\n".join(pass_list))
                pausa()
            
            case "2":
                print(custom_password(input("Ingresa la primer palabra: "), input("Ingresa la segunda palabra: "),input("Ingresa la tercer palabra: ")))
                pausa()

            case "3":
                mi_pass = input("Ingrese la contraseña: ")
                if validate_password(mi_pass):
                    print("\nTu contraseña es valida.")
                else:
                    print("\nTu contraseña es insegura.")
                pausa()

            case _: # cualquier opcion diferente de 1,2,3 hara que el programa termine, pero decidi poner 4 en el menu para hacerlo mas facil al usuario.
                sys.exit()

if __name__ == "__main__":
    select()

