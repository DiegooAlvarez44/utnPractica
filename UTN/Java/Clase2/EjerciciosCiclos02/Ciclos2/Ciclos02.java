package Clase2.EjerciciosCiclos02.Ciclos2;
import java.util.Scanner;

class Ciclos02 {
    public static void main (String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero!=0){
            if(numero<0){
                    System.out.println("El "+ numero +" es negativo");
                    
            } else{
                    System.out.println("El "+ numero +" es positivo");
                        
            }
            
            numero = Integer.parseInt(entrada.nextLine());
            
        }
        System.out.println("El numero "+numero+" finaliza el programa ");
        entrada.close();
    } 
}
