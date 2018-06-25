# Image-Transform
A short program to artificially increase dataset size. 

This code is not built for large datasets, but rather for anyone who wants to begin exploring Deep Learning and datasets in general. It is written in Python and uses modules cv2, numpy, random, and glob. The program reads in all the images in a folder, then randomly transform it 1 - 5 different ways: Rotate, Shift, Flip, Brightness, and Contrast. I wrote this program to be easily changed to increase the probablility of the image to be transformed. 

Currently built for Imagenet datasets but can easily be altered. All images should be quickly re-checked with a human eye to make sure transformation is not too much. 

### Prerequsits 
   - OpenCV (https://opencv.org/)
   - Folder with dataset, preferably Imagenet (www.image-net.org/)
   
  <br /> 
   
## Installing

Get my file

```
github git
```

Move my file into the folder with your dataset in it

```
move
```

Alter code so it works with yours

```
Give the example
```

<br />

## Running

   1) Open Terminal
   
   2) Move to your folder dataset
   
   3) Excute python run
   
   ```
   python3 imageRead.py
   ```
   
   <br />
   
## Altering the transformations


### Probabity of the Transformation
The probabity of the Transformation means how likely the Transformation will occur for each image

The transformations are currently set to occurr 50% probablitiy for each image
```
#Gives a 1/2 chance
if random.sample(set([0, 1]), 1) == [0]:
```

If you would like to decrease the probablility, you can add more 1s to the array:
```
#Gives a 1/3 chance
if random.sample(set([0, 1, 1]), 1) == [0]:
```

If you would like to increase the probablility, you can add more 0s to the array:
```
#Gives a 2/3 chance
if random.sample(set([0, 1, 0,]), 1) == [0]:
```

<br />

### Rotation Selection
Rotation Transformation means rotating the image about the center a set number of degrees

The rotation transformations are set to rotate the image by 0, 90, 180, or 270 degrees
```
rotateChoice = [0,90,180,270]
```

You can edit the array to add more or less rotational choices or edit them:
```
#Adds 45 degree options
rotateChoice = [0,45,90,135,180,225,270,315]
```

<br />


### Shift Selection
Shift Transformation means shifting the image horizontally or vertically a set number of pixels

NOTE: Shifting the image adds black area to the part of the image that was shifted. Do not add much to the shift choices because that will shift the object out of the frame.

The shift transformations are set to shift the image horizontally and vertically by -15, -5, 0, 5, or 15 pixels
```
horizontalChoice = [-15,-5,0,5,15]
verticleChoice = [-15,-5,0,5,15]
```

You can edit the array to add more or less shift choices or edit them:
```
#Limits shift to 10 pixels
horizontalChoice = [-10,0,10]
verticleChoice = [-10,0,10]
```

<br />
