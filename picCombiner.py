import os

def mySort(myList):
  for i in range(0,len(myList) - 1):
    for j in range(i+1, len(myList)):
      if myList[j] < myList[i]:
        temp = myList[i]
        myList[i] = myList[j]
        myList[j] = temp
        print(1)


pics = []
pix = []


path = "C:\\cygwin64\\home\\CSUMB\\CST205\\Project1\\pictures\\"

flag = True
for file in os.listdir(path):
  if file.endswith('.png'):
    pics.append(makePicture(path + file))
    if flag:
      flag = False
      finalPic = makePicture(path + file)
      finalPix = getPixels(finalPic)

for pic in pics:
  pix.append(getPixels(pic))
 
for i in range(0,len(finalPix)):
  redPix = []
  greenPix = []
  bluePix = []
  for j in range(0,len(pics)):
    redPix.append(getRed(pix[j][i])) 
    greenPix.append(getGreen(pix[j][i]))  
    bluePix.append(getBlue(pix[j][i])) 
  redPix.sort()
  redPixel = redPix[len(redPix)//2]
  greenPix.sort()
  greenPixel = greenPix[len(greenPix)//2]
  bluePix.sort()
  bluePixel = bluePix[len(bluePix)//2]
  finalPix[i].setRed(redPixel)
  finalPix[i].setGreen(greenPixel)
  finalPix[i].setBlue(bluePixel)
    
show(finalPic)
writePictureTo(finalPic, path + "/final/final.png")
  
