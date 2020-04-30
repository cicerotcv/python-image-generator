# -*- coding: utf-8 -*-
"""
Módulo auxiliar;
não deve ser executado diretamente
"""
from PIL import Image, ImageFont, ImageDraw
from os import listdir, system
import json
import uuid


text_font = None
title_font = None
colorScheme = {"background-color": None,
               "details": None,
               "text": None}

# font = ImageFont.truetype("assets/fonts/FiraCode-Bold.ttf", 52)
W = 1024
H = 1024
px = 0.05*W
py = 0.1*H

fonts = {
    "ubuntu-regular": "assets/fonts/UbuntuMono-Bold.ttf",
    "ubuntu-bold": "assets/fonts/UbuntuMono-Bold.ttf",
    "firacode-light": "assets/fonts/FiraCode-Light.ttf",
    "firacode-medium": "assets/fonts/FiraCode-Medium.ttf",
    "firacode-regular": "assets/fonts/FiraCode-Regular.ttf",
    "firacode-bold": "assets/fonts/FiraCode-Bold.ttf",
    "firacode-retina": "assets/fonts/FiraCode-Retina.ttf",
    "handwritten": "assets/fonts/GloriaHallelujah-Regular.ttf",
}


def setColor(color: str) -> tuple:
    global colorScheme
    themes = {
        "terminal-green": {"background-color": (12, 12, 12),
                           "details": (32, 255, 0),
                           "text": (32, 255, 0)},
        "terminal-red": {"background-color": (12, 12, 12),
                           "details": (255, 32, 0),
                           "text": (255, 32, 0)},
        "sepia": {"background-color": (231, 202, 112),
                           "details": (103,32,8),
                           "text": (103,32,8)}
    }

    colorScheme = themes[color]


def setFont(fontSize: int = 52, fontFamily: str = "ubuntu-regular"):
    global text_font
    global title_font
    text_font = ImageFont.truetype(font=fonts[fontFamily], size=fontSize)
    title_font = text_font


def findLastSpace(string: str, max_cpl: int) -> int:
    string = string.rstrip()

    if len(string) <= max_cpl:
        return len(string)

    string = string[:max_cpl][::-1]
    last_space = string.find(" ")

    return max_cpl - last_space


def get_char_box(font: ImageFont.FreeTypeFont) -> tuple:
    "Com base no tamanho da fonte (que é do tipo `monospace`), calcula a largura e altura em pixels de um caractere."
    return font.getsize("H")


def getMaxCharactersPerLine(font: ImageFont.FreeTypeFont, max_width: int, max_height: int) -> int:
    "Com base nos parâmetros, estima a quantidade máxima de caracteres por linha."
    w, h = get_char_box(font)

    char_width = w
    line_height = h

    print("char box (w,h):", (w, h))

    return int(max_width/char_width)


def formatString(string: str) -> list:
    """
    faz as devidas manipulações na string para
    centralizar na imagem
    """
    string = " ".join(string.splitlines())
    string = string.replace("  ", " ")

    max_width = 1024 - 2*px
    max_height = 1024 - 2*py

    max_cpl = getMaxCharactersPerLine(font=text_font, max_width=max_width,
                                      max_height=max_height)
    print("max char/line:", max_cpl)

    lines = []
    new_string = string

    while True:
        # verficar onde fica o espaço na string menor que
        last_space = findLastSpace(new_string, max_cpl)
        if last_space == 0:
            # return lines
            break
        # print("last space:",last_space)
        line = new_string[:last_space].lstrip()
        print(line)
        lines.append(line)

        new_string = new_string[last_space:].lstrip()
    return lines


def putText(image: Image.Image, text: list) -> Image.Image:

    (width, height) = image.getbbox()[2], image.getbbox()[3]
    print("(width, height) =", (width, height))

    nLines = len(text)
    char_width, char_height = get_char_box(font=text_font)
    max_line_width = max([len(line) for line in text])*char_width
    print("max line width:", max_line_width)

    draw = ImageDraw.Draw(image)

    print("Lines:\n", text)

    for index, line in enumerate(text):
        draw.text((width/2 - max_line_width/2, height/2 - nLines*char_height/2 + char_height*index),
                  line, font=text_font, fill=colorScheme["text"])

    return image


def putCredits(image: Image.Image,  credits: str) -> Image.Image:
    font = ImageFont.truetype(fonts["firacode-retina"], 40)

    (width, height) = image.getbbox()[2], image.getbbox()[3]
    # print("(width, height) =",(width,height))

    nLines = 1
    char_width, char_height = get_char_box(font=font)

    w, h = font.getsize(text=credits)
    draw = ImageDraw.Draw(image)

    draw.text((width/2 - w/2, (2*height - py - char_height)/2),
              credits, font=font, fill=colorScheme["text"])

    return image


def putTitle(image: Image.Image,  title: str) -> Image.Image:
    font = ImageFont.truetype(fonts["firacode-retina"], 40)

    (width, height) = image.getbbox()[2], image.getbbox()[3]
    # print("(width, height) =",(width,height))

    nLines = 1
    char_width, char_height = get_char_box(font=font)

    w, h = font.getsize(text=title)
    draw = ImageDraw.Draw(image)

    draw.text((width/2 - w/2, py/2 - char_height/2),
              title, font=font, fill=colorScheme["text"])

    return image


def match(string1, string2):
    "verifica se todas as partes de uma string estão contidas na outra"
    truth = [(part in string2.lower()) for part in string1.lower().split()]
    return all(truth)


def get_filename(filename: str) -> str:

    return ["./input/" + fname for fname in listdir("./input") if match(string1=filename, string2=fname)][0]


def load_from_json(filename: str):
    """Veja a defenição dessa função (ainda é uma função enquanto escrevo isso) 
    para entender como deve ser a estrutura do json"""
    # json structure must match:
    # [{
    #     "title": not required,
    #     "text": string | required,
    #     "credits": string | not required
    # }]

    pass  # função a ser implementada


def load_from_txt(filename: str):
    with open(filename, 'r', encoding="utf8") as file:
        lines = file.readlines()
        if len(lines) == 1:
            lines = [lines]
    return [formatString(line) for line in lines]


def load_from_command_line(string: str) -> list:
    try:
        if len(string) > 300:
            print("string precisou ser reduzida")
            string = string[:300]
        return [formatString(string)]
    except:
        print(
            "Algum erro na leitura via CLI.\nVerifique a função [load_string_from_cli] no módulo functions")
        exit()


def load_from_file(filename: str) -> list:
    # try:
    filename = get_filename(filename=filename)
    if filename.endswith(".json"):
        return load_from_json(filename)
    if filename.endswith(".txt"):
        return load_from_txt(filename)
    # except:
    #     print("Arquivo [{}] não encontrado.\nVerifique e tente novamente.".format(filename))
    #     exit()


def exist(anything) -> bool:
    return anything == None


def loadTexts(string: str, filename: str) -> list:
    """
        retorna uma lista de listas;
        `string` é uma string inserida pela linha de comando;
        `filename` é um filename:str inserido pela linha de comando;
        string tem prioridade sobre o filename.
    """
    texts = []
    if string is not None:
        from_string = load_from_command_line(string=string)
        return from_string
    elif filename is not None:
        from_filename = load_from_file(filename=filename)
        return from_filename

    if not any([exist(string), exist(filename)]):
        print("""\nNenhum texto foi inserido pela linha de comando\nRevise o comando e tente novamente.""")
        exit()


def destination_folder(destination_folder_inside_output: str = None):
    """Garante que existe o caminho entre a pasta atual e a pasta de destino."""

    if destination_folder_inside_output:
        system("mkdir output\%s" % destination_folder_inside_output)
        return "output/%s" % destination_folder_inside_output
    else:
        if "single_images" not in listdir("output"):
            system("mkdir output\single_images")
        return "output/single_images/"


def random_filename(length: int = 8):
    """retorna a string aleatória do tamanho escolhido"""
    random = str(uuid.uuid4())  # Converte o formato do UUID em uma string.
    random = random.upper()
    random = random.replace("-", "")  # Remove os traços '-'.
    return random[0:length]


def generateImageName(texts_size: int):
    """Gera o nome da imagem dependendo do tipo de texto de entrada;
    `texts_size > 1` => imagens recebem o nome `image{}.png`;
    `texts_size = 1` => imagem recebe um nome aleatório de 8 caracteres; """
    return random_filename(7) + "{}.png" if texts_size == 1 else "image{}.png"


def drawPaddingLine(img):
    w = 1024
    h = 1024
    shape = [(px, py), (W-px, H-py)]
    draw = ImageDraw.Draw(img)
    draw.rectangle(xy=shape, fill=None, outline=colorScheme["details"])

    return img


def createImage(texts: list, destination_path: str, img_name: str, credits: str = None, title: str = None):
    """Usa os parâmetros acima para gerar a imagem com os textos e salvar\n no lugar certo"""
    for index, text in enumerate(texts):
        index += 1
        if index < 10:
            index = "0"+str(index)
        img = Image.new("RGBA", (1024, 1024), colorScheme["background-color"])

        img = putText(image=img, text=text)
        if credits:
            img = putCredits(img, credits)
        if title:
            img = putTitle(img, title)
        img = drawPaddingLine(img=img)
        img.save(destination_path + "/" + img_name.format(index))
        if len(texts) == 1:
            img.show()
