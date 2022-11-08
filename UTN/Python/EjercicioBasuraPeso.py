carga = 0
peso = [1.01, 1.99, 2.5, 1.5, 1.01]
cargaTotal = 0
vuelta = 0
vaciar = 0
a = False
cargaMaxima = 3
#def sumaCargaTotal(self, cargaTotal):
#   for n in peso:
#       cargaTotal =  0 + n
#       print(cargaTotal)

cubo = 0
for n in peso:
    cuboDeBasura = n
    if cubo < 3:
        print(f"Llenando cubo de basura {cubo}")
        cubo = cuboDeBasura + cubo
        vuelta = 0 + 1
        if cubo >= 3:
            print(f"Cubo de basuro Lleno.{cubo} Vaciando")
            cubo = cubo - cubo
            vuelta = 0 + 1 
    elif cubo >= 3:
        print(f"Cubo de basura Lleno. {cubo} Vaciando")
        cubo = cubo - cubo
        print(cubo)
        vuelta = 0 + 1
print(f"Vuelta {vuelta}")

    
    


                
            

            


