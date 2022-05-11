
nombreLibro = str(input("Escriba el nombre del libro "))
libroId = int(input("Digite el id del libro "))
preciolibro = float(input("Digite el precio del libro "))
enviogratuito = str(input("¿El envio es gratuito? "))


print("")

print("Ingrese los siguientes datos del libro ")
print(nombreLibro)
print(libroId)
if enviogratuito == "si":
     print("Si el envio es gratuito ")
else:
     print("El envio no es gratuito ")


