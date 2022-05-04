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

    }
}