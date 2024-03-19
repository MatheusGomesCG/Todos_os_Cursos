let num1 = 1;
let num2 = 2.513123123213213;
let temp = num1 * 'Olá';
num1 = num1.toString(); //convertendo um numero para string

console.log(typeof num1);
console.log(num2.toFixed(2)); //fixar as casa decimais

console.log(Number.isInteger(num1)); //Verifica se o número é do tipo inteiro
console.log(Number.isNaN(temp)); //Verifica se o número é do tipo Not a number