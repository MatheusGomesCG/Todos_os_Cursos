function saudacao(nome) {
    return `Bom dia ${nome}!`;
}

const variavel = saudacao('Matheus');
console.log(variavel);

function soma(x = 1, y = 1) {
    return x+y;
}

console.log(soma(2, 2));

const raiz = (n) => {
    return Math.sqrt(n);
};

console.log(raiz(9));