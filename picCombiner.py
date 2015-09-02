pics = []

path = "C:\\cygwin64\\home\\CSUMB\\CST205\\Project1\\pictures\\"

for x in range(1,10):
  file = str(x) + '.png'
  file = path + file
  print(file)
  pics.append(makePicture(file))