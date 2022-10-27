package Clase3.EjerciciosCiclos03.Ciclos3;
import javax.swing.JOptionPane;

class ejercicio3 {
    public static void main(String[] args){
        
        int numero;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero!=0){
            if (numero % 2 == 0){
                System.out.print("El numero ingresado "+numero+" es PAR");
                
            }else{
                System.out.print("El numero ingresado "+numero+" es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero : "));
        }
        System.out.print("El programa finalizo");
    }
}