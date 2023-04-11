from PIL import Image
import os
dirname = os.path.dirname(__file__)

def baking(img,color,size,outputpath,outputname):
    w, h = img.size
    for x in range(w):
        for y in range(h):
            rgb_imnew= img.convert('RGBA')
            r, g, b, a = rgb_imnew.getpixel((x, y))
            if(a==0):                                               #transparent in grau>
                img.putpixel((x,y),(color,color,color))
    img = img.resize((size,size), Image.NEAREST)

    if os.path.isdir(outputpath):
        img.save(outputpath+outputname)
    else:
        print(outputpath)
        os.mkdir(os.path.join(outputpath))      

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
    baking(img=imgnew, color=30, size=800, outputname="mischmasher")

def recolor(img, color1, color2, outputpath, output):
    w, h = img.size
    img = img.convert('RGBA')
    imgV1=img.copy()
    imgV2=img.copy()
    uniqueColors=[tup[1] for tup in img.getcolors(w*h)]
    colorList = list(uniqueColors)
    reducedList=colorList
    #print(colorList)
    while (len(reducedList)>2):
        for v in colorList:
            if((v[0] == 255) and (v[1] == 255) and (v[2] == 255)):      #transparenz raus
                reducedList.remove(v)
                continue
            if((v[0] >= 248) and (v[1] >= 248) and (v[2] >= 248)):          #weiß raus
                reducedList.remove(v)
                continue
            if((v[0] <= 3) and (v[1] <= 3) and (v[2] <= 3)):                #schwarz raus
                reducedList.remove(v)
                continue
            if ((v[3]==0)):
                reducedList.remove(v)
                continue
    
    for x in range(w):
        for y in range(h):
                current_color = img.getpixel((x,y))
                if (current_color == (reducedList[0])):
                    imgV1.putpixel((x,y), color1)
                    imgV2.putpixel((x,y), color2)
                if (current_color == (reducedList[1])):
                    imgV1.putpixel((x,y), color2)
                    imgV2.putpixel((x,y), color1)
    baking(img=imgV1, color=30, size=800, outputpath=outputpath,outputname=output+"v1.png")
    baking(img=imgV2, color=30, size=800, outputpath=outputpath, outputname=output+"v2.png")

#Trans Pride Flagge
transBlau=91,207,250
transPink=245,170,185

#NB Pride Flagge
gelb=252,244,52
lila=156,89,209

#Genderqueer Flagge
genderLila=181,125,222
gendergreen=74,129,35

#Asexual Flagge
grey=163,163,163
asexlila=130,0,129

sourcePath = './gen2/'


for filename in os.listdir("./gen2/"):
    f = os.path.join(sourcePath, filename)
    if os.path.isfile(f):
        recolor(img=Image.open(f), color1=transBlau, color2=transPink, outputpath="./Output/trans/",output=filename[:3])
        recolor(img=Image.open(f), color1=gelb, color2=lila, outputpath="./Output/nb/",output=filename[:3])
        recolor(img=Image.open(f), color1=genderLila, color2=gendergreen, outputpath="./Output/queer/",output=filename[:3])
        recolor(img=Image.open(f), color1=grey, color2=asexlila, outputpath="./Output/asexuell/",output=filename[:3])
        print(f)

print("""
       ∧,,,∧
    (  ̳• · • ̳)
    /    づ♡ Done!!!
    """)  





