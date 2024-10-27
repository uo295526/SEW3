import xml.etree.ElementTree as ET

def xml_to_kml(xml_file, kml_file):
    # Cargar el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Espacio de nombres para el XML
    ns = {'ns': 'http://www.uniovi.es'}

    # Crear el archivo KML
    with open(kml_file, 'w') as kml:
        # Escribir cabecera del archivo KML
        kml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        kml.write('  <Document>\n')
        kml.write(f'    <name>{root.find("ns:nombre", ns).text} - Coordenadas de los Tramos</name>\n')

        # Recorrer los tramos del circuito
        for tramo in root.findall('ns:puntosTramos/ns:tramoActual', ns):
            nombre_tramo = tramo.get('nombreTramo')
            punto_final = tramo.find('ns:puntoFinalTramo', ns)
            nombre_punto = punto_final.get('nombrePuntoFinal')
            longitud = punto_final.get('longitud')
            latitud = punto_final.get('latitud')
            altitud = punto_final.get('altitud')

            # Escribir cada tramo como un PlaceMark en el KML
            kml.write('    <Placemark>\n')
            kml.write(f'      <name>{nombre_punto}</name>\n')
            kml.write(f'      <description>{nombre_tramo}</description>\n')
            kml.write('      <Point>\n')
            kml.write(f'        <coordinates>{longitud},{latitud},{altitud}</coordinates>\n')
            kml.write('      </Point>\n')
            kml.write('    </Placemark>\n')

        # Escribir cierre del archivo KML
        kml.write('  </Document>\n')
        kml.write('</kml>\n')

# Usar el programa
if __name__ == "__main__":
    xml_file = 'circuitoEsquema.xml'  # Nombre del archivo XML de entrada
    kml_file = 'circuito.kml'  # Nombre del archivo KML de salida
    xml_to_kml(xml_file, kml_file)
    print(f"El archivo KML '{kml_file}' se ha generado correctamente.")