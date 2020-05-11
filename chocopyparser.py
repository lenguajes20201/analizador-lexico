import chocopylexer as lex
import test2

lexemas = {
    "tk_sum":"+",
    "tk_res":"-",
    "tk_mul":"*",
    "tk_div":"//",
    "tk_mod":"%",
    "tk_menor":"<",
    "tk_mayor":">",
    "tk_mayoring":"<=",
    "tk_mayorig":">=",
    "tk_igual":"==",
    "tk_diferente":"!=",
    "tk_asig":"=",
    "tk_par_izq":"(",
    "tk_par_der":")",
    "tk_llave_izq":"[",
    "tk_llave_der":"]",
    "tk_coma":",",
    "tk_dospuntos":":",
    "tk_punto":".",
    "tk_ejecuta":"->",
    "tk_cadena":"",
    "tk_id":"id",
    "NEWLINE":'salto de linea',
    "INDENT":'indentacion',
    "DEDENT":'indentacion'
}


class SyntaxError(lex.Error):
    def __init__(self,details):
        error_lexeme = lexemas[details[0].type] if details[0].type[:2] != 'kw' else details[0].type[3:]
        expected_lexemes = f'"{lexemas[details[1][0]]}"' if details[1][0][:2] != 'kw' else f'"{details[1][0][3:]}"'
        for lexeme in details[1][1:]:
            expected_lexemes += f', "{lexemas[lexeme]}"' if lexeme[:2] != 'kw' else f', "{lexeme[3:]}"'

        syntax_details = f'Se encontro: "{error_lexeme}"; se esperaba: {expected_lexemes}'
        super().__init__(details[0].position,'Error sintactico',syntax_details)

class Parser:

    def __init__(self,text):
        self.lexer = lex.Lexer(text)
        self.tokens = self.lexer.make_tokens()
        self.token_index = -1
        self.current_token = None
        self.prediction = test2.PREDICCION()

        self.next_token()

    def next_token(self):
        self.token_index +=1
        self.current_token = self.tokens[self.token_index] if self.token_index < len(self.tokens) else None


    ## gramatica 
    def emparejar (self, token_esperado):
        token = self.current_token
        if token.type == token_esperado :
            self.next_token()
        else:
            a = []
            a.append(token)
            a.append([token_esperado])
            print (SyntaxError(a))

    def nt_var_def(self) :
        token1 = self.current_token
        token=token1.type
        if (token in self.prediction['nt_var_def']['nt_typed_var tk_asig nt_literal NEWLINE']):
            self.nt_typed_var()
            self.emparejar ('tk_asig')
            self.nt_literal()
            self.emparejar ('NEWLINE')
        else:
            a = []
            a.append(token1)
            a.append(list(self.prediction['nt_var_def']['nt_typed_var tk_asig nt_literal NEWLINE']))
            print (SyntaxError(a))

    def nt_typed_var(self) :
        token = self.current_token
        if (token in self.prediction['nt_typed_var']['tk_id tk_dospuntos nt_type']):
            self.emparejar ('tk_id')
            self.emparejar ('tk_dospuntos')
            self.nt_type()
        else:
            a = []
            a.append(token)
            a.append(list(self.prediction['nt_typed_var']['tk_id tk_dospuntos nt_type']))
            print (SyntaxError(a))

    def nt_literal(self) :
        token1 = self.current_token
        token=token1.type
        if (token in self.prediction['nt_literal']['kw_None']):
            self.emparejar ('kw_None')
        elif (token in self.prediction['nt_literal']['kw_True']):
            self.emparejar ('kw_True')
        elif (token in self.prediction['nt_literal']['kw_False']):
            self.emparejar ('kw_False')
        elif (token in self.prediction['nt_literal']['tk_entero']):
            self.emparejar ('tk_entero')
        elif (token in self.prediction['nt_literal']['tk_id']):
            self.emparejar ('tk_id')
        elif (token in self.prediction['nt_literal']['tk_cadena']):
            self.emparejar ('tk_cadena')
        else:
            B = self.prediction['nt_literal']['kw_None'] | self.prediction['nt_literal']['kw_True'] | self.prediction['nt_literal']['kw_False'] | self.prediction['nt_literal']['tk_entero'] | self.prediction['nt_literal']['tk_id'] | self.prediction['nt_literal']['tk_cadena']
            a = []
            a.append(token1)
            a.append(list(B))
            print (SyntaxError(a))


    def nt_type(self) :
        token1 = self.current_token
        token=token1.type
        if (token in self.prediction['nt_type']['tk_id']):
            self.emparejar ('tk_id')
        elif (token in self.prediction['nt_type']['tk_idstring']):
            self.emparejar ('tk_idstring')
        elif (token in self.prediction['nt_type']['tk_llave_izq nt_type tk_llave_der']):
            self.emparejar ('tk_llave_izq')
            self.nt_type()
            self.emparejar ('tk_llave_der')
        else:
            B = self.prediction['nt_type']['tk_id'] | self.prediction['nt_type']['tk_idstring'] | self.prediction['nt_type']['tk_llave_izq nt_type tk_llave_der']
            a = []
            a.append(token1)
            a.append(list(B))
            print (SyntaxError(a))






parser = Parser('a:int = 10000')
print(parser.tokens)

parser.nt_var_def()
if(parser.current_token != None ):
    print ('Error')
else: 
    print('exito')

