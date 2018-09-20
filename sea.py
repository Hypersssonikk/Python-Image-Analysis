# Image colour intensity calculator and detector for red green blue
##Author Alistair J BAIN 14/09/2018 14.24
#this script adds together pixel values in small areas of an image to get an intensities for those areas.
#It places blocks of colour on the image where intensities are inside a certain user defined range.

from PIL import Image #python image library
a=0 # initialising variables used in program
b=0 
c=0 
d=0 
e=0 
f=0 
count=0 

for p in range (1,2):#next line of code is file location on laptop or desktop
    im = Image.open("C:/Users/User/Desktop/New folder/sea" + str(p) + ".jpg") 
    pix=im.load() 
    for s in range (1,5): #this block of code generates square blocks made of  smaller square blocks of  pixels  to input pixel values from across image
        for r in range (1,5):
            for m in range (0,5):
                for k in range(0,5):
                    count=0 
                    for i in range (1,2):
                     for j in range (1,2):
                        wet=pix [-50+i + s*100 + 19*k ,-70+j + 19*m + r*114 ] #changing the value of -50 ( positive values too ) allows detector to be placed in desired region of image
                        count=count+1
                        a=a+wet[0] # one red pixel value
                        c=c+wet[1] #one green pixel value
                        e=e+wet[2] #one blue pixel value
                        print(str(a) +"" + "red pixel value")
                        print(str(c) +  "" +"green pixel value")
                        print (str(e)+ ""  + "blue pixel value")
                        if count%1==0: #from [i2-i1] times [j2-j1] pixels
                            b=b+a 
                            print("b"," red pixels, from number of pixels equals [i2-i1]times[j2-j1] ")
                            print (b)
                            d=d+c
                            print("d"," blue pixels, from number of pixels equals [i2-i1]times[j2-j1]    ")
                            print (d)
                            f=f+e
                            print("f" ,"green pixels,from number of pixels equals [i2-i1]times[j2-j1]  ")
                            print (f)
                            a=0 
                            c=0
                            e=0
                            if 500>b>200 and 50<d<400 and 50<f<600:# b d anf f are sum of pixel values for each colour
                             for v in range (1,5): 
                              for w in range (1,5): 
                               im.putpixel([-50 + v + s*100 + 19*k ,-70+w + 19*m + r*114],(250,20,20))#puts a square of red pixels on image where intensity was inside the red,green and blue range criteria
                        b=0 
                        d=0
                        f=0

    im.show()#display image with red pixels showing where intensity was inside the red,green and blue range criteria
