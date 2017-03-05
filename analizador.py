# -*- coding: utf-8 -*-
import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST','VAR','PROEDURE','OUT','IN','ELSE']

tokens = reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE','ODD','ASSING','NE','LT','LTE','GT','GTE','LPARENT','RPARENT','COMMA','SEMMICOLOM','DOT','UPDATE']

t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE =r'/'
t_ASSING = r'='
t_ODD = r'ODD'
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in keywords:
        tvalue = tvalue.upper()
        t.type = t.value

        return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ccode_nonspace(t):
    r'\s+'
    pass

def t_COMMENT(t):
    r'\#.*'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print "caracter ilegal '%s'" %t.value[0]
    t.lexer.sikip(1)

def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
        
    for file in files:
        print str(cont)+", "+file
        cont =cont+1

    while respuesta == False:
        numArchivo = raw_input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break
    print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]

    return files[int(numArchivo)-1]

directorio = '/Users/Abraham/Documents/Primavera2017/Introducción a los compiladores/AL/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test, "r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok : break
    print tok
