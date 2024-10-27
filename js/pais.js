class Pais {
    nombre; 
    capital;
    circuito;
    numPoblacion;
    tipoGobierno;
    coordenadasMetaCircuito;
    religion;

    constructor (nombre, capital, numPoblacion){
        this.nombre = nombre;
        this.capital = capital;
        this.numPoblacion = numPoblacion;
    }

    rellenarAtributos(circuito, tipoGobierno, coordenadasMetaCircuito, religion){
        this.circuito = circuito;
        this.tipoGobierno = tipoGobierno;
        this.coordenadasMetaCircuito = coordenadasMetaCircuito;
        this.religion = religion;
    }

    getNombreTexto(){
        return this.nombre;
    }

    getCapitalTexto(){
        return this.capital;
    }

    getInfoSecundaria(){
        return <ul><li>this.circuito</li><li>this.numPoblacion</li><li>this.tipoGobierno</li><li>this.religion</li></ul>;
        //al ya ser una lista de html, se le puede hacer un document.write directamente, no como los anteriores
    }

    escribirCoordenadasMeta(coord){
        this.coordenadasMetaCircuito = coord;
    }
}

//puedo declarar aqui tambien el elemento
var elemento = new Pais("Países Bajos", "Ámsterdam", 17963553);
//y rellenar cosas aqui, dejarlo listo para en el html solo hacer el document.write
