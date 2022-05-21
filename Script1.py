#!/usr/bin/env python

#Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
nombre=input("Dime tu nombre:")
print ("Hola %s" % nombre)


# Calcular el perímetro y área de un rectángulo dada su base y su altura. Calcular también el perímetro y área de un triangulo.
base=float(input("Dime la base:"))
altura=float(input("Dime la altura:"))
perimetro = 2*base + 2*altura
area = base * altura
print ("Resultado: Area=%.2f Perimetro=%.2f" % (area,perimetro))


base=float(input("Dime la base:"))
ladoa=float(input("Dime un lado a:"))
ladob=float(input("Dime el lado b:"))
altura=float(input("Dime la altura:"))
perimetro = base + ladoa + ladob
area = base * altura / 2
print ("Resultado: Area=%.2f Perimetro=%.2f" % (area,perimetro))

#Calcular el perímetro y área de un círculo dado su radio.
import math
radio=float(input("Dime el radio:"))
print ("Resultado: Area=%.2f Perimetro=%.2f" % (math.pi*radio**2,2*math.pi*radio))

#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos
num1=float(input("Numero1:"))
num2=float(input("Numero2:"))
print ("Suma:%d,resta:%d,multiplicacion:%d,division:%.2f"%(num1+num2,num1-num2,num1*num2,num1/num2))

# Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, con espacios intermedios.
palabra=input("Dime una palabra:")
print ((palabra+" ")*1000)

#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
minutos=int(input("Minutos:"))
print ("Horas:%d - Minutos:%d" % (minutos/60,minutos%60))


