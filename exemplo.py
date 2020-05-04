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

    string1 = "Seu aplicativo de e-mail consegue identificar spams. Seus aplicativos de músicas, filmes e notícias fazem recomendações para você. Seu aplicativo de fotos consegue reconhecer uma pessoa. O aplicativo em que você faz compras faz sugestões do que pode ser útil, baseando-se nas especificidades do seu perfil. Seu aplicativo de transporte indica para onde você provavelmente irá. Isso, é Machine learning."
    string2 = "Machine learning pode ser descrita como a possibilidade de um código fazer algo sem ser diretamente programado para isso. Esses algoritmos podem ser subdivididos em três principais categorias, sendo elas, supervised, unsupervised e semi-supervised. Na primeira, por meio de dados previamente catalogados, um determinado algoritmo consegue determinar padrões e gerar predições ou outputs. Um bom exemplo para esse tipo de algoritmo é seu aplicativo de e-mail. Quanto a segunda, um algoritmo consegue observar padrões em dados não catalogados e, a partir disso, cria outputs. Um exemplo seria o aplicativo em que você faz compras. Por fim, o último tipo é uma mistura dos dois anteriores, possui alguns dados previamente catalogados e alguns não catalogados. O melhor exemplo para ilustrar é seu aplicativo de fotos, em que o algoritmo consegue reconhecer uma pessoa, mas precisa de ajuda humana para nomeá-la."
    
    # define as caracteristicas do texto principal da imagem
    new_image.setText(string2)
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
