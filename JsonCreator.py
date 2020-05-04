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
newJson = {}
filename = "exemplo"


def prettyLine(line: str) -> str:
    line = line.strip()
    n = len(line) + 4
    layer = "*"*n + "\n"
    return layer + "* " + line + " *\n" + layer


def assertInputFolder():
    if "input" not in listdir():
        system("mkdir input")
    else:
        pass


def processInput(prompt: str) -> str:
    global done
    if not done:
        userInput = input(prompt + ": ")
        if userInput == "sair":
            done = True
            print(prettyLine("Atividade finalizada"))
            saveJson(filename=filename, data=newJson)
        else:
            return userInput


def saveJson(filename: str, data: dict):

    assertInputFolder()

    with open("input/%s.json" % filename, 'w+') as file:
        file.write(json.dumps(data))

    print("Arquivo salvo em: {0}".format(filename))


def createJson(thisFilename: str = "exemplo"):
    global newJson
    global filename
    filename = thisFilename
    # velho truque do contador
    counter = 1
    try:
        while not done:
            print(prettyLine("Digite sair a qualquer momento"))
            newJson["image{0}".format(counter)] = {
                "title": processInput("title"),
                "text": processInput("text"),
                "credits": processInput("credits")
            }
            counter += 1
    except:
        pass


if __name__ == "__main__":
    createJson()
