#IMPORTACIONES
import re

# CONSTANTES
KEYWORDS = ['__init__','and',
'as','assert','async','await',
'bool','break','class','continue',
'def','del','elif','else','except',
'False','finally','for','from','global',
'if','import','in','input','int','is',
'lambda','len','None','nonlocal',
'not','object','or','pass','print',
'raise','return','self','str','True',
'try','while','with','yield']

#ERRORES
class Error:
    def __init__(self, pos_start, error_name, details):
        self.pos_start = pos_start
        self.error_name = error_name
        self.details = details

    def __str__(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, details):
        super().__init__(pos_start, 'Error Lexico')

#POSICION
class Position:
    def __init__(self, index, line, col):
        self.index = index
        self.line = line
        self.col = col

    def advance(self, current_char):
        self.index +=1
        self.col += 1

        if current_char == '\n':
            self.line +=1
            self.col = 1
        
        return self
    
    def copy(self):
        return Position(self.index, self.line, self.col)

#TOKENS



#KEYWORDS

#TOKEN
class Token:
    def __init__(self, type_, position, value=None):
        self.type =  type_
        self.value = value
        self.position = position
    
    def __repr__(self):
        if self.value: 
            return f'<{self.type}, {self.value}, {self.position.line}, {self.position.col}>'
        return f'<{self.type}, {self.position.line}, {self.position.col}>'

#ANALIZADOR LEXICO
class Lexer:
    def __init__(self,text):
        self.text = text
        self.pos = Position (-1,1,0)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:

            if re.search(r'[ \t]',self.current_char) is not None:
                self.advance()
            
            elif re.search(r'[0-9]',self.current_char) is not None:
                tokens.append(self.make_number())
           
            elif re.search(r'[a-zA-Z_]',self.current_char) is not None:
                tokens.append(self.make_identifier())
            
            elif self.current_char == '+':
                tokens.append(Token('tk_sum',self.pos.copy()))
                self.advance() 
            
            elif self.current_char == '*':
                tokens.append(Token('tk_mul',position=self.pos.copy()))
                self.advance() 
            
            elif self.current_char == '(':
                tokens.append(Token('tk_par_izq',position=self.pos.copy()))
                self.advance() 
            
            elif self.current_char == ')':
                tokens.append(Token('tk_par_der',position=self.pos.copy()))
                self.advance() 
            
            elif self.current_char == '[':
                tokens.append(Token('tk_llave_izq',position=self.pos.copy()))
                self.advance() 
           
            elif self.current_char == ']':
                tokens.append(Token('tk_llave_der',position=self.pos.copy()))
                self.advance() 
            
            elif self.current_char == '%':
                tokens.append(Token('tk_mod',position=self.pos.copy()))
                self.advance() 
           
            elif self.current_char == ',':
                tokens.append(Token('tk_coma',position=self.pos.copy()))
                self.advance() 
            
            elif self.current_char == '.':
                tokens.append(Token('tk_punto',position=self.pos.copy()))
                self.advance() 
            
            elif self.current_char == ':':
                tokens.append(Token('tk_dospuntos',position=self.pos.copy()))
                self.advance() 
            elif self.current_char == '/':
                self.advance()
                #tokens.append(self.make_div())
            elif self.current_char == '-':
                self.advance()
                #tokens.append(self.make_minus())
            else:
                self.advance()

        return tokens, None
    
    def make_number(self):
        num_str = ''
        start = self.pos.copy()

        while (self.current_char != None) and (re.search(r'[0-9]',self.current_char) is not None):
            num_str += self.current_char
            self.advance()
        
        return Token('tk_entero',start,int(num_str))
    
    def make_identifier(self):
        id_str = ''
        start = self.pos.copy()
    
        while self.current_char != None and (re.search(r'[a-zA-Z0-9_]',self.current_char) is not None):
            id_str += self.current_char
            self.advance()

        if id_str in KEYWORDS: 
            return Token(id_str,position=start)
        else:
            return Token('id',start,id_str)

f = open("test.txt","r")
text = f.read()

lexer = Lexer(text)

print(lexer.make_tokens())
		
    

