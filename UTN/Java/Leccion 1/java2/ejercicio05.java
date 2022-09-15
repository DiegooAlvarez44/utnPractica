import java.util.Scanner;
import javax.swing.JOptionPane;
/*
 Ejercicio 5: Realizar un juego para adivinar un numero,
 para ello generar un numero aleatorio entre
 0-100, y luego ir pidiendo numeros indiciando 
 "es mayor" o  "es menor" Segun sea mayor o menor
 a N
 El proceso termina cuando el usuario acierta 
 y mostramos el numero de intentos hechos.
 */
public class ejercicio05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int) (Math.random() *100); //Esto genera un numero aleatorio
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio) {
                System.out.println("Digite un numero mayor ");
            }
            else if(numero > aleatorio) {
                System.out.println("Digite un numero menor ");
            }
            else{
                System.out.println("FELICIDADES HAS ADIVINADO EL NUMERO");
            }
            conteo++;
        }while(numero != aleatorio);
        System.out.println("Adivinaste el numero en: "+conteo+" intentos");
    }
}

class ejercicio05a {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int) (Math.random()*100); //Esto genera un numero aleatoreo
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero mayor");
            }
            else  if(numero > aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un numero menor");
            }
            else{
                JOptionPane.showMessageDialog(null, "Felicidades Has adivinado el numero ");
            }
            conteo++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el numero en: "+conteo+" intentos");
    }
}
