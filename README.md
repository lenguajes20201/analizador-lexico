# analizador-lexico
analizador lexico y sintactico para el lenguaje chocopy. taller para la materia lenguajes de programacion 2020-1
___

# Nombres
- Marcelo Escamilla Sanchez
- Nicolas Mateo Casas Ramos
- Ivan Rene Delgado Gonzalez

___
## update 3
- Se implemento el analizador lexico en el archivo chocopyparser.py

- Por ahora hace analisis limitado del caso 0, en la carpeta casos_parser

- Se implemento el error lexico que imprime el lexema erroneo y el conjunto de lexemas esperados.

- El archivo del lexer se renombro a "chocopylexer.py"

- La gramatica se encuentra en el archivo "test2.py" Puede resultar un pooco confuso ese archivo.
___
## update 2
- El archivo chocopy.py tiene el analizador lexico que analiza adecuadamente los 6 casos de prueba en ./casos_lexer

- El manejo de errores esta precario. Pero es suficiente para lo solicitado para esta entrega.

- El manejo de cadenas tambien esta precario. 
___
## update 1
- el archivo test.txt contiene el codigo de ejemplo del enunciado

- Se hizo una prueba de concepto para identificar operadores de un solo caracter +\\*%()[],.:

- Se implemento la clase Position que guarda el indice, linea y columna del caracter que se lee.
   Esta clase contiene el indice(0-indexado), la fila y la columna(ambos 1-indexado) del caracter actual.  
   Una posible idea es que el Token en si sea un objeto con informacion util. El indice es util de manera logica, puesto que el archivo se carga como un arreglo de caracteres. la fila y columna permiten determinar facilmente en donde se encuentra el caracter. Por ahora, la iteracion de caracteres esta despegada de esta clase, sigue siendo una prueba de concepto.

- Se creo la clase Token como un contenedor para los tokens(no se implementa aun)
