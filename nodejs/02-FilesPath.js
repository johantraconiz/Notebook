let path = require('path')

console.log('USO DE MÓDULOS PARA GESTION DE ARCHIVOS.')
console.log(`Ruta en donde estamos ubicados: ${__dirname}`);
console.log(`Ruta en donde estamos ubucados más nombre del archivo ejecutado: ${__filename}`);
console.log(`basename trae la ultima porcion del la ruta porporcionada en su argumento: ${path.basename(__filename)}`);