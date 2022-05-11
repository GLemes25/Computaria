# code for displaying multiple images in one figure

# import libraries
import cv2
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button


def mean():
    return cv2.blur(image2, (9, 9))


def gauss(a):
    image_gauss = cv2.GaussianBlur(image2, (9, 9), a)
    fig = plt.figure(figsize=(11, 6))

    axfreq = plt.axes([0.25, 0.1, 0.65, 0.03])
    freq_slider = Slider(
        ax=axfreq,
        label='Alpha',
        valmin=0.1,
        valmax=10,
        valinit=init_alpha,
    )

    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, 1)

    # showing image
    plt.imshow(image_original)
    plt.axis('off')
    plt.title("Original")

    # Adds a subplot at the 2nd position
    fig.add_subplot(rows, columns, 2)

    # showing image
    plt.imshow(image_gauss, cmap='gray')
    plt.axis('off')
    plt.title("Gauss")

    # The function to be called anytime a slider's value changes
    def update(val):
        image_gauss1 = cv2.GaussianBlur(image2, (9, 9), freq_slider.val)
        plt.imshow(image_gauss1, cmap='gray')
        plt.axis('off')
        plt.title("Gauss")

    # register the update function with each slider
    freq_slider.on_changed(update)
    plt.show()


def init_image():
    # Recebe a imagem e converte para HSV
    path = input('\nInforme o path da sua imagem a ser utilizada: ')
    raw_path = r'{}'.format(path)

    return raw_path


# setting values to rows and column variables
rows = 1
columns = 2
init_alpha = 0.3
op = 0

while op >= 0 and op <= 5:

    op = int(input('''
0 - Mean
1 - Gauss
2 - 
3 - 
4 -
5 - Alterar imagem

    '''))


    if op == 0:

        fig = plt.figure(figsize=(11, 6))
        # showing image
        fig.add_subplot(rows, columns, 1)
        plt.imshow(image_original)
        plt.axis('off')
        plt.title("Original")
        # Adds a subplot at the 2nd position
        fig.add_subplot(rows, columns, 2)
        # showing image
        plt.imshow(mean(), cmap='gray')
        plt.axis('off')
        plt.title("Mean")

        plt.show()

    elif op == 1:
        gauss(init_alpha)

    elif op == 5:
        image = cv2.imread(init_image())
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image_original = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)

        # Converte HSV para BGR e depois BGR para GRAY
        image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


print('Orbrigadão')
