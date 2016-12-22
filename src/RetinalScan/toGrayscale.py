#converting images to gray scale to identify vessels
# author sathvik koneru
import cv2
import os
import ctypes

#load pics from folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

#check one image
img = cv2.imread("im0001.ppm")
#test
cv2.imshow("eye", img)
cv2.waitKey()

#grayscale
gray_img = cv2.imread('im0001.ppm', cv2.IMREAD_GRAYSCALE)
#ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
#cv2.imshow('Grayscale', gray_img)
cv2.waitKey()


imgList = load_images_from_folder(RetinalScan)
cv2.imshow(RetinalScan[3])
cv2.waitKey()
