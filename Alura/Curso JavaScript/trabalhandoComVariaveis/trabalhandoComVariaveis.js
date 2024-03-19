//JS é casesensitive
console.log("'console' tem que ser minusculo")

const idade = 28;
const nome = "Matheus";

//Operações Aritméticas

console.log(10 + 8 * 2);
console.log((10 + 8) * 2);

console.log("ano " + 2023);
console.log("2" + "2");

//Conversão de tipo

console.log("ano " + 2023);
console.log("2" + "2");
console.log(parseInt("2") + parseInt("2"));

//Atribuição de variáveis
console.log(`Meu nome é ${nome}`)

//Array
const listaDeDestinos = new Array(
    `Salvador`, 
    `São Paulo`, 
    `Rio de Janeiro`,
    `Curitiba`
);

// Adicionando um item na lista
listaDeDestinos.push(`Campina Grande`)

// Tirar um item da lista
listaDeDestinos.splice(1, 1);

console.log(listaDeDestinos);
console.log(listaDeDestinos[1]);

// Operadores Lógicos


