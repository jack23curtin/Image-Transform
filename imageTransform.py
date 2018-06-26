import numpy as np
# import opencv library
import cv2
import random
import glob


def main():
    iters = input('How many new, transformed photos per image would you like: ')
    iters = int(iters)
    i = 1
    while int(i) <= int(iters):
        for filename in glob.glob('*.JPEG'):
            print("Editting: " , filename)
            #reading the image
            img = cv2.imread(filename,1)
            rows,cols,ch = img.shape
            x = 1
            isset = 0

            #Transformations
            #Transformations

            #Rotate Image
            if random.sample(set([0, 1]), 1) == [0]:
                rotateChoice = [0,90,180,270]
                rotateDecide = (random.choice(rotateChoice))
                rotate = cv2.getRotationMatrix2D((cols/2,rows/2),rotateDecide,1)
                if isset == 1:
                    newImg = cv2.warpAffine(newImg,rotate,(cols,rows))
                else:
                    isset = 1
                    newImg = cv2.warpAffine(img,rotate,(cols,rows))
            #Shift Image
            if random.sample(set([0, 1]), 1) == [0]:
                #Horizontal Shift
                horizontalChoice = [-15,-5,0,5,15]
                horizontal = (random.choice(horizontalChoice))
                #Verticle Shift
                verticleChoice = [-15,-5,0,5,15]
                verticle = (random.choice(verticleChoice))
                shift = np.float32([[1,0,horizontal],[0,1,verticle]])
                if isset == 1:
                    newImg = cv2.warpAffine(newImg,shift,(cols,rows))
                else:
                    isset = 1
                    newImg = cv2.warpAffine(img,shift,(cols,rows))
            #Flip
            if random.sample(set([0, 1]), 1) == [0]:
                flipChoice = ["hor","ver","both"]
                x = (random.choice(flipChoice))
                #Flip Horizontal
                if x=="hor":
                    if isset == 1:
                        newImg = cv2.flip( newImg, 0 )
                    else:
                        isset = 1
                        newImg = cv2.flip( img, 0 )
                #Flip Verticle
                if x=="ver":
                    if isset == 1:
                        newImg = cv2.flip( newImg, 1 )
                    else:
                        isset = 1
                        newImg = cv2.flip( img, 1 )
                #Flip Both
                if x=="both":
                    if isset == 1:
                        newImg = cv2.flip( newImg, -1 )
                    else:
                        isset = 1
                        newImg = cv2.flip( img, -1 )
            #Brightness and Contrast
            if random.sample(set([0, 1]), 1) == [0]:
                #Contrast
                contrastChoice = [.2, .5, .7, 1, 1.3, 1.5, 1.7, 2]
                contrast = (random.choice(contrastChoice))
                #Brightness
                brightnessChoice = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50]
                brightness = (random.choice(brightnessChoice))
                if isset == 1:
                    newImg = cv2.addWeighted(newImg,contrast,np.zeros(img.shape,img.dtype), 0 , brightness)
                else:
                    isset = 1
                    newImg = cv2.addWeighted(img,contrast,np.zeros(img.shape,img.dtype), 0 , brightness)



            x = filename.split(".")
            if "_NEW" not in x[0]:
                newFile = x[0] + "_NEW-" + str(i) + ".JPEG"
            else:
                y = filename.split("-")
                newFile = y[0] + "-" + str(i) + ".JPEG"
            print("Saving new image: ", newFile)
            cv2.imwrite(newFile,newImg)
        i = int(i) + 1
main()
