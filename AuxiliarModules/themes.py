# -*- coding: utf-8 -*-
"""
Não funciona se rodar diretamente
"""
from AuxiliarModules.router import themesPath as _themesPath, colorsPath as _colorsPath
from json import loads, dumps
from os import listdir, system, sys, path
sys.path.append(path.abspath(path.dirname(__file__)))


with open(_themesPath, 'r') as themesFile:
    _themes = loads(themesFile.read())
with open(_colorsPath, 'r') as colorsFile:
    _colors = loads(colorsFile.read())


def getTheme(themeName: str) -> dict:
    return _themes[themeName]


def getColor(color: str) -> dict:
    if color is tuple:
        color = _tupleToString(color)
    if color[0] == "#":
        return color
    else:
        return _colors[color]


def _tupleToString(thisTuple: tuple) -> str:
    r = min([thisTuple[0], 255])
    g = min([thisTuple[1], 255])
    b = min([thisTuple[2], 255])
    r = hex(r)[2:]
    g = hex(g)[2:]
    b = hex(b)[2:]
    return "#" + "".join([r, g, b])


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
