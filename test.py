#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:35:21 2017

@author: pabloibarra
"""
import sys

def saludo(nombre):
    frase = "Hola " + nombre + ",el mundo te saluda"
    print(frase)
    
    
 
if __name__ == "__main__":
    argv = sys.argv
    saludo(argv[1])
    