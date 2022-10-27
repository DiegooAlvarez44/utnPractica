// Tipos de datos en JavaScript
/*
L sintaxis es lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identica
*/
var nombre = 'Diego'; //Tipo Str
console.log(nombre)
nombre = 44;
console.log(nombre)
nombre = 44.4;
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

//Tipo de datos underfined
var x;
console.log(x);
 x = undefined;
 console.log( typeof x)

// null: significa ausencia de valor
var y = null;// null no es un tipo de dato, pero su origen es object
console.log(y); 
 
//Tipo de dato array y  E mpty String
var autos = ['Citroen', 'Audi', 'BMW', 'Ford'];
console.log(autos);
console.log(typeof autos); //Preguntamos que tipo de dato es

var z = '';
console.log(z); // Esto se refiere a que es una cadena vacia:
console.log(typeof z);

//Clase 7 JavaScript

let a , b; // Se pueden crear varias variables dentro de una misma linea
a = 15, b = 19; //Se puede hacer asignacion de varias variables dentro de una misma linea
let c = a + b; // Se le asigna el valor de la operacion
console.log(z)

let _1num = 31;// No utilizar numeros para iniciar el nombre de una variable
//let break = "Rompe";  No se utiliza las palabras reservadas para asignar variables
let rompiendo = "Rompe"
console.log(_1num)
console.log(rompiendo)

