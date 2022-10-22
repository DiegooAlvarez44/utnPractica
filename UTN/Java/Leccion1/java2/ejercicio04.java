import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            System.out.println("El numero "+numero+" es POSITIVO");
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());

        }
        System.out.println("A inresado "+conteo+" numeros que no son negativo");
    }
}

class ejercicio04a {
    public static void main(String[] args){
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >=0) {
            JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "A ingresado "+conteo+" numeros que no son negativos");
    }
}

