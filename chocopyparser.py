import chocopylexer as lex

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
            expected_lexemes += f', "{lexemas[lexeme]}"' if lexeme[:2] != 'kw' else f', "lexeme[3:]"'

        syntax_details = f'Se encontro: "{error_lexeme}"; se esperaba: {expected_lexemes}'
        super().__init__(details[0].position,'Error sintactico',syntax_details)

class Parser:

    def __init__(self,text):
        self.lexer = lex.Lexer(text)
        self.tokens = self.lexer.make_tokens()
        self.token_index = -1
        self.current_token = None

        self.next_token()

    def next_token(self):
        self.token_index +=1
        self.current_token = self.tokens[self.token_index] if self.token_index < len(self.tokens) else None

error = SyntaxError([lex.Token('kw_if',lex.Position(8,12,3)),['kw_if','tk_id',"NEWLINE"]])
print(error)
