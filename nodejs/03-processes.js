//console.log(process.argv); //Trae un arreglo de lo escrito en consola

function params(p) {
    let index = process.argv.indexOf(p);
    //console.log(index);
    return process.argv[index + 1];
}

let userName = params('--nombre');
console.log(`Tu nombre es: ${userName}`);