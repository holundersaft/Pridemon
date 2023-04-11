from PIL import Image
import numpy as np


def baking(img,color,size,outputname):
    w, h = img.size
    for x in range(w):
        for y in range(h):
            rgb_imnew= img.convert('RGBA')
            r, g, b, a = rgb_imnew.getpixel((x, y))
            if(a==0):                                               #transparent in grau>
                img.putpixel((x,y),(color,color,color))
    img = img.resize((size,size), Image.NEAREST)
    img.save(outputname+".png")
    print("""
       ∧,,,∧
    (  ̳• · • ̳)
    /    づ♡ Done!!!
    """)  

def mischmascher(img,imgnew):
    w,h = img.size
    for x in range(w):
        for y in range(h):
            rgb_image = img.convert('RGBA')
            r,g,b,a = rgb_image.getpixel((x,y))

            if (a==255):
                if((r_prev!=r)&(g_prev!=g)&(b_prev!=b)):           #neue pixel anders als alte
                    imgnew.putpixel((y,x),(g_prev,r_prev,b_prev))
            r_prev, g_prev, b_prev = r,g,b

def forceTrans(img):
    transBlau=91,207,250
    transPink=245,170,185
    w, h = img.size
    imgBlue=img.copy()
    imgPink=img.copy()
    uniqueColors=[tup[1] for tup in img.getcolors(w*h)]

    colorList = list(uniqueColors)
    reducedList=colorList
    while len(reducedList)>2:
        for v in colorList:
            if((v[0] == 255) and (v[1] == 255) and (v[2] == 255)):      #transparenz raus
                reducedList.remove(v)
        if((v[0] == 248) and (v[1] == 248) and (v[2] == 248)):          #weiß raus
                reducedList.remove(v)
        if((v[0] == 0) and (v[1] == 0) and (v[2] == 0)):                #schwarz raus
                reducedList.remove(v)
    for x in range(w):
        for y in range(h):
                current_color = img.getpixel((x,y))
                if (current_color == (reducedList[0])):
                    imgBlue.putpixel((x,y), transPink)
                    imgPink.putpixel((x,y), transBlau)
                if (current_color == (reducedList[1])):
                    imgBlue.putpixel((x,y), transBlau)
                    imgPink.putpixel((x,y), transPink)
    imgBlue.save("out.png")
    imgPink.save("out2.png")
    print("done")
#def girlyfication():
#def sort_row(row):


#imgPath = './Pokemon/black-white/52.png'
imgPath = './gen2/Spr_2g_001.png'

pkmnReferenz = './Try/target.png'

img = Image.open(imgPath)
imgnew = img
uniqueColors = set()

#mischmascher(img,imgnew)
#baking(img=imgnew,color=30,size=800,outputname="test")
forceTrans(img=img)
print("done")

'''
data = np.array(img)
r,g,b,a = data.T
#uniqueColors = np.unique(r,g,b,a)
print(np.unique(r))
print(np.unique(g))
print(np.unique(b))
white_areas = (r > 240) & (g > 240) & (b > 240) & (a > 240)
data[..., :-1][white_areas.T] = (255, 0, 0) # Transpose back needed 
print(info)
im2 = Image.fromarray(data)
im2.save("out.png")'''





'''for x in range(w):
    for y in range(h):
        pixel = img.getpixel((x, y))
        uniqueColors.add(pixel)
        rgb_im = img.convert('RGBA')
        r, g, b, a = rgb_im.getpixel((x, y))

        if(a==255):                                             #Farbaustausch>
            if((r_prev!=r)&(g_prev!=g)&(b_prev!=b)):           #neue pixel anders als alte
                imgnew.putpixel((y,x),(g_prev,r_prev,b_prev))
        r_prev, g_prev, b_prev = r,g,b '''
#totalUniqueColors = len(uniqueColors)    




