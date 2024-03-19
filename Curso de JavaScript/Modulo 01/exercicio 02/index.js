let umaString = "Um \"texto\"";
console.log(umaString);

//                    01234567890
let stringQualquer = "Hello World";

// retorna o texto da posição
console.log(stringQualquer.charAt(4));

// concatena o texto
console.log(stringQualquer.concat(' ', 'Brasil'));

// retorna onde começa o string
console.log(stringQualquer.indexOf("World"));

// retorna a posição da string só que começa de trás para a frente
console.log(stringQualquer.lastIndexOf("W", 4));

// Substitui o texto para outro
console.log(stringQualquer.replace("Hello", "Olá"));

// Tamanho da String
console.log(stringQualquer.length);

//                       01234567890
// let stringQualquer = "Hello World"
//  negativo             10987654321
// Fatiar a String
console.log(stringQualquer.slice(0, 5));
console.log(stringQualquer.slice(-5));

console.log(stringQualquer.split(" "));
console.log(stringQualquer.split(" ", 1));

// Deixar todo texto Maiúsculo
console.log(stringQualquer.toUpperCase());
// Deixar todo o texto minúsculo
console.log(stringQualquer.toLowerCase());