import tensorflow as tf
import numpy as np

from tkinter import *
import os
from tkinter import filedialog
import cv2
import argparse, sys, os
import time
from matplotlib import pyplot as plt
from tkinter import messagebox


def endprogram():
    print("\nProgram terminated!")
    sys.exit()


def file_sucess():
    global file_success_screen
    file_success_screen = Toplevel(training_screen)
    file_success_screen.title("File Upload Success")
    file_success_screen.geometry("150x100")
    file_success_screen.configure(bg='pink')
    Label(file_success_screen, text="File Upload Success").pack()
    Button(file_success_screen, text='''ok''', font=(
        'Verdana', 15), height="2", width="30").pack()


global ttype


def training():
    global training_screen

    global clicked

    training_screen = Toplevel(main_screen)
    training_screen.title("Training")
    # login_screen.geometry("400x300")
    training_screen.geometry("600x450+650+150")
    training_screen.minsize(120, 1)
    training_screen.maxsize(1604, 881)
    training_screen.resizable(1, 1)
    training_screen.configure()
    # login_screen.title("New Toplevel")

    Label(training_screen, text='''Upload Image ''', background="#d9d9d9", disabledforeground="#a3a3a3",
          foreground="#000000", width="300", height="2", font=("Calibri", 16)).pack()
    Label(training_screen, text="").pack()

    options = [
        'Apple___Black_rot',
        'Apple___healthy',
        'Corn_(maize)___healthy',
        'Corn_(maize)___Northern_Leaf_Blight',
        'Peach___Bacterial_spot',
        'Peach___healthy',
        'Pepper_bell___Bacterial_spot',
        'Pepper_bell___healthy',
        'Potato___Early_blight',
        'Potato___healthy',
        'Potato___Late_blight',
        'Tomato___Bacterial_spot',
        'Tomato___Late_blight',
        'Tomato___Leaf_Mold',
        'Tomato___Septoria_leaf_spot'
    ]

    # datatype of menu text
    clicked = StringVar()

    # initial menu text
    clicked.set("select")

    # Create Dropdown menu
    drop = OptionMenu(training_screen, clicked, *options)
    drop.config(width="30")

    drop.pack()

    ttype = clicked.get()

    Button(training_screen, text='''Upload Image''', font=(
        'Verdana', 15), height="2", width="30", command=imgtraining).pack()


def vgg():
    import VggModel as vgg


def imgtraining():
    name1 = clicked.get()

    print(name1)

    import_file_path = filedialog.askopenfilename()
    import os
    s = import_file_path
    os.path.split(s)
    os.path.split(s)[1]
    splname = os.path.split(s)[1]

    image = cv2.imread(import_file_path)
    # filename = 'Test.jpg'
    filename = 'NewPlant/DataSet/' + name1 + '/' + splname

    cv2.imwrite(filename, image)
    print("After saving image:")

    fnm = os.path.basename(import_file_path)
    print(os.path.basename(import_file_path))

    # file_sucess()

    print("\n*********************\nImage : " + fnm + "\n*********************")
    img = cv2.imread(import_file_path)
    if img is None:
        print('no data')

    img1 = cv2.imread(import_file_path)
    print(img.shape)
    img = cv2.resize(img, ((int)(img.shape[1] / 5), (int)(img.shape[0] / 5)))
    original = img.copy()
    neworiginal = img.copy()
    cv2.imshow('original', img1)
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    img1S = cv2.resize(img1, (960, 540))

    cv2.imshow('Original image', img1S)

    dst = cv2.fastNlMeansDenoisingColored(img1, None, 10, 10, 7, 21)
    cv2.imshow("Nosie Removal", dst)


def imgtest():
    import_file_path = filedialog.askopenfilename()

    image = cv2.imread(import_file_path)
    print(import_file_path)
    filename = 'Out/Test.jpg'
    cv2.imwrite(filename, image)
    print("After saving image:")
    # result()

    # import_file_path = filedialog.askopenfilename()
    print(import_file_path)
    fnm = os.path.basename(import_file_path)
    print(os.path.basename(import_file_path))

    # file_sucess()

    print("\n*********************\nImage : " + fnm + "\n*********************")
    img = cv2.imread(import_file_path)
    if img is None:
        print('no data')

    img1 = cv2.imread(import_file_path)
    print(img.shape)
    img = cv2.resize(img, ((int)(img.shape[1] / 5), (int)(img.shape[0] / 5)))
    original = img.copy()
    neworiginal = img.copy()
    img1 = cv2.resize(img1, (540, 540))
    cv2.imshow('original', img1)
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    img1S = cv2.resize(img1, (540, 540))

    cv2.imshow('Original image', img1S)
    grayS = cv2.resize(gray, (540, 540))
    cv2.imshow('Gray image', grayS)

    dst = cv2.fastNlMeansDenoisingColored(img1, None, 10, 10, 7, 21)
    dst = cv2.resize(dst, (540, 540))
    cv2.imshow("Nosie Removal", dst)
    result()


def result():
    import warnings
    warnings.filterwarnings('ignore')

    import tensorflow as tf
    classifierLoad = tf.keras.models.load_model('Model/model.h5')

    import numpy as np
    from keras.preprocessing import image

    test_image = image.load_img('Out/Test.jpg', target_size=(100, 100))
    # img1 = cv2.imread('Output/Out/Test.jpg')
    # test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result1 = classifierLoad.predict(test_image)
    result = np.argmax(result1, axis=1)
    print(result)

    out = ''
    pre = ''
    if result[0] == 0:

        out = "Apple_Black_rot"
        pre = "You can reduce your risk by maintain irrigation of crops and making sure you use less than 2,300 mg of sodium a day"
    elif result[0] == 1:
        print("Apple_healthy")
        out = "Apple_healthy"
        pre =''
    elif result[0] == 2:
        print("Corn_(maize)___healthy")
        out = "Corn_(maize)___healthy"


    elif result[0] == 3:
        print("Corn_(maize)___Northern_Leaf_Blight")
        out = "Corn_(maize)___Northern_Leaf_Blight"
        pre = "azoxystrobin"

    elif result[0] == 4:
        print("Peach___Bacterial_spot")
        out = "Peach___Bacterial_spot"
        pre = "Use sprays containing organic copper compounds to treat D. citri. Initial application should take place at petal fall, followed by a secondary treatment 6-8 weeks later."

    elif result[0] == 5:
        print("Peach___healthy")
        out = "Peach___healthy"
        # pre = "Bacterial blight can be severe in susceptible rice varieties under high nitrogen fertilization"

    elif result[0] == 6:
        print("Pepper_bell___Bacterial_spot")
        out = "Pepper_bell___Bacterial_spot"
        pre = "Always consider an integrated approach with both preventive measures and biological treatments if available. The best way to prevent the disease is to use fungicides (e.g., iprodione, propiconazole, azoxystrobin, trifloxystrobin) as seed treatments."
    elif result[0] == 7:
        print("Pepper_bell___healthy")
        out = "Pepper_bell___healthy"
        pre = ""



    elif result[0] == 8:
        print("Potato___Early_blight")
        out = "Potato___Early_blight"
        pre = "Treat seeds with dilute bleach, hydrochloric acid, or hot water to reduce the potential for seedling infection"
    elif result[0] == 9:
        print("Potato___healthy")
        out = "Potato___healthy"
        pre = ""
    elif result[0] == 10:
        print("Potato___Late_blight")
        out = "Potato___Late_blight"
        pre = "You can reduce your risk by ensuring adequate water supply and making sure you use less than 2,300 mg of sodium a day"

    elif result[0] == 11:
        print("Tomato___Bacterial_spot")
        out = "Tomato___Bacterial_spot"
        pre = "Treat seeds with dilute bleach, hydrochloric acid, or hot water to reduce the potential for seedling infection"
    elif result[0] == 12:
        print("Tomato___Late_blight")
        out = "Tomato___Late_blight"
        pre = "Apply a fungicide according to the manufacturer’s instructions at the first sign of infection"
    elif result[0] == 13:
        print("Tomato___Leaf_Mold")
        out = "Tomato___Leaf_Mold"
        pre = "One of the least toxic and most effective is chlorothalonil (sold under the names Fungonil and Daconil)"
    elif result[0] == 14:
        print("Tomato___Septoria_leaf_spot")
        out = "Tomato___Septoria_leaf_spot"
        pre = "Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable"

    messagebox.showinfo("Result", "Prediction Result : " + str(out))

    messagebox.showinfo("Fertilizer Or Treatment ", "fertilizer  Or Treatment : " + str(pre))


def main_account_screen():
    global main_screen
    main_screen = Tk()
    width = 600
    height = 600
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main_screen.resizable(0, 0)
    # main_screen.geometry("300x250")
    main_screen.configure()
    main_screen.title(" Leaf Disease Prediction")

    Label(text="Leaf Disease Prediction", width="300", height="5", font=("Calibri", 16)).pack()

    Button(text="UploadImage", font=(
        'Verdana', 15), height="2", width="30", command=training, highlightcolor="black").pack(side=TOP)
    Label(text="").pack()
    Button(text="Training Vgg16Model", font=(
        'Verdana', 15), height="2", width="30", command=vgg, highlightcolor="black").pack(side=TOP)

    Label(text="").pack()
    Button(text="Prediction", font=(
        'Verdana', 15), height="2", width="30", command=imgtest, highlightcolor="black").pack(side=TOP)

    main_screen.mainloop()


main_account_screen()
