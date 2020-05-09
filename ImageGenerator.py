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
        self.x = int(x)
        self.y = int(y)

class Texto:
    def __init__(self, text:[str,list], font:ImageFont.FreeTypeFont):
        "`text`: lista de parágrafos ou uma string com um único parágrafo;"
        if text is str:
            text = text.splitlines()
        self.textWidth, self.textHeight = font.getsize(text)

    def getLines(self, maxLineWidth:int):
        "`maxLineWidth`: pixels"
        pass

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

        self.textFontSize = textFontSize
        self.textFontFamily = textFont
        self.titleFontSize = titleFontSize
        self.titleFontFamily = titleFont
        self.creditsFontSize = creditsFontSize
        self.creditsFontFamily = creditsFont

        # colors
        self.colorScheme = getTheme(theme)
        # "exemplo": {
        #         "background-color": "#E7CA70",
        #         "details": "#672008",
        #         "text": "#672008",
        #         "selection":"#672008"
        #     }
        self.paddingLineColor = None
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
            print("[DEBUG] Text definido como:", self.text)

    def setCredits(self, string: str = "default credits"):
        "Determina os créditos da imagem"
        self.credits = string
        if self.debug:
            print("[DEBUG] Credits definido como:", self.credits)

    def setTitle(self, string: str = "default title"):
        "Determina o título da imagem"
        self.title = string
        if self.debug:
            print("[DEBUG] Title definido como:", self.title)

    def setColorScheme(self, theme: str = "sepia"):
        """Define o esquema de cores da imagem\n
        `theme`: string com nome do tema a ser utilizado;\n
        Veja a documentação para saber quais temas estão disponíveis e veja como construir o seu próprio."""
        self.colorScheme = getTheme(theme)
        if self.debug:
            print("[DEBUG] Theme definido como:", self.colorScheme)

    def setFontFamily(self, text: str = "ubuntu-bold", title: str = "ubuntu-bold",
                      credits: str = "firacode-retina", textFontSize: int = 48,
                      titleFontSize: int = 40, creditsFontSize: int = 40):
        """
        Define as fontes utilizadas na imagem\n
        `text`: define o estilo da font a ser usada no texto;\n
        `title`: define o estilo da font a ser usada no título;\n
        `credits`: pdefine o estilo da font a ser usada nos créditos;
        """
        self.textFont = ImageFont.truetype(font=fonts[text], size=textFontSize)
        self.titleFont = ImageFont.truetype(
            font=fonts[title], size=titleFontSize)
        self.creditsFont = ImageFont.truetype(
            font=fonts[credits], size=creditsFontSize)

    def setTextFont(self, fontFamily: str = None, fontSize: int = None):
        "Determina a fonte do texto principal da imagem."
        if fontFamily:
            self.textFontFamily = fontFamily
        if fontSize:
            self.textFontSize = fontSize
        self.textFont = ImageFont.truetype(
            font=fonts[self.textFontFamily], size=self.textFontSize)
        if self.debug:
            print(f"\tfonts[{self.textFontFamily}], size={self.textFontSize})")

    def setCreditsFont(self, fontFamily: str = "firacode-retina", fontSize: int = 40):
        "Determina a fonte dos créditos da imagem."
        self.creditsFont = ImageFont.truetype(
            font=fonts[fontFamily], size=fontSize)

    def setTitleFont(self, fontFamily: str = "firacode-retina", fontSize: int = 40):
        "Determina a fonte do título da imagem."
        self.titleFont = ImageFont.truetype(
            font=fonts[fontFamily], size=fontSize)

    def setLines(self):
        "Transforma o texto `self.text` em linhas a serem desenhadas na imagem;"
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

    def setPaddingBox(self, boolean: bool = True, color: str = "details"):
        self.drawPaddingBox = boolean
        self.paddingLineColor = self.getColor(thisColor=color)
        if self.debug:
            print(
                f"[DEBUG] padding line will be drawn: {boolean};\n\tcolor: {self.paddingLineColor}")

    # Updates
    def updateSelf(self):
        "Deve ser chamado após qualquer mudança 'manual' de dimensões;"
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
    def getColor(self, thisColor:[str,tuple]) -> str:
        """Pode ser:\n
        `details`, `selection`, `text`, `red`, `gray`, `#2020F3`, `(255,32,0)`..."""
        if thisColor:
            try:
                # podemos verificar se a cor inserida está no esquema de cores:
                if thisColor in self.colorScheme:
                    color = self.colorScheme[thisColor]
                else:
                    # ... se a cor não estiver no esquema de cores da imagem,
                    # devemos buscar no banco de cores;
                    color = getColor(thisColor)
            except:
                color = getColor("red")
                print(
                    "[ERROR] Falha ao encontrar cores. vermelho utilizado por default.")
        else:
            color = getColor("red")
            print(
                "[ERROR] Método getColor chamado sem informação de cor. Usando vermelho por default.")
        return color
            

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

        self.setCharBox()

        return int(max_width/self.charWidth)

    def findLastSpace(self, string: str, max_cpl: int) -> int:
        string = string.rstrip()

        if len(string) <= max_cpl:
            return len(string)

        string = string[:max_cpl][::-1]
        last_space = string.find(" ")

        return max_cpl - last_space

    def formatString(self):
        """
        faz as devidas manipulações na string para
        centralizar na imagem
        """
        string = self.text
        string = " ".join(string.split())
        # string = string.replace("  ", " ")

        max_cpl = self.getMaxCharactersPerLine(
            font=self.textFont, max_width=self.maxTextWidth)
        if self.debug:
            print(f"\tmax_cpl: {max_cpl}")
        lines = []

        new_string = string
        # aqui temos um pequeno dilema:
        # deveriamos ser capazes de pegar uma string e calcular 
        # o tamanho ideal de fonte, mas e se o usuário escolher 
        # o tamanho da fonte? E se o tamanho da fonte que ele 
        # escolher estourar os limites da página? Deveríamos 
        # intervir? Deveríamos escolher o tamanho da fonte 
        # automaticamnete para ele? O tamanho inteiro da string
        # pode ser calculado com self.getLineShape(line=string, font=self.textFont)
        width, height = self.getLineShape(string, font=self.textFont)
        while True:
            # verficar onde fica o espaço na string menor que
            last_space = self.findLastSpace(new_string, max_cpl)
            if last_space == 0:
                break
            line = new_string[:last_space].strip()
            lines.append(line)

            new_string = new_string[last_space:].lstrip()

        self.lines = lines
        
    def getLineShape(self, line: str, font: ImageFont):
        "Retorna `(width, height)` da string imputada em `line`;"
        return font.getsize(line)  # (width, height)

    def assertOutput(self, outputPath: str):
        "Método muito bagunçado. Arrumar depois e corrigir erros de compatibilidade com Linux"
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
    def drawLine(self, p0: tuple, p1: tuple, color="details"):
        thisColor = self.getColor(color)
        # if self.debug:
        #     print("[DEBUG] drawLine:")
        #     print(f"\tcolor: {color}")
        p0 = Ponto(p0[0], p0[1])
        p1 = Ponto(p1[0], p1[1])
        shape = [(p0.x, p0.y), (p1.x, p1.y)]
        self.draw.line(shape, fill=thisColor, width=2)

    def drawRect(self, p0: Ponto, p1: Ponto, fillColor = "details"):
        
        fillColor = self.getColor(fillColor)

        shape = [(p0.x, p0.y), (p1.x, p1.y)]
        if self.debug:
            print(f"[DEBUG] drawRect: (x0,y0):{(p0.x,p0.y)}; (x1,y1):{(p1.x,p1.y)}; color: {fillColor}")
        self.draw.rectangle(xy=shape, fill=self.getColor("details"),
                            outline=None)

    def drawPaddingLine(self):
        w = self.width
        h = self.height
        shape = [(self.px, self.py), (w-self.px, h-self.py)]
        self.draw.rectangle(xy=shape, fill=None, outline=self.getColor("details"), width=2)

    def createImage(self):
        "Cria a imagem com altura, largura e cor de fundo"
        self.image = Image.new("RGBA", (self.width, self.height),
                               self.colorScheme["background-color"])
        if self.debug:
            print(
                f"""[DEBUG] Imagem criada:\n\tmode=RGBA,\n\twidth: {
                    self.width},\n\theight: {
                        self.height},\n\tbackground-color: {
                            self.colorScheme['background-color']}""")

    def putCredits(self, color = None):
        if color:
            color = self.getColor(color)
        else:
            color = self.getColor("details")
        w, h = self.creditsFont.getsize(text=self.credits)

        x = self.width/2 - w/2
        y = self.height - h/2 - self.py/2

        if self.drawSelection:
            width, height = self.getLineShape(
                self.credits, font=self.creditsFont)
            self.drawRect(Ponto(x, y), Ponto(x+width, y+height), fillColor=color)
        self.draw.text((x, y),
                       self.credits, font=self.creditsFont, fill=self.colorScheme["text"])

    def putTitle(self):

        w, h = self.getLineShape(self.title, self.titleFont)

        x = self.width/2 - w/2
        y = self.py/2 - h/2

        if self.drawSelection:
            width, height = self.getLineShape(self.title, font=self.titleFont)
            self.drawRect(Ponto(x, y), Ponto(x+width, y+height),fillColor="details")

        self.draw.text((x, y),
                       self.title, font=self.titleFont, fill=self.colorScheme["text"])

    def putText(self):

        nLines = len(self.lines)
        char_width, char_height = self.get_char_box(font=self.textFont)

        maxLineHeight = max(
            [self.getLineShape(line, font=self.textFont)[1] for line in self.lines])
        maxLineWidth = max(
            [self.getLineShape(line, font=self.textFont)[0] for line in self.lines])

        totalTextHeight = maxLineHeight*nLines
        while not ((totalTextHeight < self.maxTextHeight) and (maxLineWidth < self.maxTextWidth)):
            # modificar self.formatString para que consiga calcular o tamanho
            # ideal de fonte para ajustar o texto;
            self.setTextFont(fontSize=self.textFontSize-1)
            self.formatString()
            maxLineHeight = max(
                [self.getLineShape(line, font=self.textFont)[1] for line in self.lines])
            maxLineWidth = max(
                [self.getLineShape(line, font=self.textFont)[0] for line in self.lines])
            totalTextHeight = maxLineHeight*nLines

            if self.debug:
                print("\n[DEBUG] putText: ajustando texto à imagem")
                print(f"\tself.textFontSize: {self.textFontSize}")
                print(f"\tlen(lines):{len(self.lines)}")
                print(f"\ttotalTextHeight: {totalTextHeight}")
                print(f"\tmaxTextHeight: {self.maxTextHeight}")
                print(f"\tmaxLineWidth: {maxLineWidth}")
                print(
                    f"\t(totalTextHeight < self.maxTextHeight): {(totalTextHeight < self.maxTextHeight)}")
                print(
                    f"\t(maxLineWidth < self.maxTextWidth): {(maxLineWidth < self.maxTextWidth)}")

            nLines = len(self.lines)

        x = int(self.width/2 - maxLineWidth/2)
        y = int(self.height/2 - nLines*maxLineHeight/2)

        for index, line in enumerate(self.lines):
            if self.drawSelection:
                width = self.getLineShape(line, font=self.textFont)[0]
                height = maxLineHeight
                self.drawRect(Ponto(x, y + maxLineHeight*index),
                              Ponto(x+width, y+height + maxLineHeight*index),fillColor="details")

            self.draw.text((x, y + maxLineHeight*index),
                           line, font=self.textFont, fill=self.colorScheme["text"])

    def process(self, show: bool = False, debug: bool = False):
        """Processa a imagem e torna ela visualizável;\n
        `show`: se True, exibe o programa ao final do processo;\n
        `debug`: se True, processa a imagem com modo Debug ativado, isto é, fica printando etapas e desenha linhas de referência;"""
        if debug:
            self.debug = True
        if self.drawSelection:
            self.colorScheme["selection"] = self.colorScheme["details"]
            self.colorScheme["text"] = self.colorScheme["secondary"]

        self.createImage()

        self.setLines()

        self.setDrawer()

        if self.drawPaddingBox:
            self.drawPaddingLine()

        if self.debug:
            # vertical central
            self.drawLine((self.width/2, 0), (self.width/2,
                                              self.height))
            # vertical esquerda - padding
            self.drawLine((self.px, 0), (self.px, self.height))
            # vertical direita - padding
            self.drawLine((self.width-self.px, 0),
                          (self.width - self.px, self.height))
            # horizontal central
            self.drawLine((0, self.height/2), (self.width, self.height/2))
            # horizontal superior - titulo
            self.drawLine((0, self.py/2), (self.width, self.py/2))
            # horizontal superior - padding
            self.drawLine((0, self.py), (self.width, self.py))
            # horizontal inferior - padding
            self.drawLine((0, self.height - self.py),
                          (self.width, self.height - self.py))
            # horizontal inferior - credits
            self.drawLine((0, self.height - self.py/2),
                          (self.width, self.height - self.py/2))

        self.putText()
        if self.title:
            self.putTitle()
        if self.credits:
            self.putCredits()
        if show:
            self.show()
        # self.updateAfterShow() # reseta as configurações da imagem para que possa ser reconfigurada e exibida novamente

    def save(self, path: str = None):
        self.image.save(self.assertOutput(path) + self.name + ".png")
    
    def show(self):
        "Exibe a imagem. É necessário que `process` tenha sido chamado antes."
        self.image.show()
