#!/usr/bin/env python

stack = []
loop = 0

def lexer(line):

    raw_tokens = line.split(' ')
    i = 0

    tokens = []

    for token in raw_tokens:
        token = token.upper()
        if not token == ' ':
            try:
                token = int(token)

            except:
                try:
                    token = float(token)

                except: pass

            tokens.append(token)
        

    return tokens

def parser(tokens):
    global stack

    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token == "CLEAR":
            stack.clear()

        elif token == "PUSH":
            i += 1
            value = tokens[i]
            if type(value) == type(" "):
                value = parsestring(tokens[i])
            stack.append(value)

        elif token == "PEEK":
            try : print(stack[-1], end = '')
            except : print("NIL", end = '')

        elif token == "POP":
            try : print(stack.pop(), end = '')
            except : print("NIL", end = '')
        
        elif token == "ADD":
            stack.append(sum(stack))

        elif token == "PRINT":
            i += 1 
            string = parsestring(tokens[i])
            
            print(string, end = '')

        elif token == "INPUT":
            stack.append(input())

        elif token == "PARSE":
            stack = parsestack()

        elif token == "IF":
            j = i
            while tokens[j] != "FI":
                j += 1
            if_block = tokens[i + 1:j]
            if stack[-1] != 0:
                parser(if_block)
            return 2

        elif token == "LOOP":
            j = i
            while tokens[j] != "POOL":
                j += 1
            loop_block = tokens[i + 1:j]
            while stack[-1] != 0:
                parser(loop_block)

            return 2

        elif token == "ADDWITH":
            stack[-1] = stack[-1] + tokens[i + 1]
            i += 1

        elif token == "EVAL":
            stack.append(eval(parsestring(stack[-1])))

        elif token == "END":
            return 0

        i += 1
    

    return 2

def parsestring(string):
    string = string.replace("__", " ")
    string = string.replace("_N", "\n")
    string = string.replace("_T", "\t")
    try:
        if string[:2] == '_L':
            string = string[2:].lower()
        elif string[:2] == '_U':
            string = string[2:].upper()
    except : pass
    return string
def parsestack():
    parsed = []
    for elm in stack:
        try:
            elm = int(elm)
        except:
            try:
                elm = float(elm)
            except: pass
        
        parsed.append(elm)

    return parsed

if __name__ == "__main__":

    import sys

    rcode = 2
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line[:len(line) - 1]
            tokens = lexer(line) 
            rcode = parser(tokens)

           

            if rcode != 2:
                break

    else:
        while rcode == 2:
            line = input(">> ")
            tokens = lexer(line)
            rcode = parser(tokens)
            print(stack)
