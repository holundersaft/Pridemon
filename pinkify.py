from PIL import Image


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

#def girlyfication():
#def sort_row(row):


#imgPath = './Pokemon/black-white/52.png'
imgPath = './gen2/Spr_2g_003.png'

pkmnReferenz = './Try/target.png'

img = Image.open(imgPath)
imgnew = img
uniqueColors = set()

#mischmascher(img,imgnew)
#baking(img=imgnew,color=30,size=800,outputname="test")
forceTrans(img=img)






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




