# Manual Técnico del Proyecto 2
## José Daniel Lorenzana Medina - 202206560

## Introducción

Este manual técnico describe en detalle la estructura y el funcionamiento del analizador léxico y sintáctico. El analizador se encarga de procesar un lenguaje de programación específico, identificando tokens, declaraciones y comandos.

## Estructura del Código

El código está dividido en dos partes principales: el analizador léxico y el analizador sintáctico. A continuación, se presenta una descripción de cada sección del código:

## Analizador Léxico

El analizador léxico es responsable de dividir el código fuente en tokens, identificando palabras clave, números, comillas, paréntesis, corchetes y otros elementos del lenguaje. Aquí están los componentes clave del analizador léxico:

<img src="https://github.com/JoseLorenzana272/LFP_S2_2023_Proyecto2_202206560/assets/122989930/b4abdddb-6a26-4d17-a067-3415a2540a52" alt="Texto alternativo" width="1000" height="1200">




### Lista de Palabras Reservadas

Se define un diccionario llamado "palabras_reservadas", en el cual se asocia el nombre de la palabra con su identificador.

<img src="https://github.com/JoseLorenzana272/LFP_S2_2023_Proyecto2_202206560/assets/122989930/7b6e6fa4-93e8-4922-96aa-5a2926bdfc28" alt="Texto alternativo" width="700" height="900">

### Funciones para Identificar Tokens

- La función "instruccion(cadena)" procesa la cadena de entrada y genera una lista de tokens.
- La función "armar_lexema(cadena)" divide la cadena en tokens y reconoce números y texto.
- La función "armar_instruccion(cadena)" identifica declaraciones y palabras clave.
- La función "armar_numero(cadena)" reconoce números enteros y flotantes.

### Manejo de Errores

Se registran errores léxicos en una lista llamada "lista_errores" cuando se encuentra un carácter no reconocido.

### Generación de un Archivo HTML de Errores

Se genera un archivo HTML que muestra los errores léxicos en una tabla con estilo Bootstrap.

## Analizador Sintáctico

El analizador sintáctico se encarga de analizar la estructura de las instrucciones y construir objetos que representan las declaraciones y comandos del lenguaje. A continuación se describen los aspectos clave del analizador sintáctico:
![image](https://github.com/JoseLorenzana272/LFP_S2_2023_Proyecto2_202206560/assets/122989930/79c52d98-4ac0-43f5-aea4-d99211574d09)


### Función "instrucciones_sintactico(lista_lexemas)"

Esta función toma una lista de lexemas generada por el analizador léxico y analiza la estructura sintáctica del código. Reconoce declaraciones de claves, registros y comandos como imprimir, contar, promedio, datos, máximo, mínimo, sumar y contarsi.

### Declaraciones y Comandos

- Declaración de Claves: Se reconoce declaraciones que comienzan con "Claves", seguidas de una lista de elementos entre corchetes.
- Declaración de Registros: Se reconoce declaraciones que comienzan con "Registros", seguidas de una lista de registros con elementos entre corchetes y llaves.
- Comandos de Impresión: Se reconocen comandos de impresión (imprimir y imprimirln) con texto entre comillas.
- Comandos Estadísticos: Se reconocen comandos para contar, promediar, obtener el máximo, el mínimo, sumar y contar si se cumplen ciertas condiciones.
- Comando ExportarReporte: Se reconoce el comando ExportarReporte para generar reportes.

### Manejo de Errores Sintácticos

La generación de errores sintácticos se comenta para evitar que se registren errores mientras se depura el analizador.

## Uso del Analizador

Para utilizar el analizador, se deben seguir estos pasos:

1. Se llama la función "instruccion(cadena)" del analizador léxico con la cadena de entrada.
2. Se obtiene la lista de lexemas generada por el analizador léxico.
3. Se llama la función "instrucciones_sintactico(lista_lexemas)" del analizador sintáctico con la lista de lexemas.
4. El analizador sintáctico generará objetos que representan las declaraciones y comandos del lenguaje.

## Conclusiones

Este manual técnico proporciona una visión general del funcionamiento y la estructura del analizador léxico y sintáctico. Esta información puede ser utilizada para comprender y depurar el código, así como para extender su funcionalidad si es necesario. Además, se debe tener en cuenta que el código presenta partes comentadas que manejan errores sintácticos; es importante habilitarlas cuando se desee validar la sintaxis del lenguaje de programación.

## Notas Adicionales

- Es importante asegurarse de que los nombres de las clases y los métodos correspondan a la estructura de directorios del proyecto. En el código proporcionado, se importan clases como "Abstract.Numero" y "Instrucciones.Claves_declaracion". Debe asegurarse de que estas rutas sean correctas y se correspondan con la estructura del proyecto.

- El código genera un archivo HTML llamado "tabla_errores.html" para mostrar los errores léxicos. Es necesario asegurarse de que la ruta y el nombre del archivo sean adecuados para el proyecto.

- Se debe considerar habilitar el manejo de errores sintácticos en el analizador sintáctico para validar la estructura del lenguaje de programación.

- Actualmente, el código no maneja comentarios de varias líneas y algunos caracteres especiales. Pueden extender el analizador para incluir estas funcionalidades si es necesario.


## AFD (Autómata Finito Determinista) para el Analizador Léxico

### Estados del AFD:
1. Estado Inicial (q0)
2. Estado de Identificador (q1)
3. Estado de Entero (q2)
4. Estado de Flotante (q3)
5. Estado de Operador (q4)
6. Estado de Comillas (q5)
7. Estado de Comentario (q6)
8. Estado de Comentario Multilínea (q7)
9. Estado de Comentario de Una Línea (q8)

### Alfabeto:
- Letras (a-z, A-Z)
- Dígitos (0-9)
- Comillas (")
- Espacios en blanco
- Caracteres especiales (',', '=', '[', ']', '(', ')', '{', '}', ';', '#', '\t', '\n')

### Función de Transición (Tabla de Transiciones):

| Estado Actual | Símbolo de Entrada | Estado Siguiente |
|---------------|---------------------|-----------------|
| q0            | Letra               | q1              |
| q0            | Dígito              | q2              |
| q0            | '"'                 | q5              |
| q0            | Espacio             | q0              |
| q0            | ','                 | q0              |
| q0            | '='                 | q0              |
| q0            | '['                 | q0              |
| q0            | ']'                 | q0              |
| q0            | '('                 | q0              |
| q0            | ')'                 | q0              |
| q0            | '{'                 | q0              |
| q0            | '}'                 | q0              |
| q0            | ';'                 | q0              |
| q0            | '#'                 | q8              |
| q0            | '\t'                | q0              |
| q0            | '\n'                | q0              |
| q1            | Letra               | q1              |
| q1            | Dígito              | q1              |
| q2            | Dígito              | q2              |
| q2            | '.'                 | q3              |
| q3            | Dígito              | q3              |
| q3            | Espacio             | q0              |
| q3            | ','                 | q0              |
| q3            | '='                 | q0              |
| q3            | '['                 | q0              |
| q3            | ']'                 | q0              |
| q3            | '('                 | q0              |
| q3            | ')'                 | q0              |
| q3            | '{'                 | q0              |
| q3            | '}'                 | q0              |
| q3            | ';'                 | q0              |
| q3            | '#'                 | q8              |
| q3            | '\t'                | q0              |
| q3            | '\n'                | q0              |
| q4            | Espacio             | q0              |
| q4            | ','                 | q0              |
| q4            | '='                 | q0              |
| q4            | '['                 | q0              |
| q4            | ']'                 | q0              |
| q4            | '('                 | q0              |
| q4            | ')'                 | q0              |
| q4            | '{'                 | q0              |
| q4            | '}'                 | q0              |
| q4            | ';'                 | q0              |
| q4            | Letra               | q1              |
| q4            | Dígito              | q2              |
| q4            | '"'                 | q5              |
| q4            | '#'                 | q8              |
| q4            | '\t'                | q0              |
| q4            | '\n'                | q0              |
| q5            | Cualquier símbolo   | q5              |
| q5            | '"'                 | q0              |
| q6            | '#'                 | q6              |
| q6            | Cualquier símbolo   | q6              |
| q7            | "'''""              | q0              |
| q7            | Cualquier símbolo   | q7              |
| q8            | '\n'                | q0              |


## Método del Árbol utilizado en el analizador Léxico junto con el Sintáctico
- `analizador_lexico(cadena)`
  - Declaración de variables globales
  - Inicialización de `lista_lexemas`, `instrucciones`, `lista_errores`
  - Bucle principal mientras `cadena` no esté vacía
    - Si el carácter actual es `"`
      - Agregar un lexema para la comilla (`"`)
      - Llamar a la función `armar_lexema` para obtener un texto entre comillas y agregarlo como un lexema de tipo `'TEXTO'`
      - Agregar un lexema para la comilla (`"`)
    - Si la cadena comienza con `"Claves"`
      - Llamar a la función `armar_instruccion` para obtener la instrucción `"Claves"` y agregarla como un lexema de tipo `'CLAVES'`
    - Si la cadena comienza con `"Registros"`
      - Llamar a la función `armar_instruccion` para obtener la instrucción `"Registros"` y agregarla como un lexema de tipo `'REGISTROS'`
    - Si la cadena comienza con `"imprimir"`
      - Llamar a la función `armar_instruccion` para obtener la instrucción `"imprimir"` y agregarla como un lexema de tipo `'IMPRIMIR'`
      - Agregar un lexema para `(` (`PARIZQ`)
    - Si la cadena comienza con `"conteo"`
      - Llamar a la función `armar_instruccion` para obtener la instrucción `"conteo"` y agregarla como un lexema de tipo `'CONTEO'`
      - Agregar un lexema para `(` (`PARIZQ`)
    - Si la cadena comienza con `"promedio"`
      - Llamar a la función `armar_instruccion` para obtener la instrucción `"promedio"` y agregarla como un lexema de tipo `'PROMEDIO'`
      - Agregar un lexema para `(` (`PARIZQ`)
    - Si la cadena comienza con `"datos"`
      - Llamar a la función `armar_instruccion` para obtener la instrucción `"datos"` y agregarla como un lexema de tipo `'DATOS'`
      - Agregar un lexema para `(` (`PARIZQ`)
    - Si la cadena comienza con `"max"`
      - Llamar a la función `armar_instruccion` para obtener la instrucción `"max"` y agregarla como un lexema de tipo `'MAX'`
      - Agregar un lexema para `(` (`PARIZQ`)
    - Si la cadena comienza con `"min"`
      - Llamar a la función `armar_instruccion` para obtener la instrucción `"min"` y agregarla como un lexema de tipo `'MIN'`
      - Agregar un lexema para `(` (`PARIZQ`)
    - Si la cadena comienza con `"sumar"`
      - Llamar a la función `armar_instruccion` para obtener la instrucción `"sumar"` y agregarla como un lexema de tipo `'SUMAR'`
      - Agregar un lexema para `(` (`PARIZQ`)
    - Si el carácter actual es un dígito
      - Llamar a la función `armar_numero` para obtener un número y agregarlo como un lexema de tipo `'NUMERO'`
    - Si el carácter actual es `[`
      - Agregar un lexema para `[` (`CORCHETE_IZQ`)
    - Si el carácter actual es `]`
      - Agregar un lexema para `]` (`CORCHETE_DER`)
    - Si el carácter actual es `;`
      - Agregar un lexema para `;` (`PUNTOYCOMA`)
    - Si el carácter actual es `=`
      - Agregar un lexema para `=` (`IGUAL`)
    - Si el carácter actual es `,`
      - Agregar un lexema para `,` (`COMA`)
    - Si el carácter actual es `)`
      - Agregar un lexema para `)` (`PARDER`)
    - Si el carácter actual es `#`
      - Agregar un lexema para `#` (`COMENTARIO_UNA_LINEA`)
      - Llamar a la función `armar_lexema` para obtener un comentario y agregarlo como un lexema de tipo `'TEXTO'`
    - Si el carácter actual es `'"`
      - Verificar si es un comentario multilinea
      - Si es un comentario multilinea, avanzar a través del comentario y actualizar `n_linea` y `n_columna`
    - Si el carácter actual es `\t`
      - Avanzar cuatro espacios y actualizar `n_columna`
    - Si el carácter actual es `\n`
      - Actualizar `n_linea` y restablecer `n_columna` a 1
    - Si el carácter actual es `{`
      - Agregar un lexema para `{` (`LLAVE_IZQ`)
    - Si el carácter actual es `}`
      - Agregar un lexema para `}` (`LLAVE_DER`)
    - Si el carácter actual es `' '` o `\r` o `.` o `:`
      - Avanzar un espacio y actualizar `n_columna`
    - Si el carácter actual no coincide con ninguno de los casos anteriores
      - Agregar un lexema con el carácter como texto y tipo `'Léxico Desconocido'` y agregar el error a `lista_errores`
     
    ## Gramática Libre de Contexto (CFG) - Analizador Sintáctico

- `<instrucciones_sintactico>` ::= `<declaracion_claves>` | `<declaracion_registros>` | `<imprimir>` | `<imprimirln>` | `<conteo>` | `<promedio>` | `<datos>` | `<max>` | `<min>` | `<sumar>` | `<contarsi>` | `<exportar_reporte>`
- `<declaracion_claves>` ::= `"Claves" "=" "[" <lista_elementos> "]"`
- `<lista_elementos>` ::= `<elemento> "," <lista_elementos>` | `<elemento>`
- `<elemento>` ::= '"' `<texto>` '"'
- `<texto>` ::= `<cadena_de_texto>`
- `<declaracion_registros>` ::= `"Registros" "=" "[" <lista_registros> "]"`
- `<lista_registros>` ::= `<registro> "," <lista_registros>` | `<registro>`
- `<registro>` ::= "{" <lista_elementos> "}"
- `<imprimir>` ::= `"imprimir" "(" '"' <texto> '"' ")" ";"`
- `<imprimirln>` ::= `"imprimirln" "(" '"' <texto> '"' ")" ";"`
- `<conteo>` ::= `"conteo" "()" ";"`
- `<promedio>` ::= `"promedio" "(" '"' <texto> '"' ")" ";"`
- `<datos>` ::= `"datos" "()" ";"`
- `<max>` ::= `"max" "(" '"' <texto> '"' ")" ";"`
- `<min>` ::= `"min" "(" '"' <texto> '"' ")" ";"`
- `<sumar>` ::= `"sumar" "(" '"' <texto> '"' ")" ";"`
- `<contarsi>` ::= `"contarsi" "(" '"' <texto> '"' "," <numero> ")" ";"`
- `<numero>` ::= `<entero>` | `<decimal>`
- `<exportar_reporte>` ::= `"exportarReporte" "(" '"' <texto> '"' ")" ";"

