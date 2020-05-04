# -*- coding: utf-8 -*-
"""
Script de exemplo
"""
from os import sys, path, listdir, system
import json
# ==========
sys.path.append(path.abspath(path.dirname(__file__)))
# ==========

done = False
newTheme = {}


def prettyLine(line: str) -> str:
    line = line.strip()
    n = len(line) + 4
    layer = "*"*n + "\n"
    return layer + "* " + line + " *\n" + layer

def processInput(prompt: str, filename: str) -> str:
    global done
    if not done:
        userInput = input(prompt + ": ")
        if userInput == "sair":
            done = True
            print(prettyLine("Atividade finalizada"))
            saveTheme(filename=filename, data=newTheme)
        else:
            return userInput


def saveTheme(filename: str, data: dict):

    with open("input/%s.json" % filename, 'w+') as file:
        file.write(json.dumps(data))

    print("Arquivo salvo em: {0}".format(filename))


def createTheme(themeName: str = None):
    pass


if __name__ == "__main__":
    # call createTheme
    createTheme(themeName="example-theme")
