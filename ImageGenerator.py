# -*- coding: utf-8 -*-
"""
Módulo central que utiliza todo e qualquer método e chamada
"""
from AuxiliarModules.router import fonts
from AuxiliarModules.themes import getColor, getTheme
from PIL import Image, ImageDraw, ImageFont
import json
import uuid
from os import listdir, system, sys, path, mkdir
sys.path.append(path.abspath(path.dirname(__file__)))
# from themes. import getTheme, getColor
# from router import fonts



class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ImageObject():
    """Classe responsável por criar e lidar com imagens\n
    Não precisa receber argumentos na construção, pois todos já possuem valores `default`
    """

    def __init__(self, text: str = None, title: str = None, credits: str = None, theme: str = "sepia",
                 textFont: str = "ubuntu-bold", titleFont: str = "ubuntu-bold", creditsFont: str = "firacode-retina",
                 textFontSize: int = 48, titleFontSize: int = 40, creditsFontSize: int = 40, width: int = 1024,
                 height: int = 1024, paddingX: float = 0.05, paddingY: float = 0.1):
        # data
        # default name (precisa ser trocado em algum método)
        self.name = "exemplo"
        self.text = text
        self.title = title
        self.credits = title
        self.lines = None
        # fonts
        self.textFont = ImageFont.truetype(
            font=fonts[textFont], size=textFontSize)
        self.titleFont = ImageFont.truetype(
            font=fonts[titleFont], size=titleFontSize)
        self.creditsFont = ImageFont.truetype(
            font=fonts[creditsFont], size=creditsFontSize)
        # colors
        self.colorScheme = getTheme(theme)
        # "exemplo": {
        #         "background-color": "#E7CA70",
        #         "details": "#672008",
        #         "text": "#672008",
        #         "selection":"#672008"
        #     }
        self.selection = None
        # size
        self.width = width
        self.height = height
        self.paddingX = paddingX
        self.paddingY = paddingY
        self.px = int(self.paddingX*self.width)
        self.py = int(self.paddingY*self.height)
        self.maxTextWidth = self.width - 2*self.px
        self.maxTextHeight = self.height - 2*self.py
        self.charWidth = None
        self.charHeight = None
        # image
        self.image = None
        self.draw = None
        # booleans
        self.drawPaddingBox = False
        self.drawSelection = False
        self.debug = False

    # setters
    def setText(self, string: str = "default string with five words"):
        "Determina o texto principal da imagem."
        self.text = string
        if self.debug:
            print("Text definido como:", self.text)

    def setCredits(self, string: str = "default credits"):
        "Determina os créditos da imagem"
        self.credits = string
        if self.debug:
            print("Credits definido como:", self.credits)

    def setTitle(self, string: str = "default title"):
        "Determina o título da imagem"
        self.title = string
        if self.debug:
            print("Title definido como:", self.title)

    def setColorScheme(self, theme: str = "sepia"):
        """Define o esquema de cores da imagem\n
        `theme`: string com nome do tema a ser utilizado;\n
        Veja a documentação para saber quais temas estão disponíveis e veja como construir o seu próprio."""
        self.colorScheme = getTheme(theme)
        if self.debug:
            print("Theme definido como:", self.colorScheme)

    def setFontFamily(self, text: str = "ubuntu-bold", title: str = "ubuntu-bold",
                      credits: str = "firacode-retina", textFontSize: int = 48,
                      titleFontSize: int = 40, creditsFontSize: int = 40):
        """ Define as fontes utilizadas na imagem\n
        `text`: define o estilo da font a ser usada no texto;\n
        `title`: define o estilo da font a ser usada no título;\n
        `credits`: pdefine o estilo da font a ser usada nos créditos;
        """
        self.textFont = ImageFont.truetype(font=fonts[text], size=textFontSize)
        self.titleFont = ImageFont.truetype(
            font=fonts[title], size=titleFontSize)
        self.creditsFont = ImageFont.truetype(
            font=fonts[credits], size=creditsFontSize)

    def setTextFont(self, fontFamily: str = "ubuntu-bold", fontSize: int = 48):
        "Determina a fonte do texto principal da imagem."
        self.textFont = ImageFont.truetype(
            font=fonts[fontFamily], size=fontSize)

    def setCreditsFont(self, fontFamily: str = "firacode-retina", fontSize: int = 40):
        "Determina a fonte dos créditos da imagem."
        self.creditsFont = ImageFont.truetype(
            font=fonts[fontFamily], size=fontSize)

    def setTitleFont(self, fontFamily: str = "firacode-retina", fontSize: int = 40):
        "Determina a fonte do título da imagem."
        self.titleFont = ImageFont.truetype(
            font=fonts[fontFamily], size=fontSize)

    def setLines(self):
        "transforma o texto em `self.text` em linhas a serem desenhadas na imagem;"
        if not self.lines:
            self.formatString()
        self.lines = [line.strip() for line in self.lines]

    def setSize(self, width: int = 1024, height: int = 1024, paddingX: float = 0.05, paddingY: float = 0.1):
        """ Define os tamanhos da imagem\n
        `width`: largura da imagem;\n
        `height`: altura da imagem;\n
        `paddingX`: percentual da largura a ser ocupado pela margem;\n
        `paddingY`: percentual da altura a ser ocupado pela margem;
        """
        self.width = width
        self.height = height
        self.paddingX = paddingX
        self.paddingY = paddingY
        self.updateSelf()

    def setCharBox(self):
        self.charWidth = self.textFont.getsize("H")[0]
        self.charHeight = self.textFont.getsize("H")[1]

    def setDrawer(self):
        self.draw = ImageDraw.Draw(self.image)

    # Updates
    def updateSelf(self):
        self.px = int(self.paddingX*self.width)
        self.py = int(self.paddingY*self.height)
        self.maxTextWidth = self.width - 2*self.px
        self.maxTextHeight = self.height - 2*self.py

    def updateAfterShow(self):
        self.image = None
        self.draw = None
        self.lines = None
        if self.debug:
            print("[OK]\tImagem resetada")

    # métodos auxiliares

    def get_char_box(self, font: ImageFont.FreeTypeFont) -> tuple:
        """
        Com base no tamanho da fonte (que é do tipo `monospace`), 
        calcula a largura e altura em pixels de um caractere."""
        return font.getsize("H")

    def getMaxCharactersPerLine(self, font: ImageFont.FreeTypeFont,
                                max_width: int) -> int:
        """Com base nos parâmetros, estima a quantidade máxima de caracteres por linha."""
        if not font:
            font = self.textFont
        if not max_width:
            max_width = self.maxTextWidth
        if not self.charWidth:
            self.setCharBox()

        return int(max_width/self.charWidth)

    def findLastSpace(self, string: str, max_cpl: int) -> int:
        string = string.rstrip()

        if len(string) <= max_cpl:
            return len(string)

        string = string[:max_cpl][::-1]
        last_space = string.find(" ")

        return max_cpl - last_space

    def formatString(self) -> list:
        """
        faz as devidas manipulações na string para
        centralizar na imagem
        """
        string = self.text
        string = " ".join(string.splitlines())
        string = string.replace("  ", " ")

        max_cpl = self.getMaxCharactersPerLine(
            font=self.textFont, max_width=self.maxTextWidth)

        lines = []
        new_string = string

        while True:
            # verficar onde fica o espaço na string menor que
            last_space = self.findLastSpace(new_string, max_cpl)
            if last_space == 0:
                break
            line = new_string[:last_space].lstrip()
            lines.append(line)

            new_string = new_string[last_space:].lstrip()

        self.lines = lines

    def getLineShape(self, line: str, font: ImageFont):
        return font.getsize(line)

    def assertOutput(self, outputPath: str):
        if outputPath:
            if "output" not in listdir():
                system(r"mkdir output\%s" % outputPath)
            if outputPath not in listdir("output"):
                system(r"mkdir output\\%s" % outputPath)
            else:
                if self.debug:
                    print("Diretório de saída existe.")
                    print("output\%s\\" % outputPath)
            return r"output\%s\\" % outputPath
        else:
            if "output" not in listdir():
                system(r"mkdir output\SingleImages")
                if self.debug:
                    print("[DEBUG]  Output criado")
            if "SingleImages" not in listdir("output"):
                system(r"mkdir output\SingleImages")
                if self.debug:
                    print("[DEBUG]  SingleImages criado em /output/")
            return r"output\SingleImages\\"

    # métodos de ação
    def drawLine(self, p0, p1):
        p0 = Ponto(p0[0], p0[1])
        p1 = Ponto(p1[0], p1[1])
        shape = [(p0.x, p0.y), (p1.x, p1.y)]
        self.draw.line(shape, fill="red", width=2)

    def drawRect(self, p0: Ponto, p1: Ponto):
        shape = [(p0.x, p0.y), (p1.x, p1.y)]
        self.draw.rectangle(xy=shape, fill=getTheme("terminal-red")["background-color"],
                            outline=None)

    def drawPaddingLine(self):
        w = self.width
        h = self.height
        shape = [(self.px, self.py), (w-self.px, h-self.py)]
        self.draw.rectangle(xy=shape, fill=None,
                            outline=self.colorScheme["details"])

    def createImage(self):
        "Cria a imagem com altura, largura e cor de fundo"
        self.image = Image.new("RGBA", (self.width, self.height),
                               self.colorScheme["background-color"])
        if self.debug:
            print("""[DEBUG]  Imagem criada:\n\tmode=RGBA,\n\twidth: {width},\n\theight: {height},\n\tbackground-color: {backgroundColor}""".format(
                width=self.width, height=self.height, backgroundColor=self.colorScheme['background-color']))

    def putCredits(self):

        w, h = self.creditsFont.getsize(text=self.credits)

        x = self.width/2 - w/2
        y = self.height - h/2 - self.py/2
        self.draw.text((x, y),
                       self.credits, font=self.creditsFont, fill=self.colorScheme["text"])

    def putTitle(self):

        w, h = self.getLineShape(self.title, self.titleFont)

        x = self.width/2 - w/2
        y = self.py/2 - h/2
        self.draw.text((x, y),
                       self.title, font=self.titleFont, fill=self.colorScheme["text"])

    def putText(self):

        width, height = self.width, self.height

        nLines = len(self.lines)
        char_width, char_height = self.get_char_box(font=self.textFont)
        max_line_width = max([len(line) for line in self.lines])*char_width

        self.drawdraw = ImageDraw.Draw(self.image)

        x = int(self.width/2 - max_line_width/2)
        y = int(self.height/2 - nLines*char_height/2)
        for index, line in enumerate(self.lines):
            self.draw.text((x, y + char_height*index),
                           line, font=self.textFont, fill=self.colorScheme["text"])

    def process(self, show: bool = False, debug: bool = False):
        "Processa a imagem e torna ela visualizável"
        if debug:
            self.debug = True

        self.createImage()

        self.setLines()

        self.setDrawer()

        if self.drawPaddingBox:
            self.drawPaddingLine()

        if self.debug:
            self.drawLine((self.width/2, 0), (self.width/2,
                                              self.height))  # vertical central
            # horizontal cetral
            self.drawLine((0, self.height/2), (self.width, self.height/2))
            # horizontal margem superior
            self.drawLine((0, self.py/2), (self.width, self.py/2))
            self.drawLine((0, self.height - self.py/2), (self.width,
                                                         self.height - self.py/2))  # horizontal margem inferior

        self.putText()
        if self.credits:
            self.putCredits()
        if self.title:
            self.putTitle()
        if show:
            self.image.show()
        # self.updateAfterShow() # reseta as configurações da imagem para que possa ser reconfigurada e exibida novamente

    def save(self, path: str = None):
        self.image.save(self.assertOutput(path) + self.name + ".png")
