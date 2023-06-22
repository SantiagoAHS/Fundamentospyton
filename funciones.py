#funciones en pyton
#def name_funcion(params):
#codigo 
#return

#Funcion sin parametros y sin retornos
def saludo():
    print("Hola a Todos!")

saludo()

#Funcion con 1 parametro
def get_age_in_future(age):
    print(f"en 3 años tendras {age+3} años")

get_age_in_future(19)

#funcion con 2 parametros sin retorno
def suma(num1,num2):
    print(f"{num1} + {num2} = {num1 + num2}")

suma(12, 35)

#Funciones con parametros opcionales
def get_heroes(h1="Ironman", h2="Spiderman"):
    print([h1, h2])

get_heroes()
get_heroes("Batman")
get_heroes("Batman", "Superman")
get_heroes(h2="Batman", h1="Superman")

#Funciones con retorno
def title(texto):
    return texto.title()

text_change=title("hOlA a ToDoS")
print(text_change)