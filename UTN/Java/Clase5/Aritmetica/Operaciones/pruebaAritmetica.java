
package Clase5.Aritmetica.Operaciones;






public class pruebaAritmetica {
    public static void main(String[] args) {
        //int a = 10; //Variables locales
        //int b = 7;  //Memoria stack
        miMetodo();//Llamamos el metodo nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        //Para almacenar un objeto o los atributos se utiiza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = "+resultado);
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos "+resultado);
        System.out.println("Aritmetica1 : " + aritmetica1.a);
        System.out.println("Aritmetica1 : " + aritmetica1.b);
        Aritmetica aritmetica2 = new Aritmetica(4, 44);
        System.out.println("resultado usando argumentos "+resultado);
        System.out.println("Aritmetica2 : " + aritmetica2.a);
        System.out.println("Aritmetica2 : " + aritmetica2.b);
        //aritmetica1 = null; // Nunca utilizar esto, no se debe hacer
        //System.gc(); // Metodo para limpiar residuos, es pesado, no utilizar
        Persona persona = new Persona("Diego", "Alvarez");
        System.out.println("Persona = "+ persona);
        System.out.println("Persona nombre = "+persona.nombre);
        System.out.println("Prsona Apellido = "+persona.apellido);
    }
    public static void miMetodo() {
        // a = 10; una variable que esta limitada
        System.out.println("Aqui ha otro metodo");
    }
}

//Creamos una nueva clase 
class Persona{
    String nombre;
    String apellido;

    Persona(String nombre, String apellido) {
        //Imprimir imprimir = new Imprimir();
        //super();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}

class Imprimir{
    public Imprimir(){
        super(); //El constructor de la clase padre, para reservar memoria
    }

    public void imprimir(Persona persona) {
        System.out.println("Persona desde la clase imprimir "+persona);
        System.out.println("Imprecion del objeto actual con (this) " + this);
        
    }
}