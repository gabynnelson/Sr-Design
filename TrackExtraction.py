"""
Name: TrackExtraction
Author: Kowe Kadoma
Purpose: To create the lines of best fit on the track
Date: Jan 16, 2021
Functional: not yet tested
Challenges: Knowing the dimensions to crop each video
"""
#Imports
import numpy as np
import cv2
import matplotlib.pyplot as plt



#Main Program
img = cv2.imread("lenna.png") #Loading the video


x,y,h,w=100 #Cropping frame of track video
"""
These are just dummy variables to hold the dimensions
how do we know the dimensions which are exact to focus on the track 
& what is the margin of error?
"""
img = img[y:y+h, x:x+w]

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converting to b&w
dst = cv2.equalizeHist(img) #Histogram equalization operation

img = cv2.GaussianBlur(img,(5,5),0) #Gaussian filter

img = cv2.threshold(img,cv2.THRESH_BINARY) #Converting to binary image

#Canny operator to extract edges

#Counting the number of markers

#Connecting using line of best fit
