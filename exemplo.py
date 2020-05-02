# -*- coding: utf-8 -*-
"""
Script de exemplo
"""
from AuxiliarModules.router import outputPath
from ImageGenerator import ImageObject as Image
from os import sys, path
# ==========
sys.path.append(path.abspath(path.dirname(__file__)))
# ==========


def main():
    # Cria o objeto do tipo ImageObject rsrsrs
    new_image = Image()

    # diz ao programa que ele deve desenhar a linha que delimita a área de texto
    new_image.drawPaddingBox = True

    # ativa o modo debug
    # new_image.debug = True

    # define as dimensões da imagem
    new_image.setSize(width=int(1024*9/19), paddingX=0.1, paddingY=0.1)

    # define o esquema de cores da imagem
    new_image.setColorScheme("terminal-green")

    # define as caracteristicas do texto principal da imagem
    new_image.setText("Mensagem central com cinco palavras")
    new_image.setTextFont("handwritten")

    # define as caracteristicas do titulo
    new_image.setTitleFont("firacode-light", 30)
    new_image.setTitle("cabeçalho")

    # define as caracteristicas dos créditos
    new_image.setCreditsFont("firacode-bold", 30)
    new_image.setCredits("footer")

    # exibe a imagem em modo de desenvolvimento
    new_image.show()

    # salva a imagem
    # new_image.save()


if __name__ == "__main__":
    main()
