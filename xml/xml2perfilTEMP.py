import xml.etree.ElementTree as ET

def xml_to_svg(xml_file, svg_file):
    # Cargar el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Espacio de nombres para el XML
    ns = {'ns': 'http://www.uniovi.es'}

    # Parámetros del SVG
    width = 1000  # Ancho del SVG
    height = 800  # Alto del SVG
    margin = 50   # Margen alrededor del contenido

    # Recoger todas las coordenadas de los tramos
    tramos = root.findall('ns:puntosTramos/ns:tramoActual', ns)
    longitudes = [float(tramo.find('ns:puntoFinalTramo', ns).get('longitud')) for tramo in tramos]
    latitudes = [float(tramo.find('ns:puntoFinalTramo', ns).get('latitud')) for tramo in tramos]

    # Escalar las coordenadas geográficas al tamaño del SVG
    min_long = min(longitudes)
    max_long = max(longitudes)
    min_lat = min(latitudes)
    max_lat = max(latitudes)

    def escalar_longitud(longitud):
        return margin + (longitud - min_long) / (max_long - min_long) * (width - 2 * margin)

    def escalar_latitud(latitud):
        return height - margin - (latitud - min_lat) / (max_lat - min_lat) * (height - 2 * margin)

    # Crear el archivo SVG
    with open(svg_file, 'w') as svg:
        # Escribir cabecera del archivo SVG
        svg.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n')
        svg.write(f'  <rect width="100%" height="100%" fill="white" />\n')

        # Dibujar los puntos y líneas entre los tramos
        for i, tramo in enumerate(tramos):
            punto_final = tramo.find('ns:puntoFinalTramo', ns)
            nombre_punto = punto_final.get('nombrePuntoFinal')
            longitud = float(punto_final.get('longitud'))
            latitud = float(punto_final.get('latitud'))

            # Escalar las coordenadas geográficas a coordenadas SVG
            x = escalar_longitud(longitud)
            y = escalar_latitud(latitud)

            # Dibujar un círculo en cada punto final del tramo
            svg.write(f'  <circle cx="{x}" cy="{y}" r="5" fill="red" />\n')

            # Añadir el nombre del punto final como texto al lado del círculo
            svg.write(f'  <text x="{x + 10}" y="{y}" font-size="12" fill="black">{nombre_punto}</text>\n')

            # Dibujar una línea entre puntos consecutivos
            if i > 0:
                x_prev = escalar_longitud(float(tramos[i - 1].find('ns:puntoFinalTramo', ns).get('longitud')))
                y_prev = escalar_latitud(float(tramos[i - 1].find('ns:puntoFinalTramo', ns).get('latitud')))
                svg.write(f'  <line x1="{x_prev}" y1="{y_prev}" x2="{x}" y2="{y}" stroke="blue" stroke-width="2"/>\n')

        # Cerrar el archivo SVG
        svg.write('</svg>\n')

# Usar el programa
if __name__ == "__main__":
    xml_file = 'circuitoEsquema.xml'  # Nombre del archivo XML de entrada
    svg_file = 'altimetria.svg'  # Nombre del archivo SVG de salida
    xml_to_svg(xml_file, svg_file)
    print(f"El archivo SVG '{svg_file}' se ha generado correctamente.")