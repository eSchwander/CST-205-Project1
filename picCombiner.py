tolerance = 10
def closeRed(x,y):
  return (x.getRed() <= y.getRed() + tolerance and x.getRed() >= y.getRed() - tolerance)
def closeBlue(x,y):
  return (x.getBlue() <= y.getBlue() + tolerance and x.getBlue() >= y.getBlue() - tolerance)
def closeGreen(x,y):
  return (x.getGreen() <= y.getGreen() + tolerance and x.getGreen() >= y.getGreen() - tolerance)
  
def closeTo(pix1,pix2):
  return (closeRed(pix1,pix2) and closeBlue(pix1,pix2) and closeGreen(pix1,pix2))

pics = []
pix = []
path = "C:\\cygwin64\\home\\CSUMB\\CST205\\Project1\\pictures\\"

flag = True

#This loop creates a list with all the pictures in it
for x in range(1,10):
  file = str(x) + '.png'
  file = path + file
  if flag:
    toKeep = makePicture(file)
    flag = False
  pics.append(makePicture(file))
  
#This loop creates a list with pointers to all the pixels in the pics list
for pic in pics:
  pix.append(getPixels(pic))  

toKeepPix = getPixels(toKeep)
for pixel in toKeepPix:
  pixel.setColor(pix[0][0].getColor())
  

#Here we attempt to compare pixels
for i in range(0,len(pics)-1):
  for j in range(i+1,len(pics)):
    for k in range(0,len(pix[0])):
      if closeTo(pix[i][k],pix[j][k]):
        toKeepPix[k].setColor(pix[i][k].getColor())
     
show(toKeep)
writePictureTo(toKeep, path + "final.png")
  
