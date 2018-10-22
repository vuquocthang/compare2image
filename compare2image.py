# coding=utf-8

#from skimage.measure import structural_similarity as ssim
import random

import matplotlib.pyplot as plt
import numpy as np
import cv2
import requests
import datetime
from time import gmtime
import os

MAX = 1000000

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)

    return m
    #s = ssim(imageA, imageB)

def compare_images2(url_1, url_2):
    fn = filename_gen()
    img_name_1 = fn + "1.jpg"
    img_name_2 = fn + "2.jpg"

    with open( img_name_1 , 'wb') as f:
        f.write(requests.get(url_1).content)
    with open( img_name_2 , 'wb') as f:
        f.write(requests.get(url_2).content)

    img1 = cv2.imread(img_name_1)
    img2 = cv2.imread(img_name_2)

    checkKichThuoc = kiemTraKichThuoc(img1, img2)

    #nếu ảnh không cùng kích thước thì trả về giá trị MAX -> ảnh sai khác rất lớn
    if checkKichThuoc is False:
        #os.remove(img1)
        #os.remove(img2)
        return MAX


    #os.remove(img_name_1)
    #os.remove(img_name_2)
    return compare_images(checkKichThuoc[0], checkKichThuoc[1])

def filename_gen():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    passlen = 8
    p = "".join(random.sample(s, passlen))

    return p

def kiemTraKichThuoc(img1, img2):

    kichthuoc1 = img1.shape[:2]
    kichthuoc2 = img2.shape[:2]

    print(kichthuoc1)
    print(kichthuoc2)

    checkWidth = kichthuoc1[0]/kichthuoc2[0]
    checkHeight = kichthuoc1[1]/kichthuoc2[1]

    if( checkWidth != checkHeight):
        print("Ảnh không cùng tỉ lệ")
        return False

    if( checkWidth == checkHeight ):
        print("Ảnh cùng tỉ lệ")
        #nếu ảnh cùng kích thước
        if (kichthuoc1[0] == kichthuoc2[0]):
            r = []
            r.append(img1)
            r.append(img2)

            return r


        #nếu ảnh 1 nhỏ hơn ảnh 2 thì resize ảnh 2 bằng với size ảnh 1
        if(kichthuoc1[0] < kichthuoc2[0]):
            img2_new = cv2.resize(img2, (kichthuoc1[0], kichthuoc1[1]) )

            r = []
            r.append(img1)
            r.append(img2_new)

            return r
        #nếu ngược lại
        if(kichthuoc1[0] > kichthuoc2[0]):
            img1_new = cv2.resize(img1, (kichthuoc2[0], kichthuoc2[1]))

            r = []
            r.append(img1_new)
            r.append(img2)

            return r


