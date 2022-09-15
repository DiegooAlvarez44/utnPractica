
import javax.swing.JOptionPane;

import java.nio.file.WatchEvent;
import java.util.Scanner;

class Ejercicio02 {
    public static void main (String[] args){
    
    int numero;
    numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
    while(numero!=0){
        if(numero<0){
                System.out.print("El"+numero+" es negativo");
                numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        } else if(numero>0){
                    System.out.print("El"+numero+" es positivo");
                    numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }else {
            System.out.print("Finalizo el programa");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
    } 
    }
 }

 class Ejercicio02a {
    public static void main (String[] args){
        Scanner entrada = new Scanner(System.in);
    
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero!=0){
            if(numero<0){
                    System.out.println("El"+numero+" es negativo");
                    
            } else{
                    System.out.println("El"+numero+" es positivo");
                        
            }
            System.out.println("Finalizo el programa");
            numero = Integer.parseInt(entrada.nextLine());
            
        }
        System.out.println("El numero "+numero+" finaliza el programa ");
        } 
    }
    