package Clase3.EjerciciosCiclos03.Ciclos3;

import java.util.Scanner;

public class Ciclos03 {

        public static void main(String[] args){
            Scanner entrada = new Scanner(System.in);
            int numero;
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            while(numero!=0){
                if (numero % 2 == 0){
                    System.out.print("El numero ingresado "+numero+" es PAR");
                }else{
                    System.out.print("El numero ingresado "+numero+" es IMPAR");
                }
                System.out.println("Digite otro numero: ");
                numero = Integer.parseInt(entrada.nextLine());
            }
            entrada.close();
        }
    }
    

