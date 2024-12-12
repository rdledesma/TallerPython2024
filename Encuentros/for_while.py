import random
r1 = random.randint(-10, 10)
print("Random number between -10 and 10 is % s" % (r1))



def indicaEsPar(n):
    for i in range(0, n, 1):
        if i%2 == 0:
            print(f"el numero {i} es par")


def sumaNPares(n):
    acum = 0
    i = 0
    while i < n: 
        if i % 2 == 0:
            acum = acum + i
        i = i+1
    
    



l = [1,2,3,4,5,6,7]

l.append(73)

print(l[0])

print(l[1:5])


l2 = [x for x in range(0,100)]

lImpar = [x for x in range(0,100) if x%2 == 1]




#Ejercicio 1

#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
# y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

#Ejercicio 2
#Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los 
#elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

#Ejercicio 3
#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas 
# por un alumno (comprendidas entre 0 y 10).
# A continuación debe mostrar todas las notas, la nota media,
# la nota más alta que ha sacado y la menor.