--------------------------- PROJETO DE RUIDO EM UMA IMAGEM ---------------------------
#Participantes do projeto :
-Matheus Alexandre  RA 181441
-Leonel Solano RA 
-Thiago Olswezski RA 182687
-Gabriel Lemes RA 181502

#Explicação do projeto: O projeto de adição de ruido, suavização & borda, consiste em um programa com menú interativo por terminal, no qual, o usuário consegue inserir os dados e valores desejados para manipulação da imagem que o mesmo especificou. Este programa surgiu com o intuito de mostrar os efeitos produzidos na imagem, quando nela são inseridos diferentes tipos de ruido, suavização e até mesmo detecção de bordas dependendo das necesidades do usuário. Logo a seguir, será explicado como foi a realização completa do projeto.

------------------------------- REALIZAÇÃO DO PROJETO --------------------------------
O projeto se dividiu em 2 partes, menu + ruido(Matheus & Leonel) e suavização + bordas(Thiago & Gabriel), todas as informações que encontramos sobre o tema foram retiradas do youtube(conceitos sobre ruido, suavização e bordas; utilização do opencv para processamento de imagens, plotagem de imagens em uma tela com matplotlib), stack overflow e livros da biblioteca virtual ucdb(python3; python: conceito e aplicações).
Para a criação do projeto foram feitos varios testes em grupos separados, sendo eles o de menu e o de suavização, todos eles tentando minimizar as linhas de códigos usadas para que o código/projeto fique mais simples para o entendimento do usuário. Ao finalizar o projeto, testes relacionados ao programa(realizados parte por parte dependendo de cada grupo(menu/suavização)) foram feitos, testados e alterados através da plataforma github, alguns deles sendo: implementação de um menu gráfico e interativo por janela; plotagem das imagens em janela junto de uma barra interativa, assim o usuário poderia manipular as imagens sem precisar inserir valor por valor; minimização e refatoração do código.
Após a realização das partes do projeto(MENU / RUIDO / SUAVIZAÇÃO / BORDAS), foi feito a montagem do programa principal, no qual algumas funções foram substituídas por outras para uma melhor visualização do projeto, algumas delas sendo: o modo como o usuário inseria a imagem & a presentação por janela do resultado de processamento da imagem.
Com isso, o projeto chegou a sua conclusão final, sendo essa: um programa capaz de receber um caminho de diretório que pode ser alterado sem precisar fechar o mesmo; fazer a transformação da imagem por meio dos valores que o usuário insere(ruido, suavização e borda); apresentação por janela da imagem original com sua transformação ao lado.

Link com funcionamento do programa: 
https://drive.google.com/drive/folders/1bIRWHx1K8o5hFrPz7ZFCkcgkYKnJ2H1v?usp=sharing

--------------------------------------------------------------------------------------
Bibliotecas utilizadas no programa

from contextlib import nullcontext     #parte da biblioteca desde a versão 2.5 fonte:
https://docs.python.org/3/library/contextlib.html
from email.mime import image
from sequence import Sequence
from turtle import end_fill
import cv2
import numpy as np
import random            #parte da biblioteca python, necessário apenas o comando import
import os                #parte da biblioteca python, necessário apenas o comando import
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
from skimage import io, color

--------------------------------------------------------------------------------------
Comandos para instalação após ativação do conda *conda activate vc
Para a instalação das bibliotecas a seguir, será necessário abrir o prompt de comando e instalar todas as bibliotecas citadas abaixo de forma individual, com algumas delas ja estando presentes na biblioteca python como ja foi citado anteriormente.

pip install email.mime
pip instal Sequence
pip install turtle
pip install opencv-python
pip install numpy
pip install matplotlib
pip install pillow
pip install scikit-image