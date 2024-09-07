#Sintaxis --> def NombreDeFuncion(Parámetros):

nombre  = "Ivon"
numero1 = 2
numero2 = 3

def Saludo ():
    print("Hola. Mucho Gusto " + nombre)

def Sumar():
    num1 = 10
    num2 = 20
    #print(num1 + num2)
    suma = num1 + num2
    return suma

#Sumar()

def Resta(numero1,numero2):
    
    resta = numero1 - numero2
    return resta


#print(Sumar()+10)

print(Resta(numero1,numero2)+10)


#Saludo()