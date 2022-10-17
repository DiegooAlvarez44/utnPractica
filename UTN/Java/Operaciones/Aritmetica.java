package UTN.Java.Operaciones;

public class Aritmetica {
    //Atributos de la calse
    int a;
    int b;
    
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