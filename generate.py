# -*- coding: utf-8 -*-
import random
from PIL import Image, ImageFont, ImageDraw
import argparse
import time
import functions as aux
from os import system, listdir, mkdir
"""
    origem (140,160)
    end (884,864)
    largura de texto: 744px
    altura de texto:  704px
    max caracteres: 480
"""

parser = argparse.ArgumentParser()
parser.add_argument(
    "-t",
    "--text",
    type=str,
    help="text",
    required=False,
    default=None
)
parser.add_argument(
    "-f",
    "--filename",
    type=str,
    help="file containing strings",
    required=False,
    default=None
)
parser.add_argument(
    "-fs",
    "--fontsize",
    type=int,
    help="fontsize",
    required=False,
    default=48
)
parser.add_argument(
    "-c",
    "--credits",
    type=str,
    help="credits to be printed on the footer",
    required=False,
    default=None
)
parser.add_argument(
    "-tt",
    "--title",
    type=str,
    help="title to be printed on the header",
    required=False,
    default=None
)
parser.add_argument(
    "-cs",
    "--colorScheme",
    type=str,
    help="cor dos elementos",
    required=False,
    default="red"
)
parser.add_argument(
    "-ff",
    "--fontFamily",
    type=str,
    help="tipo de fonte",
    required=False,
    default="ubuntu-regular"
)

args = parser.parse_args()

title = args.title
string = args.text
credits = args.credits
filename = args.filename
fontSize = args.fontsize
fontFamily = args.fontFamily
colorScheme = args.colorScheme

if __name__ == "__main__":
    # define as caracteristicas da fonte;
    aux.setFont(fontFamily=fontFamily, fontSize=fontSize)

    # define o esquema de cores da imagem;
    aux.setColor(color=colorScheme)  # default: red

    # carrega um texto a partir dos comandos da CLI;
    texts = aux.loadTexts(string=string, filename=filename)

    # gera um nome para a imagem de saída;
    img_name = aux.generateImageName(texts_size=len(texts))

    # garante que existe pasta de saída;
    destination_path = aux.destination_folder(filename)

    # lida com os parametros acima e gera a(s) imagem(ns);
    aux.createImage(texts=texts, destination_path=destination_path,
                    img_name=img_name, credits=credits, title=title)
