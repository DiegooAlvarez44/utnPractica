package Clase5.EjerciciosCiclos09;

import java.util.Scanner;



public class Ciclos09 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int dia = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el mes: ");
        int mes = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el año: ");
        int año = Integer.parseInt(entrada.nextLine());
        if((dia != 0 )&&(dia <= 30)){
            if((mes != 0) &&(mes <=12)){
                if((año != 0)&&(año <= 2022)){
                    System.out.println("La fecha ingresada es "+dia+"/"+mes+"/"+año);
                }
                else{
                    System.out.println("Fecha incorrecta, año incorrecto");
                }

            }
            else{
                System.out.println("Fecha incorrecta, dia incorrecto");
            }
        }
        entrada.close();
    }
}
