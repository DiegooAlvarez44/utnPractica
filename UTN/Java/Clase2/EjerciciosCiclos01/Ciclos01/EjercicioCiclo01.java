package Clase2.EjerciciosCiclos01.Ciclos01;
import javax.swing.JOptionPane;

class Ciclos01a {  
    public static void main(String[] args){
        int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero>=0){   // Mientras el numero sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.print("El numero "+numero+" elevado al cuadrado es: " + cuadrado);
            System.out.println("");
            System.out.print(" Digite un numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        System.out.println("El programa a finalizado");
    }
}
