# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le devolvera la misma
# frase pero sin espacios en blanco, y
# ademas un contador de cuentos caracteres tiene la frase
# (sin contar los espacios en blanco)
# Ejemplo:      frase = vivir por siempre en paz
#               frase final = vivirporsiempreenpaz
#               N° de caracteres = 20

frase = str(input("Escriba una oracion: "))
frase2 = ""
contador = 0
for i in frase:
    if i != " ":
        frase2 += i
for i in frase2:
    contador = contador + 1

print(frase2)
print(contador)