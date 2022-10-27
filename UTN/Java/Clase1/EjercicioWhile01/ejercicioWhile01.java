
package Clase1.EjercicioWhile01;

public class ejercicioWhile01 {
    public static void main(String[] args){
        var conteo = 0; // Inferencia de tipos
        while(conteo < 7){
            System.out.println("conteo con ciclo while = "+ conteo);
            conteo++;//Vamos aumentando en uno la variable
        }

        var contador = 0;
        do{
            System.out.println("contador con do = " + contador);
            contador++;
        }while(contador < 7); //PERO si la condicion es falsa sale de ciclo y no lo vuelve a ejecutar

        for(var contador1 = 1; contador1 < 7; contador1++){
            if(contador1 % 2 ==0){ // Si encuentra un numero que dividido de 0 
            System.out.println("contador1 con for + break = " + contador1);
            break; // Aqui rompe! sale del ciclo
            }
        // Otra forma que lo llegar a podemos encontrar
        //for(int i = 0; ; ){
        //}

        for(var contador2 = 0; contador2 < 7; contador2++){
            if(contador2 % 2 !=0){ //  
                continue;
            }
            System.out.println("contador2 con for + continue = " + contador2);
        }
        
        // Etiquetas Lebels
        inicio:
        for(var contador4 = 1; contador4 < 7; contador4++){
            if(contador4 % 2 == 0){ // Si encuentra un numero que dividido de 0 
            System.out.println("contador4 con for + break + lebels= " + contador4);
            break inicio; // Aqui rompe! sale del ciclo
        }

    }
}
}
}

