# -*- coding: utf-8 -*-

from json import loads, dumps

_themesPath = "assets/themes/themes.json"
_colorsPath = "assets/themes/colors.json"
print("themesPath:", _themesPath)

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
