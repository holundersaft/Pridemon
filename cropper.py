from PIL import Image
import os


sourcePath = './gen2 fake/'
destinyPath='./cropped/'

source = './gen2/'
destiny='./gen2Renamed/'
x=0

'''for filename in os.listdir(sourcePath):
    f = os.path.join(sourcePath, filename)
    # checking if it is a file
    if os.path.isfile(f):
        img = Image.open(f)
        w,h,= img.size
        imgnew = img.crop((0,0,w,w))
        #print(filename)
        imgnew.save(destinyPath+filename)'''


for filename in os.listdir(source):
    f = os.path.join(source, filename)
    # checking if it is a file
    if os.path.isfile(f):
        pkmnNumber = filename[-7:]
        img = Image.open(f)
        img.save(destiny+"test"+pkmnNumber)