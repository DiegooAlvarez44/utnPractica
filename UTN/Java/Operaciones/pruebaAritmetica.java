package UTN.Java.Operaciones;

public class pruebaAritmetica {
    public static void main(String[] args) {
        int a = 10; //Variables locales
        int b = 7;  //Memoria stack
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
        
        System.out.println("Aritmetica1 a: " + aritmetica1.a);
        System.out.println("Aritmetica1 b: " + aritmetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(4, 44);
        System.out.println("resultado usando argumentos "+resultado);
        
        System.out.println("Aritmetica1 a: " + aritmetica2.a);
        System.out.println("Aritmetica1 b: " + aritmetica2.b);
        //aritmetica1 = null; // Nunca utilizar esto, no se debe hacer
        //System.gc(); // Metodo para limpiar residuos, es pesado, no utilizar

    }
    public static void miMetodo() {
        // a = 10; una variable que esta limitada
        System.out.println("Aqui ha otro metodo");
    }
}
