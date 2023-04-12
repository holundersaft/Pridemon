from PIL import Image
import os
import time
dirname = os.path.dirname(__file__)

start=time.time()
counter=0

def baking(img,color,size,outputpath,outputName):
    #print(outputName)
    w, h = img.size
    for x in range(w):
        for y in range(h):
            rgb_imnew= img.convert('RGBA')
            r, g, b, a = rgb_imnew.getpixel((x, y))
            if(a==0):                                               #transparent in grau>
                img.putpixel((x,y),(color,color,color))
    img = img.resize((size,size), Image.NEAREST)

    if os.path.isdir(outputpath):
        img.save(outputpath+outputName)
    else:
        #print(outputpath)
        os.mkdir(os.path.join(outputpath))
        img.save(outputpath+outputName)

    print(outputpath+outputName)
    global counter
    counter += 1
    

def mischmascher(img):
    w,h = img.size
    imgnew=img.copy()
    for x in range(w):
        for y in range(h):
            rgb_image = img.convert('RGBA')
            r,g,b,a = rgb_image.getpixel((x,y))

            if (a==255):
                if((r_prev!=r)&(g_prev!=g)&(b_prev!=b)):           #neue pixel anders als alte
                    imgnew.putpixel((y,x),(g_prev,r_prev,b_prev))
            r_prev, g_prev, b_prev = r,g,b
    baking(img=imgnew, color=30, size=800, outputName="mischmasher")

def recolor(img, outputName, outputPath=None, color1=None, color2=None, black=(0,0,0),white=(248,248,248)):
    w, h = img.size
    img = img.convert('RGBA')
    imgV1=img.copy()
    imgV2=img.copy()

    

    uniqueColors=[tup[1] for tup in img.getcolors(w*h)]
    colorList = list(uniqueColors)
    colorList=sorted(colorList, key=sum)

    reducedList=colorList
    reducedList=[x for x in reducedList if x[3] == 255] #macht alles weg außer die 4 gewünschten Farben 

    if (color1 == None):
        color1 = reducedList[1]
    if (color2 == None):
        color2 = reducedList[2]

    for x in range(w):
        for y in range(h):

            current_color = img.getpixel((x,y))
            if (current_color == (reducedList[0])):
                imgV1.putpixel((x,y), black)
                imgV2.putpixel((x,y), black)
            if (current_color == (reducedList[1])):
                imgV1.putpixel((x,y), color1)
                imgV2.putpixel((x,y), color2)
            if (current_color == (reducedList[2])):
                imgV1.putpixel((x,y), color2)
                imgV2.putpixel((x,y), color1)
            if (current_color == (reducedList[3])):
                imgV1.putpixel((x,y), white)
                imgV2.putpixel((x,y), white)
                
    outputName=outputName[:-4]

    if (outputPath==None):
        outputPath="./Output/"
    else:
        outputPath="./Output/"+outputPath+"/"
    baking(img=imgV1, color=30, size=800, outputpath=outputPath,outputName=outputName+"v1.png")
    baking(img=imgV2, color=30, size=800, outputpath=outputPath, outputName=outputName+"v2.png")

def kitty(timer=0, counter=0)
    

#Trans Pride Flagge
transBlau=91,207,250
transPink=245,170,185

#NB Pride Flagge
nbGelb=252,244,52
nbLila=156,89,209

#Genderqueer Flagge
genderLila=181,125,222
genderGrün=74,129,35

#Asexual Flagge
asexGrau=163,163,163
asexLila=130,0,129

#bisexual
biPink=214,2,112
biRosa=155,79,150
biBlau=0,56,168

#pan
panPink=255,33,140
panGelb=255,216,0
panTürkis=33,177,255




sourcePath = "./testmon/"


for filename in os.listdir(sourcePath):
    f = os.path.join(sourcePath, filename)
    if os.path.isfile(f):
        recolor(img=Image.open(f), outputName=filename, outputPath="normal")

        '''recolor(img=Image.open(f), outputName=filename, outputPath="trans", color1=transBlau, color2=transPink)
        recolor(img=Image.open(f), outputName=filename, outputPath="nonbinary", color1=nbGelb, color2=nbLila)
        recolor(img=Image.open(f), outputName=filename, outputPath="genderqueer", color1=genderLila, color2=genderGrün)
        recolor(img=Image.open(f), outputName=filename, outputPath="asexuell", color1=asexGrau, color2=asexLila)

        #DER BI BLOCK
        recolor(img=Image.open(f), outputName=filename, outputPath="bi1", color1=biPink, color2=biRosa, black=biBlau)
        recolor(img=Image.open(f), outputName=filename, outputPath="bi2", color1=biPink, color2=biRosa, white=biBlau)

        recolor(img=Image.open(f), outputName=filename, outputPath="bi3", color1=biRosa, color2=biBlau, black=biPink)
        recolor(img=Image.open(f), outputName=filename, outputPath="bi4", color1=biRosa, color2=biBlau, white=biPink)

        recolor(img=Image.open(f), outputName=filename, outputPath="bi5", color1=biPink, color2=biBlau, white=biRosa)
        recolor(img=Image.open(f), outputName=filename, outputPath="bi6", color1=biPink, color2=biBlau, black=biRosa)

        #DER PAN BLOCK
        recolor(img=Image.open(f), outputName=filename, outputPath="pan1", color1=panPink, color2=panGelb, black=panTürkis)
        recolor(img=Image.open(f), outputName=filename, outputPath="pan2", color1=panPink, color2=panGelb, white=panTürkis)

        recolor(img=Image.open(f), outputName=filename, outputPath="pan3", color1=panGelb, color2=panTürkis, black=panPink)
        recolor(img=Image.open(f), outputName=filename, outputPath="pan4", color1=panGelb, color2=panTürkis, white=panPink)

        recolor(img=Image.open(f), outputName=filename, outputPath="pan5", color1=panPink, color2=panTürkis, white=panGelb)
        recolor(img=Image.open(f), outputName=filename, outputPath="pan6", color1=panPink, color2=panTürkis, black=panGelb)'''

       




end=time.time()
timer=round(end-start)
if (timer<60):
    minuten=round(timer/60)
    sekunden=timer%60
    aussage=("♡♡♡♡ "+str(minuten)+ " Minuten & "+ str(sekunden)+" Sekunden Runtime für insgesamt "+str(counter) +" Bilder ♡♡♡♡")
else:
    aussage=("♡♡♡♡ "+str(timer)+" Sekunden Runtime für insgesamt "+str(counter) +" Bilder ♡♡♡♡")

          
print("""


  ✦*͙*❥⃝∗⁎.ʚɞ.⁎∗❥⃝**͙✦

       ∧,,,∧
    (  ̳• · • ̳)
    /    づ     """+str(timer)+"""Sekunden Runtime für insgesamt """+str(counter) +""" Bilder
    
  ✦*͙*❥⃝∗⁎.ʚɞ.⁎∗❥⃝**͙✦
  
  """)







