// Tipos de datos en JavaScript
/*
L sintaxis es lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identica
*/
var nombre = 'Diego'; //Tipo Str
console.log(nombre)

var numero = 3000; //Tipo numerico
console.log(numero)

var objeto = {
    nombre : "Diego",
    apellido : "Alvarez",
    telefono : "123456"

}

console.log(objeto);

// Tipo de dato boolean
var bandera = true;
console.log(bandera)

// Tipo de dato funcion
function mifuncion(){}
console.log(mifuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo)

//Tipo de dato clase
class Persona{
    constructor(nombre, apellido){
    this.nombre = nombre;
    this.apellido = apellido;
    }
}
console.log(Persona)