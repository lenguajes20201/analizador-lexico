symbols=['+','-','*','/','%',
        '<','>','=','!','(',
        ')','[',']',',',':',
        '.']

class Token:

    def __init__(self, type_, position, value=None ):
        self.type = type_
        self.value = value
        self.position = position

    def __str__(self):
        if self.value:
            return f'<{self.type}, {self.value}, {self.position.line}, {self.position.col}>'
        if self.type == 'tk_error':
            return f'>>> Error lexico(linea:{self.position.line},posicion:{self.position.col})'
        return f'<{self.type}, {self.position.line}, {self.position.col}>'
    
    def __repr__(self):
        if self.value:
            return f'<{self.type}, {self.value}, {self.position.line}, {self.position.col}>'
        if self.type == 'tk_error':
            return f'>>> Error lexico(linea:{self.position.line},posicion:{self.position.col})'
        return f'<{self.type}, {self.position.line}, {self.position.col}>'



class Position:
    def __init__(self, index, line, col):
        self.index = index
        self.line = line
        self.col = col

    def __str__(self):
        return f'idx: {self.index}, line: {self.line}, col: {self.col} '

    def advance(self, current_char):
        self.index += 1
        self.col += 1

        if current_char == '\n':
            self.line +=1
            self.col = 1

        return self

    def copy(self):
        return Position(self.index,self.line,self.col)


def analyzer(string):

    token =None

    comment_mode =False

    for index, char in enumerate(string,start=0):
        
        #Se actualiza indice, fila y columna al caracter actual
        pos.advance(char)

        #Si hay un comentario desactiva todo
        if char == '#':
            comment_mode =True
        #Se vuelve a activar en una nueva linea
        elif char == '\n':
            comment_mode =False

        
        if not comment_mode:

            if char == '+':
                token= Token('tk_sum', pos.copy())
                
            if char == '*':
                token= Token('tk_mul', pos.copy())

                
            elif char == '%': 
                token=Token('tk_mod',pos.copy())

                
            elif char == '(': 
                token=Token('tk_par_izq',pos.copy())

                
            elif char == ')': 
                token=Token('tk__par_der',pos.copy())

                
            elif char == '[': 
                token=Token('tk_llave_izq',pos.copy())
                
            elif char == ']': 
                token=Token('tk_llave_der',pos.copy())
                
            elif char == ',': 
                token=Token('tk_coma',pos.copy())
                
            elif char == '.': 
                token=Token('tk_punto',pos.copy())

                
            elif char == ':': 
                token=Token('tk_dospuntos',pos.copy())

                
            elif char == '-':
                if string[index+1] == '>': 
                    token=Token('tk_ejecuta',pos.copy())
                    pos.advance(char)  
                else:
                    token =Token('tk_res',pos.copy())
                    
            elif char == '<':
                if string[index+1] == '=': 
                    token=Token('tk_menorig',pos.copy())
                    pos.advance(char)  
                else:
                    token =Token('tk_menor',pos.copy())
                    
            elif char == '>':
                if string[index+1] == '=': 
                    token=Token('tk_mayorig',pos.copy())
                    pos.advance(char)   
                else:
                    token =Token('tk_mayor',pos.copy())
                    
            elif char == '=':
                if string[index+1] == '=': 
                    token=Token('tk_igual',pos.copy())
                    pos.advance(char)
                else:
                    token =Token('tk_asig',pos.copy())

            elif char == '!':
                if string[index+1] == '=': 
                    token=Token('tk_diferente',pos.copy())
                    pos.advance(char)
            
            #En teoria aqui va lo demas :p
            else:
                #token =Token('tk_error',pos.copy())
                pass
            
            #Si el token no esta vacio, sale del ciclo y retorna
            if token != None:
                break
       
    return token


#Programa de prueba
f = open("test.txt","r")
text = f.read()

pos = Position(0,1,0)
tokens=[]
while text[pos.index: ]:
    token = analyzer(text[pos.index:])
    print(token)
    tokens.append(token)

# Los tokens imprimen acorde a lo que se define en Token.__repr__()
print(tokens)



