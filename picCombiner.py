# Link to github: https://github.com/eSchwander/CST-205_Project1

import os
import time
import types

#These first two functions are used for a merge sort which i actually never use
#As it turns out the built in sort python has is faster

def myMergeSort(myList):
  length = len(myList)
  if length == 1:
    return myList[0]
  x = myList[0:length // 2]
  y = myList[length // 2 : length]
  return myMerge(myMergeSort(x),myMergeSort(y))
  
def myMerge(xList, yList):
  x = []
  y = []
  if isinstance(xList, list):
    x.extend(xList)
  else:
    x.append(xList)
  if isinstance(yList, list):
    y.extend(yList)
  else:
    y.append(yList)
  mergeList = []
  xCount = 0
  yCount = 0
  end = len(x) + len(y)
  for _ in range(0,end):
    if xCount < len(x):
      if yCount < len(y):
        if y[yCount] < x[xCount]:
          mergeList.append(y[yCount])
          yCount+=1
        else:
          mergeList.append(x[xCount])
          xCount+=1
      else:
        mergeList.extend(x[xCount:])
        break
    else:
      mergeList.extend(y[yCount:])
      break
  return mergeList

  
  
#startTime = time.time() # this is used to measure run time 
pics = [] # holds all the pictures in a folder
pix = [] # Holds pixels for all pictures in pix

path = "C:\\cygwin64\\home\\CSUMB\\CST205\\Project1\\pictures\\"

#the following loop adds all pictures in given path into the pics list
flag = True
for file in os.listdir(path):
  if file.endswith('.png'):
    pics.append(makePicture(path + file))
    if flag:
      flag = False
      finalPic = makePicture(path + file)
      finalPix = getPixels(finalPic)

#the following loop adds all pixles of the pictures in the pix list into pix
for pic in pics:
  pix.append(getPixels(pic))
 
#This loop is the meat of the program. It finds the rgb color values
# across all pixels in a single location and finds the meadian of each
for i in range(0,len(finalPix)):
  redPix = []
  greenPix = []
  bluePix = []
  for j in range(0,len(pics)):
    redPix.append(getRed(pix[j][i])) 
    greenPix.append(getGreen(pix[j][i]))  
    bluePix.append(getBlue(pix[j][i])) 
  redPix.sort()
  #redPix = myMergeSort(redPix)
  redPixel = redPix[len(redPix)//2]
  greenPix.sort()
  #greenPix = myMergeSort(greenPix)
  greenPixel = greenPix[len(greenPix)//2]
  bluePix.sort()
  #bluePix = myMergeSort(bluePix)
  bluePixel = bluePix[len(bluePix)//2]
  finalPix[i].setRed(redPixel)
  finalPix[i].setGreen(greenPixel)
  finalPix[i].setBlue(bluePixel)
    
#show the final pic and save it
show(finalPic)
writePictureTo(finalPic, path + "/final/final.png")
#print(time.time() - startTime)
