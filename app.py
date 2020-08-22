#!/usr/bin/env python3
# coding: utf-8

import os
import cv2
import matplotlib.pyplot as plt

### IF Running from Colab. ###
#from google.colab import drive
#drive.mount('/content/drive')

#Location Check
d = os.getcwd()
print(d)

#for img in os.listdir("/content/train"):
#img = cv2.imread('./img/[FileName].png')

def img_process(filename):

    ### IF Running from Colab. ###
#    img = cv2.imread('/content/drive/My Drive/Colab Notebooks/img/[FileName].png')

    img = cv2.imread(filename)
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

    low_threshold = 0
    high_threshold = 100
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

    #plt.imshow(edges)
    return edges

def save_image():
    ### IF Running from Colab. ###
#    img_dir = '/content/drive/My Drive/Colab Notebooks/img/'
#    output_dir = '/content/drive/My Drive/Colab Notebooks/img_out/'

    ### IF Running locally. ###
    img_dir = './img/'

    files = os.listdir(img_dir)

    for f in files:
        filename = img_dir + f
        #print(filename)
        output = img_process(filename)

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        plt.imshow(output) #cmap='gray', vmin=0, vmax=255)
        print(os.getcwd()+'/img_out/'+f)
        result = cv2.imwrite(os.getcwd()+'/img_out/'+f, output)
        if result == True:
            print('File Saved')
        else:
            print('Saving Failed')

save_image()


# In[ ]:
