package Clase5.LeccionClasesObjetos;

public class Persona {
    // Atributos de la clase (Caracteristicas)
    public String nombre;
    public String apellido;
    
    public Persona(String string, String string2) {
    }

    public Persona() {
    }

    //Metodos de la clase (Acciones)
    public void obtenerInformacion(){
        System.out.println("Nombre: "+ nombre);
        System.out.println("Apellido: "+apellido);
    }
}
