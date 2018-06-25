# Image-Transform
A short program to artificially increase dataset size. 

This code is not built for large datasets, but rather for anyone who wants to begin exploring Deep Learning and datasets in general. It is written in Python and uses modules cv2, numpy, random, and glob. The program reads in all the images in a folder, then randomly transform it 1 - 5 different ways: Rotate, Shift, Flip, Brightness, and Contrast. I wrote this program to be easily changed to increase the probablility of the image to be transformed. 

Currently built for Imagenet datasets but can easily be altered. All images should be quickly re-checked with a human eye to make sure transformation is not too much. 

### Prerequsits 
   - OpenCV (https://opencv.org/)
   - Folder with dataset, preferably Imagenet (www.image-net.org/)
   
### Installing

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

### Running

   1) Open Terminal
   
   2) Move to your folder dataset
   
   3) Excute python run
   
   ```
   python3 imageRead.py
   ```

