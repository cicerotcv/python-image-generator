# -*- coding: utf-8 -*-

from os import path


thisPath = path.abspath(path.dirname(__file__))
themesPath = path.join(thisPath, "../assets/themes/themes.json")
colorsPath = path.join(thisPath, "../assets/themes/colors.json")
fontsPath = path.join(thisPath, "../assets/fonts")
outputPath = path.join(thisPath, "../output")

fonts = {
    "ubuntu-regular": path.join(fontsPath, "UbuntuMono-Regular.ttf"),
    "ubuntu-bold": path.join(fontsPath, "UbuntuMono-Bold.ttf"),
    "firacode-light": path.join(fontsPath, "FiraCode-Light.ttf"),
    "firacode-medium": path.join(fontsPath, "FiraCode-Medium.ttf"),
    "firacode-regular": path.join(fontsPath, "FiraCode-Regular.ttf"),
    "firacode-bold": path.join(fontsPath, "FiraCode-Bold.ttf"),
    "firacode-retina": path.join(fontsPath, "FiraCode-Retina.ttf"),
    "handwritten1": path.join(fontsPath, "GloriaHallelujah-Regular.ttf"),
    "handwritten2": path.join(fontsPath, "IndieFlower-Regular.ttf"),
    "handwritten3": path.join(fontsPath, "MarckScript-Regular.ttf")
}


# debug purpose
# print("routerPath:",thisPath)
# print("themesPath:",themesPath)
# print("colorsPath:",colorsPath)
# print("fontsPath:",fontsPath)
