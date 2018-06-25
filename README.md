# Image-Transform
A short program to artificially increase dataset size. 

This code is not built for large datasets, but rather for anyone who wants to begin exploring Deep Learning and datasets in general. It is written in Python and uses modules cv2, numpy, random, and glob. The program reads in all the images in a folder, then randomly transform it 1 - 5 different ways: Rotate, Shift, Flip, Brightness, and Contrast. I wrote this program to be easily changed to increase the probablility of the image to be transformed. 

Currently built for Imagenet datasets but can easily be altered. All images should be quickly re-checked with a human eye to make sure transformation is not too much. 

### Prerequsits 
   - OpenCV (https://opencv.org/)
   - Folder with dataset, preferably Imagenet (www.image-net.org/)
   
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

## Running

   1) Open Terminal
   
   2) Move to your folder dataset
   
   3) Excute python run
   
   ```
   python3 imageRead.py
   ```
   
## Altering the transformations

#### Probabity of the Transformation

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


