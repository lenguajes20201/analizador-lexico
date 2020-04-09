# Guarda el indice, linea y columna del caracter
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
            self.col = 0

        return self

    def copy(self):
        return Position(self.index,self.line,self.col)


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __str__(self):
        if self.value:
            return f'{self.type}, {self.value}'
        return f'{self.type}'

f = open("test.txt","r")
text = f.read()
pos = Position(0,1,1)
for char in text:
    if char == '\n': print(f'>\\n<',pos)
    elif char == '+': print(f'<tk_sum, {pos.line}, {pos.col}>')
    elif char == '%': print(f'<tk_mod, {pos.line}, {pos.col}>')
    elif char == '(': print(f'<tk_par_izq, {pos.line}, {pos.col}>')
    elif char == ')': print(f'<tk_par_der, {pos.line}, {pos.col}>')
    elif char == '[': print(f'<tk_llave_izq, {pos.line}, {pos.col}>')
    elif char == ']': print(f'<tk_llave_der, {pos.line}, {pos.col}>')
    elif char == ',': print(f'<tk_coma, {pos.line}, {pos.col}>')
    elif char == '.': print(f'<tk_punto, {pos.line}, {pos.col}>')
    elif char == ':': print(f'<tk_dospuntos, {pos.line}, {pos.col}>')
    else: print(f'>{char}<',pos)
    pos.advance(char)