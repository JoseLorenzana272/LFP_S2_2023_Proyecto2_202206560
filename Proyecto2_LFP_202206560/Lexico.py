import html

from Abstract.Numero import *
from Abstract.Lexema import *
from Errores.Errores import *

palabras_reservadas = {
    'RCLAVES': 'Claves',
    'RREGISTROS': 'Registros',
    'RCOMENTARIO': 'Comentario',
    'RIMPRIMIR': 'imprimir',
    'RIMPRIMIRLN': 'imprimirln',
    'RCONTEO': 'conteo',
    'RPROMEDIO': 'promedio',
    'RCONTARSI': 'contarsi',
    'RDATOS': 'datos',
    'RSUMAR': 'sumar',
    'RMAX': 'max',
    'RMIN': 'min',
    'REXPORTARREPORTE': 'ExportarReporte',
    'RIGUAL': '=',
    'RCOMA': ',',
    'RCORCHETE_ABRIR': '[',
    'RCORCHETE_CERRAR': ']',
    'RLLAVE_ABRIR': '{',
    'RLLAVE_CERRAR': '}',
    'RCOMILLA': '"',
    'RPUNTOTCOMA': ';',

}

lexema = list(palabras_reservadas.values())
global n_linea
global n_columna
global instrucciones
global lista_lexemas


n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []

def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = 0
    palabras_reservadas = ['Claves', 'imprimir']
    multiline_comment = False
    while cadena:
        char = cadena[puntero]
        puntero += 1

        if char == '"':
            l = Lexema('"', n_linea, n_columna, 'COMILLA')
            lista_lexemas.append(l)
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna, 'TEXTO')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('"', n_linea, n_columna, 'COMILLA')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("Claves"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'CLAVES')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0

        #COLOQUÉ ESTOOOOOOOOOOOO
        elif cadena.startswith("Registros"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'REGISTROS')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0

        elif cadena.startswith("imprimir"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'IMPRIMIR')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("conteo"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'CONTEO')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("promedio"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'PROMEDIO')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("datos"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'DATOS')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("max"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'MAX')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("min"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'MIN')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("sumar"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'SUMAR')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("contarsi"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'CONTARSI')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("exportarReporte"):
            lexema, cadena = armar_instruccion(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'EXPORTARREPORTE')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna += 1
                #! Armamos lexema como clase
                n = Numero(token, n_linea, n_columna, 'NUMERO')

                lista_lexemas.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0

        elif char == '[':
            # ! Armamos lexema como clase
            c = Lexema(char, n_linea, n_columna, 'CORCHETE_IZQ')

            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ']':
            # ! Armamos lexema como clase
            c = Lexema(char, n_linea, n_columna, 'CORCHETE_DER')

            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ';':

            c = Lexema(char, n_linea, n_columna, 'PUNTOYCOMA')

            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == '=':
            c = Lexema(char, n_linea, n_columna, 'IGUAL')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ',':
            c = Lexema(char, n_linea, n_columna, 'COMA')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ')':
            c = Lexema(char, n_linea, n_columna, 'PARDER')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == '#':
            l = Lexema('#', n_linea, n_columna, 'COMENTARIO_UNA_LINEA')
            lista_lexemas.append(l)
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                # Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna, 'TEXTO')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0


        elif char == "'":
            if cadena[puntero:puntero + 3] == "'''":
                n_columna += 3  # Avanzar más allá de las tres comillas
                puntero += 3
                while puntero < len(cadena):
                    if cadena[puntero:puntero + 3] == "'''":
                        n_columna += 3  # Avanzar más allá de las tres comillas
                        puntero += 3
                        break
                    elif cadena[puntero] == '\n':
                        n_linea += 1
                        n_columna = 1
                    else:
                        puntero += 1
                        n_columna += 1
        elif char == "\t":
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == "\n":
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1

        elif char == '{':
            c = Lexema(char, n_linea, n_columna, 'LLAVE_IZQ')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
        elif char == '}':
            c = Lexema(char, n_linea, n_columna, 'LLAVE_DER')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ' ' or char == '\r' or char == '.' or char == ':':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0
        else:
            lista_errores.append(Errores(char, 'Léxico', n_linea, n_columna))
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

    with open("tabla_errores.html", "w") as archivo_html:
        # Escribe el encabezado del HTML
        archivo_html.write('<!DOCTYPE html>\n')
        archivo_html.write('<html>\n')
        archivo_html.write('<head>\n')
        archivo_html.write(
            '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n')
        archivo_html.write('</head>\n')
        archivo_html.write('<body>\n')

        # Crea una tabla con estilos de Bootstrap
        archivo_html.write('<div class="container mt-4">\n')
        archivo_html.write('<table class="table table-striped table-bordered">\n')
        archivo_html.write('<thead class="thead-dark">\n')
        archivo_html.write('<tr><th>Lexema</th><th>Tipo</th><th>Fila</th><th>Columna</th></tr>\n')
        archivo_html.write('</thead>\n')
        archivo_html.write('<tbody>\n')

        # Recorre la lista de errores y agrega cada error como una fila en la tabla
        for error in lista_errores:
            lexema = html.escape(error.lexema)
            tipo = html.escape(error.tipo)
            fila = error.fila
            columna = error.columna

            fila_html = f"<tr><td>{lexema}</td><td>{tipo}</td><td>{fila}</td><td>{columna}</td></tr>\n"
            archivo_html.write(fila_html)

        # Cierra la tabla y el archivo HTML
        archivo_html.write('</tbody>\n')
        archivo_html.write('</table>\n')
        archivo_html.write('</div>\n')
        archivo_html.write('</body>\n')
        archivo_html.write('</html>\n')

    return lista_lexemas



def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == '"' or char == '\n' or char == '\t' or char == '(' or char == ')':
            return lexema, cadena[len(puntero):]    #! si encuentra una  " termino de leer el token
        else:
            lexema += char   #! creamos nuestros Token
    return None, None

def armar_instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas

    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == '"' or char == '\n' or char == '\t' or char == '(' or char == ')' or char == ' ' or char == '=':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None

def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal =  False

    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True

        if char == ' ' or char == '\n' or char == '\t' or char == ',' or char == ')' or char == '}':
            if is_decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            if char != ',': #! si no es una coma lo agregamos al numero
                numero += char
    return None, None
