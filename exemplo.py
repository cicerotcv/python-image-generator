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
    new_image.setColorScheme("black-white-red")

    # desenha as "seleção" do texto
    new_image.drawSelection = True

    string1 = """
Programa que gera imagens com base em textos. O texto obedece a um template que é definido na hora da criação;
O texto é centralizado e o programa adapta o tamanho da fonte caso exista tendência de extrapolar os limites;
Para conhecer os limites, pode-se ativar o 'modo debug', que já possui funções que ajudam na hora de encontrar erros.
A fonte se adapta mesmo que exista uma linha com um link bem grande:
https://github.com/cicerotcv/Image-Generator
    """*2
    # define as caracteristicas do texto principal da imagem
    new_image.setText(string1)
    new_image.setTextFont("firacode-retina", 45)

    # define as caracteristicas do titulo
    new_image.setTitleFont("ubuntu-regular", 40)
    new_image.setTitle(f"(debug_mode = {new_image.debug})")

    # define as caracteristicas dos créditos
    new_image.setCreditsFont("firacode-retina", 40)
    new_image.setCredits("@ImageGenerator")

    # exibe a imagem em modo de desenvolvimento
    new_image.process(show=True)

    # salva a imagem
    new_image.save()


if __name__ == "__main__":
    main()
