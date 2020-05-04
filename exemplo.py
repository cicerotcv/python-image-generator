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
    # new_image.drawPaddingBox = True

    # ativa o modo debug
    new_image.debug = True

    # define as dimensões da imagem
    # new_image.setSize(width=int(1024*9/19), paddingX=0.1, paddingY=0.1)

    # define o esquema de cores da imagem
    # new_image.setColorScheme("insper-talus")

    string1 = "exemplo de texto com seis palavras"
    # define as caracteristicas do texto principal da imagem
    new_image.setText(string1)
    new_image.setTextFont("ubuntu-bold",45)

    # define as caracteristicas do titulo
    new_image.setTitleFont("ubuntu-regular", 30)
    new_image.setTitle("Machine Learning (1/2)")

    # define as caracteristicas dos créditos
    new_image.setCreditsFont("ubuntu-regular", 30)
    new_image.setCredits("@talus_insper")

    # exibe a imagem em modo de desenvolvimento
    new_image.process(show=True)

    # salva a imagem
    new_image.save()


if __name__ == "__main__":
    main()
