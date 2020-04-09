#main program
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


def singlecharop(string,currentPos):
    token =''
    for index, char in enumerate(string,start=0):
        currentPos.advance(char)
        if char == '+':
            token= f'<tk_sum, {currentPos.line}, {currentPos.col}>'
            #currentPos.advance(char)
            break
        elif char == '%': 
            token=f'<tk_mod, {currentPos.line}, {currentPos.col}>'
            #currentPos.advance(char)
            break
        elif char == '(': 
            token=f'<tk_par_izq, {currentPos.line}, {currentPos.col}>'
            #currentPos.advance(char)
            break
        elif char == ')': 
            token=f'<tk_par_der, {currentPos.line}, {currentPos.col}>'
            #currentPos.advance(char)
            break
        elif char == '[': 
            token=f'<tk_llave_izq, {currentPos.line}, {currentPos.col}>'
            #currentPos.advance(char)
            break
        elif char == ']': 
            token=f'<tk_llave_der, {currentPos.line}, {currentPos.col}>'
            #currentPos.advance(char)
            break
        elif char == ',': 
            token=f'<tk_coma, {currentPos.line}, {currentPos.col}>'
            #currentPos.advance(char)
            break
        elif char == '.': 
            token=f'<tk_punto, {currentPos.line}, {currentPos.col}>'
            #currentPos.advance(char)
            break
        elif char == ':': 
            token=f'<tk_dospuntos, {currentPos.line}, {currentPos.col}>'
            #currentPos.advance(char)
            break
        elif char == '-':
            if string[index+1] == '>': 
                token=f'<tk_ejecuta, {pos.line}, {pos.col}>'
                currentPos.advance(char)
                break
            else:
                token =f'<tk_res, {pos.line}, {pos.col}>'
                break
        elif char == '<':
            if string[index+1] == '=': 
                token=f'<tk_menorig, {pos.line}, {pos.col}>'
                currentPos.advance(char)
                break
            else:
                token =f'<tk_menor, {pos.line}, {pos.col}>'
                break
        elif char == '>':
            if string[index+1] == '=': 
                token=f'<tk_mayorig, {pos.line}, {pos.col}>'
                currentPos.advance(char)
                break
            else:
                token =f'<tk_menor, {pos.line}, {pos.col}>'
                break
        elif char == '=':
            if string[index+1] == '=': 
                token=f'<tk_igual, {pos.line}, {pos.col}>'
                currentPos.advance(char)
                break
            else:
                token =f'<tk_asig, {pos.line}, {pos.col}>'
                break
    return token




f = open("test.txt","r")
text = f.read()

pos = Position(0,1,0)

while text[pos.index: ]:
    print(singlecharop(text[pos.index: ],pos))


