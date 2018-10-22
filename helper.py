import cv2
from cv2.cv2 import imread

image1 = imread("img1.jpg")
image2 = imread("img2.jpg")
image3 = image1 - image2

#print(image3)

cv2_mean = cv2.mean(image3)

print('open cv mean is:', cv2_mean)