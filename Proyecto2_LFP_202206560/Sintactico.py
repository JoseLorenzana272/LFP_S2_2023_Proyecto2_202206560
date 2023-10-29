from Errores.Errores import *
from Instrucciones.Claves_declaracion import *
from Instrucciones.Registros_declaracion import *
from Instrucciones.Imprimir import *
from Instrucciones.imprimirln import *
from Instrucciones.Conteo import *
from Instrucciones.Promedio import *
from Instrucciones.datos import *
from Instrucciones.Max import *
from Instrucciones.Min import *
from Instrucciones.Sumar import *
from Instrucciones.contarsi import *
from Instrucciones.Reporte import *
global n_linea
global n_columna
global lista_lexemas_sintacticos
global instrucciones_sintacticas
global lista_errores



def instrucciones_sintactico(lista_lexemas):

    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'Claves':
            lista_elementos = []
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        if lex.operar(None) == '"':
                            continue
                        elif lex.operar(None) == ',':
                            continue
                        elif lex.operar(None) == ']':
                            return DeclaracionClaves(palabra_reservada.lexema, lista_elementos, lex.getFila(), lex.getColumna())
                        else:
                            lista_elementos.append(lex.lexema)
        #COLOQUË ESTOOOOOOOOOOOOOO
        elif lexema.operar(None) == 'Registros':
            lista_registros = []
            lista_agrupar = []
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        if lex.operar(None) == '"':
                            continue
                        elif lex.operar(None) == ',':
                            continue
                        elif lex.operar(None) == '{':
                            continue
                        elif lex.operar(None) == '}':
                            lista_registros.append(lista_agrupar)
                            lista_agrupar = []
                        elif lex.operar(None) == ']':
                            return DeclaracionRegistros(palabra_reservada.lexema, lista_registros, lex.getFila(), lex.getColumna())
                        else:
                            lista_agrupar.append(lex.lexema)


        elif lexema.operar(None) == 'imprimir':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Imprimir(texto.lexema, lexema.getFila(), lexema.getColumna())

        elif lexema.operar(None) == 'imprimirln':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return ImprimirLn(texto.lexema, lexema.getFila(), lexema.getColumna())

        elif lexema.operar(None) == 'conteo':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                parentesis = lista_lexemas.pop(0)
                if parentesis.operar(None) == ')':
                    punto_coma = lista_lexemas.pop(0)
                    if punto_coma.operar(None) == ';':
                        return Contar(lexema.getFila(), lexema.getColumna())

        elif lexema.operar(None) == 'promedio':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Promedio(texto.lexema, lexema.getFila(), lexema.getColumna())

        elif lexema.operar(None) == 'datos':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                parentesis = lista_lexemas.pop(0)
                if parentesis.operar(None) == ')':
                    punto_coma = lista_lexemas.pop(0)
                    if punto_coma.operar(None) == ';':
                        return Datos(lexema.getFila(), lexema.getColumna())

        elif lexema.operar(None) == 'max':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Max(texto.lexema, lexema.getFila(), lexema.getColumna())

        elif lexema.operar(None) == 'min':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Min(texto.lexema, lexema.getFila(), lexema.getColumna())

        elif lexema.operar(None) == 'sumar':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Sumar(texto.lexema, lexema.getFila(), lexema.getColumna())

        elif lexema.operar(None) == 'contarsi':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)

                    if comillas.operar(None) == '"':
                        coma = lista_lexemas.pop(0)
                        if coma.operar(None) == ',':
                            numero = lista_lexemas.pop(0)  # Asume que cualquier número es válido
                            comas = lista_lexemas.pop(0)

                            if comas.operar(None) == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.operar(None) == ';':
                                    return ContarSi(texto.lexema, numero.lexema, lexema.getFila(), lexema.getColumna())

        elif lexema.operar(None) == 'exportarReporte':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                lexema = lista_lexemas.pop(0)
                if lexema.operar(None) == '"':
                    titulo = lista_lexemas.pop(0)
                    lexema = lista_lexemas.pop(0)
                    if lexema.operar(None) == '"':
                        lexema = lista_lexemas.pop(0)
                        if lexema.operar(None) == ')':
                            lexema = lista_lexemas.pop(0)
                            if lexema.operar(None) == ';':
                                return Reporte(titulo.lexema, lexema.getFila(), lexema.getColumna())

        '''else:
            error = Errores("Error sintáctico: Token inesperado -> " + lexema.lexema, "Sintáctico", lexema.getFila(),
                            lexema.getColumna())
            lista_errores.append(error)'''




