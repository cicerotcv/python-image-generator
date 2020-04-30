# -*- coding: utf-8 -*-
"""
Script de exemplo
"""
from ImageGenerator import ImageObject as Image


# Cria o objeto do tipo ImageObject rsrsrs
new_image = Image()

# diz ao programa que ele deve desenhar a linha que delimita a área de texto
new_image.drawPaddingBox = True

# define as dimensões da imagem
new_image.setSize(width=720, paddingX=0.1, paddingY=0.1)

# define o texto principal da imagem
new_image.setText("hello world message with six words")

# define as caracteristicas do titulo
new_image.setTitleFont("firacode-light", 50)
new_image.setTitle("Default Title")

# define as caracteristicas dos créditos
new_image.setCreditsFont("firacode-bold", 40)
new_image.setCredits("yourCustomCreditsHere")

# exibe a imagem em modo de desenvolvimento
new_image.show(debug=True)
