package UTN.Java.Leccion1.pasoporreferencia;

import java.lang.Thread.State;

import UTN.Java.Clase4.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        final Persona persona1 = new Persona();
        persona1.nombre = "Ester";
        System.out.println("persona1 = "+ persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es : "+persona1);
        persona1 =  cambiarElValor(persona1);
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        System.out.println("El nuevo valor del objeto es: "+persona2.nombre);

    }

    public static void cambiarValor(Persona persona) { //Párametro por referencia
        persona.nombre = "Maria";
        return;
    }
    public static Persona cambiarElValor(Persona persona){
        if(persona  == null){
            System.out.println("Valor de persona es invalido : Null " );
            return null;
        }
        else{
            persona.nombre = "Monica";
            return persona;
        }
        
    }
}
