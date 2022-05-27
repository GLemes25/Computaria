--------------------------- PROJETO DE RUIDO EM UMA IMAGEM ---------------------------
#Participantes do projeto :
-Matheus Alexandre  RA 181441
-Leonel Solano RA 
-Thiago Olswezski RA 182687
-Gabriel Lemes RA 181502

#Explica��o do projeto: O projeto de adi��o de ruido, suaviza��o & borda, consiste em um programa com men� interativo por terminal, no qual, o usu�rio consegue inserir os dados e valores desejados para manipula��o da imagem que o mesmo especificou. Este programa surgiu com o intuito de mostrar os efeitos produzidos na imagem, quando nela s�o inseridos diferentes tipos de ruido, suaviza��o e at� mesmo detec��o de bordas dependendo das necesidades do usu�rio. Logo a seguir, ser� explicado como foi a realiza��o completa do projeto.

------------------------------- REALIZA��O DO PROJETO --------------------------------
O projeto se dividiu em 2 partes, menu + ruido(Matheus & Leonel) e suaviza��o + bordas(Thiago & Gabriel), todas as informa��es que encontramos sobre o tema foram retiradas do youtube(conceitos sobre ruido, suaviza��o e bordas; utiliza��o do opencv para processamento de imagens, plotagem de imagens em uma tela com matplotlib), stack overflow e livros da biblioteca virtual ucdb(python3; python: conceito e aplica��es).
Para a cria��o do projeto foram feitos varios testes em grupos separados, sendo eles o de menu e o de suaviza��o, todos eles tentando minimizar as linhas de c�digos usadas para que o c�digo/projeto fique mais simples para o entendimento do usu�rio. Ao finalizar o projeto, testes relacionados ao programa(realizados parte por parte dependendo de cada grupo(menu/suaviza��o)) foram feitos, testados e alterados atrav�s da plataforma github, alguns deles sendo: implementa��o de um menu gr�fico e interativo por janela; plotagem das imagens em janela junto de uma barra interativa, assim o usu�rio poderia manipular as imagens sem precisar inserir valor por valor; minimiza��o e refatora��o do c�digo.
Ap�s a realiza��o das partes do projeto(MENU / RUIDO / SUAVIZA��O / BORDAS), foi feito a montagem do programa principal, no qual algumas fun��es foram substitu�das por outras para uma melhor visualiza��o do projeto, algumas delas sendo: o modo como o usu�rio inseria a imagem & a presenta��o por janela do resultado de processamento da imagem.
Com isso, o projeto chegou a sua conclus�o final, sendo essa: um programa capaz de receber um caminho de diret�rio que pode ser alterado sem precisar fechar o mesmo; fazer a transforma��o da imagem por meio dos valores que o usu�rio insere(ruido, suaviza��o e borda); apresenta��o por janela da imagem original com sua transforma��o ao lado.

Link com funcionamento do programa: 
https://drive.google.com/drive/folders/1bIRWHx1K8o5hFrPz7ZFCkcgkYKnJ2H1v?usp=sharing

--------------------------------------------------------------------------------------
Bibliotecas utilizadas no programa

from contextlib import nullcontext     #parte da biblioteca desde a vers�o 2.5 fonte:
https://docs.python.org/3/library/contextlib.html
from email.mime import image
from sequence import Sequence
from turtle import end_fill
import cv2
import numpy as np
import random            #parte da biblioteca python, necess�rio apenas o comando import
import os                #parte da biblioteca python, necess�rio apenas o comando import
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
from skimage import io, color

--------------------------------------------------------------------------------------
Comandos para instala��o ap�s ativa��o do conda *conda activate vc
Para a instala��o das bibliotecas a seguir, ser� necess�rio abrir o prompt de comando e instalar todas as bibliotecas citadas abaixo de forma individual, com algumas delas ja estando presentes na biblioteca python como ja foi citado anteriormente.

pip install email.mime
pip instal Sequence
pip install turtle
pip install opencv-python
pip install numpy
pip install matplotlib
pip install pillow
pip install scikit-image