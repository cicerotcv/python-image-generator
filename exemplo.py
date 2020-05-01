# -*- coding: utf-8 -*-
"""
Script de exemplo
"""
from os import sys, path
# ==========
sys.path.append(path.abspath(path.dirname(__file__) ))
# ==========
from ImageGenerator import ImageObject as Image
from AuxiliarModules.router import outputPath

def main():
    # Cria o objeto do tipo ImageObject rsrsrs
    new_image = Image()

    # diz ao programa que ele deve desenhar a linha que delimita a área de texto
    new_image.drawPaddingBox = True

    # define as dimensões da imagem
    new_image.setSize(width=720, paddingX=0.1, paddingY=0.1)

    # define o texto principal da imagem
    new_image.setText("0-00-000-0000-000-00-0")
    # new_image.setText("hello world message with six words")

    # define as caracteristicas do titulo
    new_image.setTitleFont("firacode-light", 50)
    new_image.setTitle("00-000-00-00-000-00")

    # define as caracteristicas dos créditos
    new_image.setCreditsFont("firacode-bold", 50)
    new_image.setCredits("--yourCreditsHere--")

    # exibe a imagem em modo de desenvolvimento
    new_image.show(debug=True)
    
    # salva a imagem
    new_image.save(outputPath)
    


if __name__ == "__main__":
    main()
