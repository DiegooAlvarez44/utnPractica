package Clase2.EjerciciosCiclos02.Ciclos2;

import javax.swing.JOptionPane;


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

 
    