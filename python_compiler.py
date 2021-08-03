#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py_compile

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PYTHON Compiler")

print ( """

Welcome PYthon Compiler

""")

comp = str(input("Enter the name of the python file you want to compile: "))
py_compile.compile(comp)
print("process completed")
