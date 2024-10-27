#-------------------------------------------------------------------------------
# Convertidor de archivos xml a kml mediante python
#-------------------------------------------------------------------------------

import xml.etree.ElementTree as ET

class Kml(object):
    def __init__(self):
        """
        Crea el elemento raíz y el espacio de nombres
        """
        self.raiz = ET.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
        self.doc = ET.SubElement(self.raiz,'Document')

    def addPlacemark(self,nombre,descripcion,long,lat,alt, modoAltitud):
        """
        Añade un elemento <Placemark> con puntos <Point>
        """
        pm = ET.SubElement(self.doc,'Placemark')
        ET.SubElement(pm,'name').text = '\n' + nombre + '\n'
        ET.SubElement(pm,'description').text = '\n' + descripcion + '\n'
        punto = ET.SubElement(pm,'Point')
        ET.SubElement(punto,'coordinates').text = '\n{},{},{}\n'.format(long,lat,alt)
        ET.SubElement(punto,'altitudeMode').text = '\n' + modoAltitud + '\n'

    def addLineString(self,nombre,extrude,tesela, listaCoordenadas, modoAltitud, color, ancho):
        """
        Añade un elemento <Placemark> con líneas <LineString>
        """
        ET.SubElement(self.doc,'name').text = '\n' + nombre + '\n'
        pm = ET.SubElement(self.doc,'Placemark')
        ls = ET.SubElement(pm, 'LineString')
        ET.SubElement(ls,'extrude').text = '\n' + extrude + '\n'
        ET.SubElement(ls,'tessellation').text = '\n' + tesela + '\n'
        ET.SubElement(ls,'coordinates').text = '\n' + listaCoordenadas + '\n'
        ET.SubElement(ls,'altitudeMode').text = '\n' + modoAltitud + '\n'

        estilo = ET.SubElement(pm, 'Style')
        linea = ET.SubElement(estilo, 'LineStyle')
        ET.SubElement (linea, 'color').text = '\n' + color + '\n'
        ET.SubElement (linea, 'width').text = '\n' + ancho + '\n'

    def escribir(self,nombreArchivoKML):
        """
        Escribe el archivo KML con declaración y codificación
        """
        arbol = ET.ElementTree(self.raiz)
        arbol.write(nombreArchivoKML, encoding='utf-8', xml_declaration=True)

    def ver(self):
        """
        Muestra el archivo KML. Se utiliza para depurar
        """
        print("\nElemento raiz = ", self.raiz.tag)

        if self.raiz.text != None:
            print("Contenido = "    , self.raiz.text.strip('\n')) #strip() elimina los '\n' del string
        else:
            print("Contenido = "    , self.raiz.text)

        print("Atributos = "    , self.raiz.attrib)

        # Recorrido de los elementos del árbol
        for hijo in self.raiz.findall('.//'): # Expresión XPath
            print("\nElemento = " , hijo.tag)
            if hijo.text != None:
                print("Contenido = ", hijo.text.strip('\n')) #strip() elimina los '\n' del string
            else:
                print("Contenido = ", hijo.text)
            print("Atributos = ", hijo.attrib)


def main():

    #convertirXMLaKML('circuitoEsquema.xml', 'circuitoEsquema.kml')
    
    nuevoKML = Kml()

    try:
        tree = ET.parse('circuitoEsquema.xml')
    except IOError:
        print("No se ha encontrado el archivo xml de entrada")
        exit()
    except ET.ParseError:
        print("Error ocurrido al procesar el xml de entrada")
        exit()
    raiz = tree.getroot()
    tramosCircuito = raiz.findall('puntosTramos/tramoActual')

    nuevoKML = Kml()

    for tramo in tramosCircuito:
        puntoFinal = tramo.find('puntoFinalTramo')
        nombreTramo = tramo.attrib['nombreTramo']
        nombrePuntoFinal = puntoFinal.attrib['nombrePuntoFinal']
        longitudPunto = puntoFinal.attrib['longitud']
        latitudPunto = puntoFinal.attrib['latitud']
        altitudPunto = puntoFinal.attrib['altitud']
        #ahora con los datos obtenidos, lo anadimos al KML
        nuevoKML.addPlacemark(nombreTramo, nombrePuntoFinal, longitudPunto, latitudPunto, altitudPunto, 'relativeToGround')

    #anadimos un placemark para cada tramo del circuito. Se la pasaria:
    # El propio Kml, El nombre del punto, Las Tres coordenadas, y para acabar El modo de la altitud
    #nuevoKML.addPlacemark()

    #"""Creación del archivo en formato KML"""
    nombreKML = "circuitoEsquema.kml"
    nuevoKML.escribir(nombreKML)
    print("Creado el archivo: ", nombreKML)



if __name__ == "__main__":
    main()