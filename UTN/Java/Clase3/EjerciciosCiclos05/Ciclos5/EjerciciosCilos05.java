package Clase3.EjerciciosCiclos05.Ciclos5;

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

class EjerciciosCilos05 {
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
