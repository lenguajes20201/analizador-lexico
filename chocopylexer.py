#IMPORTACIONES
import re

# CONSTANTES
CHARACTERS = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@','A', 'B', 
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a','b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{',
 '|', '}', '~']

DIGITS= '0123456789'

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
    def __init__(self, pos, error_name, details):
        self.pos = pos
        self.error_name = error_name
        self.details = details

    def __repr__(self):
        result = f'{self.error_name}: {self.details}, {self.pos.line}, {self.pos.col}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos, details):
        super().__init__(pos, '>>> Error Lexico', details)

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

        self.comment_mode = False
        self.token_generated = False

        self.indent_stack = [0]
        self.indent_mode = True

        self.tokens = []

        self.advance()

    def advance(self):

        #comment_mode flag enable/disable
        if self.current_char == '#': self.comment_mode = True
        elif self.current_char == '\n':self.comment_mode = False

        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def make_tokens(self):

        while self.current_char != None:

            if self.comment_mode:
                self.advance()
                if self.current_char == '\n':
                    self.make_indent()

            else:
                if self.current_char in '[\r\t#]':
                    self.advance()

                elif self.current_char in DIGITS:
                    self.tokens.append(self.make_number())
                    self.token_generated = True

                elif re.search(r'[a-zA-Z_]',self.current_char) is not None:
                    self.tokens.append(self.make_identifier())
                    self.token_generated = True

                elif self.current_char == ' ':
                    self.advance()

                elif self.current_char == '\n':
                    if self.token_generated: 
                        self.tokens.append(Token('NEWLINE',self.pos.copy()))
                        self.make_indent()
                        self.token_generated = False
                    else:
                        self.advance()
                    
                elif self.current_char == '+':
                    self.tokens.append(Token('tk_sum',self.pos.copy()))
                    self.advance() 
                    self.token_generated = True

                elif self.current_char == '*':
                    self.tokens.append(Token('tk_mul',position=self.pos.copy()))
                    self.advance() 
                    self.token_generated = True

                elif self.current_char == '(':
                    self.tokens.append(Token('tk_par_izq',position=self.pos.copy()))
                    self.advance()
                    self.token_generated = True 
                
                elif self.current_char == ')':
                    self.tokens.append(Token('tk_par_der',position=self.pos.copy()))
                    self.advance()
                    self.token_generated = True 
                
                elif self.current_char == '[':
                    self.tokens.append(Token('tk_llave_izq',position=self.pos.copy()))
                    self.advance()
                    self.token_generated = True 
            
                elif self.current_char == ']':
                    self.tokens.append(Token('tk_llave_der',position=self.pos.copy()))
                    self.advance() 
                    self.token_generated = True
                
                elif self.current_char == '%':
                    self.tokens.append(Token('tk_mod',position=self.pos.copy()))
                    self.advance() 
                    self.token_generated = True
            
                elif self.current_char == ',':
                    self.tokens.append(Token('tk_coma',position=self.pos.copy()))
                    self.advance() 
                    self.token_generated = True
                
                elif self.current_char == '.':
                    self.tokens.append(Token('tk_punto',position=self.pos.copy()))
                    self.advance() 
                    self.token_generated = True
                
                elif self.current_char == ':':
                    self.tokens.append(Token('tk_dospuntos',position=self.pos.copy()))
                    self.advance() 
                    self.token_generated = True

                elif self.current_char == '/':
                    if self.text[self.pos.index+1] == '/':
                        self.tokens.append(Token('tk_div',position=self.pos.copy()))
                        self.advance()
                        self.advance()
                    else:
                        self.tokens.append(IllegalCharError(self.pos.copy()," '/' caracter invalido"))
                        self.advance()
                        break
                    self.token_generated = True    

                elif self.current_char == '-':
                    if self.text[self.pos.index+1] == '>':
                        self.tokens.append(Token('tk_ejecuta',position=self.pos.copy()))
                        self.advance()
                        self.advance()
                    else:
                        self.tokens.append(Token('tk_res',position=self.pos.copy()))
                        self.advance()
                    self.token_generated = True

                elif self.current_char == '=':
                    if self.text[self.pos.index+1] == '=':
                        self.tokens.append(Token('tk_igual',position=self.pos.copy()))
                        self.advance()
                        self.advance()
                    else:
                        self.tokens.append(Token('tk_asig',position=self.pos.copy()))
                        self.advance()
                    self.token_generated = True

                elif self.current_char == '>':
                    if self.text[self.pos.index+1] == '=':
                        self.tokens.append(Token('tk_mayorig',position=self.pos.copy()))
                        self.advance()
                        self.advance()
                    else:
                        self.tokens.append(Token('tk_mayor',position=self.pos.copy()))
                        self.advance()
                    self.token_generated = True

                elif self.current_char == '<':
                    if self.text[self.pos.index+1] == '=':
                        self.tokens.append(Token('tk_menorig',position=self.pos.copy()))
                        self.advance()
                        self.advance()
                    else:
                        self.tokens.append(Token('tk_menor',position=self.pos.copy()))
                        self.advance()
                    self.token_generated = True

                elif self.current_char == '!':
                    self.advance()
                    if self.current_char == '=':
                        self.advance()
                        self.tokens.append(Token('tk_diferente',position=self.pos.copy()))
                    else:
                        self.tokens.append(IllegalCharError(self.pos.copy()," '!' caracter invalido"))
                        self.advance()
                        break
                    self.token_generated = True

                elif self.current_char == '"':
                    self.tokens.append(self.make_string())
                    self.token_generated = True

                else:
                    self.tokens.append(IllegalCharError(self.pos.copy(),f"'{self.current_char}'caracter invalido"))
                    self.advance()

            if self.tokens:
                if isinstance(self.tokens[-1], Error): break
        self.make_indent()
        return self.tokens

    def make_string(self):
        string_str = '"'
        start = self.pos.copy()
        escape = False
        self.advance()

        escape_characters={
            'n':'\n',
            't':'\t',
            '"':'"'
        }

        while (self.current_char != None) and (self.current_char in CHARACTERS):
            if escape:
                if self.current_char in escape_characters: 
                    string_str += escape_characters.get(self.current_char)
                    escape = False
                else:
                    return IllegalCharError(self.pos.copy(),f"'{self.current_char}'caracter invalido")
            else:
                if self.current_char == '\\':
                    escape = True
                elif self.current_char == '"':
                    string_str += self.current_char
                    self.advance()
                    break
                else:
                    string_str += self.current_char
            self.advance()
            
        if string_str[-1] == '"': return Token('tk_cadena',start,string_str)
        else:  return IllegalCharError(self.pos.copy(),f"cadena invalida")

    def make_number(self):
        num_str = ''
        start = self.pos.copy()

        while (self.current_char != None) and (re.search(r'[0-9]',self.current_char) is not None):
            num_str += self.current_char
            self.advance()
        return Token('tk_entero',start,num_str)
    
    def make_identifier(self):
        id_str = ''
        start = self.pos.copy()
    
        while self.current_char != None and (re.search(r'[a-zA-Z0-9_]',self.current_char) is not None):
            id_str += self.current_char
            self.advance()

        if id_str in KEYWORDS: 
            return Token(id_str,start)
        else:
            return Token('id',start,id_str)
    def make_indent(self):
        self.advance()
        indent_count = 0
        indent_index =self.pos.index
        # Start counting whitespaces, reset on newlines
        while self.current_char is not None and self.current_char in ' \n':
            if self.current_char == ' ': indent_count += 1
            elif self.current_char == '\n':
                indent_index = self.pos.index+1
                indent_count = 0
            self.advance()
        
        start = Position(indent_index,self.pos.line,1)
        if self.current_char is None: start = self.pos.copy()

        if indent_count > self.indent_stack[-1]:
            self.indent_stack.append(indent_count)
            self.tokens.append(Token('INDENT',start))
        else:
            while indent_count < self.indent_stack[-1]:
                self.indent_stack.pop()
                self.tokens.append(Token('DEDENT',start))
        
        return None

f = open(f"casos_lexer/{0}.txt","r")
text = f.read()
lexer = Lexer(text)
tokens=lexer.make_tokens()
f.close()
x = open('output.txt','w')
for i in tokens:
    x.write(str(i))
    x.write('\n')
x.close()