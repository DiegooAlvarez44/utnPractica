package Clase2.EjerciciosCiclos01.Ciclos01;


import java.util.Scanner;



class Ciclos01 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int numero, cuadrado;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero>=0){ //Mientras el numero sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.print("El numero "+numero+" elevado al cuadrado es: " + cuadrado);
            
            System.out.print(" Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado");
        entrada.close();
}
}

