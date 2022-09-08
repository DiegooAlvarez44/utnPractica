import java.rmi.server.SocketSecurityException;

import javax.annotation.processing.SupportedOptions;
import javax.print.attribute.SupportedValuesAttribute;

public class holamundo {
    public static void main(String[] args) {
        System.out.println("Hola mundo desde java ");
        // De tipo entero
        int myVariable = 10;
        System.out.println(myVariable);
        myVariable = 5;
        System.out.println(myVariable);
        // De tipo string
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = " Bueno a sido un placer conocerte hasta luego";
        System.out.println(miVariableCadena);

        // var - inferencia de tipos
        var myVariable2 = 44;
        var miVariableCadena2 = "Seguimos estudiando ";
        System.out.println(myVariable2 + " El mejor numero ");
        System.out.println(miVariableCadena2 + "Vamos a seguir mejorando!!");
        // soutv + tab te escribe el codigo

        var nombre = "Diego";
        var titulo = "Estudiante Tecnico en Programacion";
        var union = nombre + " " + titulo;
        System.out.println(union);
        // Para ordenar el codigo es Format

        var a = 8;
        var b = 4;
        System.out.println(a + b);
        // Contexto de cadena primero hay un string entonces va a tomar todo como cadena
        System.out.println(nombre + a + b);
        // Si ponemos la prioridad de parentesis si realiza la suma y despues agrega el string
        System.out.println(nombre + (a + b));
        // Diagonal inversa
        System.out.println("Nueva linea: \n" + nombre);
        //diagonal inversa y letra n
        System.out.println("\n Linea doble N \n" + nombre);
        // Tabulador 
        System.out.println("Tabulador \t" + nombre);
        // Tabulador en el otro lado 
        System.out.println("\t Tabulador" + nombre);
        // Tabulador doble ejemplo menu
        System.out.println("\t\t .:MENU:. ");
        // Borra hacia atras lo que hay en el careacter
        System.out.println("Retroseso: \b\b" + nombre);
        // Comillas simples de esta manera ponemos comillas simples
        System.out.println("Comillas simples:  \'"+nombre+"\'");
        // Comillas dobles
        System.out.println("Comillas dobles \""+nombre+"\"");

    }
}