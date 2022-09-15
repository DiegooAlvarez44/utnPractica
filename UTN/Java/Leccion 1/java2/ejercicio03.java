import java.util.Scanner;

import javax.sound.sampled.SourceDataLine;
import javax.swing.JOptionPane;

public class ejercicio03 {
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
    }
}

class ejercicio3 {
    public static void main(String[] args){
        
        int numero;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero!=0){
            if (numero % 2 == 0){
                System.out.print("El numero ingresado "+numero+" es PAR");
                numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero : "));
            }else{
                System.out.print("El numero ingresado "+numero+" es IMPAR");
                numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero : "));
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero : "));
        }
        System.out.print("El programa finalizo");
    }
}