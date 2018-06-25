# Image-Transform
A short program to artificially increase dataset size. 

This code is not built for large datasets, but rather for anyone who wants to begin exploring Deep Learning and datasets in general. It is written in Python and uses modules cv2, numpy, random, and glob. The program reads in all the images in a folder, then randomly transform it 1 - 5 different ways: Rotate, Shift, Flip, Brightness, and Contrast. I wrote this program to be easily changed to increase the probablility of the image to be transformed. 

Currently built for Imagenet datasets but can easily be altered. All images should be quickly rechecked with a human eye to make sure transformation is not too much. 

### Prerequsits 
   - OpenCV
