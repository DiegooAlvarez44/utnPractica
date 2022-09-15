

class EjercicioWhile01 {
    public static void main(String[] args){
        var conteo = 0; // Inferencia de tipos
        while(conteo < 7){
            System.out.print("conteo = "+ conteo);
            conteo++;//Vamos aumentando en uno la variable
        }
        
        var contador = 0;
        do{
            System.out.print("contador = " + contador);
            contador++;
        }while(contador < 7);

        // Uso de las palabras BREAK y CONTINUE junto a las etiquetas (labels)
        
        for(var contando = 0 ; contando < 7 ; contando++ ){
            if(contando % 2 == 0){
                System.out.print("contando = " + contando);
                break;
            }
        }
        inicio:
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 !=0){
                continue inicio; //Vamos a las siguiente iteracion
            }
            System.out.print("contando = " + contando);
        }
    }
}