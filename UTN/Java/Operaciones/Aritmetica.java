package UTN.Java.Operaciones;

public class Aritmetica {
    //Atributos de la calse
    int a;
    int b;
    
    //El constructor es un metodo especial
    public Aritmetica(){// Constructor 1
        System.out.println("Se esta ejecutando este constructor");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){ //Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el construtor numero 2");
    }

    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("Resultado = "+ resultado);
    }

    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }

    public int sumarConArgumentos(int a, int b){
        this.a = a; //El argumento a se asigna al atributo this.a
        this.b = b;
        //return a + b;
        return this.sumarConRetorno();
    }
}
