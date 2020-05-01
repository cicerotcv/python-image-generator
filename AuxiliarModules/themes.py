# -*- coding: utf-8 -*-
"""
Não funciona se rodar diretamente
"""
from os import listdir, system, sys, path
sys.path.append(path.abspath(path.dirname(__file__) ))
from json import loads, dumps
from AuxiliarModules.router import themesPath as _themesPath, colorsPath as _colorsPath


with open(_themesPath, 'r') as themesFile:
    _themes = loads(themesFile.read())
with open(_colorsPath, 'r') as colorsFile:
    _colors = loads(colorsFile.read())

def getTheme(themeName: str) -> dict:
    return _themes[themeName]

def getColor(colorName:str) -> dict:
    return _colors[colorName]

def createTheme(themeName: str, backgroundColor: tuple, textColor: tuple, detailsColor: tuple):
    def rgb_to_hex(rgb: tuple) -> str:
        return "#"+"".join(hex(spectre)[2:] for spectre in rgb)

    localThemes = _themes
    localThemes[themeName] = {
        "background-color": rgb_to_hex(backgroundColor),
        "details": rgb_to_hex(detailsColor),
        "text": rgb_to_hex(textColor)
    }
    with open(_themesPath, "w") as themesFile:
        print(dumps(localThemes))
