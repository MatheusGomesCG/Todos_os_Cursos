let alunos = ["Rebeca", "Matheus", "Jessé"];
alunos[1] = "Matheus G"; //Altera
alunos.push("Josefa"); //Adiciona no final
alunos.unshift("Jerry"); //Adiciona no começo
alunos.pop(); //Remove do final (pode salvar numa variável)
alunos.shift(); //Remove do inicio
// delete alunos[1]; //Apaga o elemento no item1 porém fica vázio no local
alunos.slice(0, 3); //Fatiar o array
console.log(alunos);
console.log(typeof alunos);
console.log(alunos instanceof Array);