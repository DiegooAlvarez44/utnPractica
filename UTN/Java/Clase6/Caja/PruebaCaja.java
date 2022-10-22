package UTN.Java.Clase6.Caja;

public class PruebaCaja {
    public static void main(String args[]) {
        //Variables locales
        int medidaAncho = 3; //Valores ingresados
        int medidaAlto = 2;
        int medidaProf = 6;

        Caja caja1 = new Caja(); //Instaciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho; // Le pasamos los valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen();
        //Primer resultado
        System.out.println("resultado volumen de caja 1: "+ resultado);

        Caja caja2 = new Caja(2, 4, 6); // Llamamos al constructor 2 con nuevos argumentos
        //Llamamos con el nuevo objeto al metodo para un nuevo calculo
        System.out.println("Resultado volumen de caja 2: "+ caja2.calcularVolumen());
    }
}
