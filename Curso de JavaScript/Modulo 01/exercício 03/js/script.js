let num = prompt("Digite um número");
let numeroTitulo = document.getElementById("numero-titulo");
let texto = document.getElementById("texto");
num = parseFloat(num);
numeroTitulo.innerHTML = num;
texto.innerHTML = `<ul>
<li>A raiz quadrada é: <strong> ${Math.sqrt(num)}</strong></li>
<li>${num} é inteiro? ${Number.isInteger(num)}</li>
<li>${num} é NaN? ${Number.isNaN(num)}</li>
<li>Arredondado para baixo: ${Math.floor(num)}</li>
<li>Arredondado para cima: ${Math.ceil(num)}</li>
<li>Com duas casas decimaisi: ${num.toFixed(2)}</li>
</ul>`;
