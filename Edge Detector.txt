#blocks of pixel intensities across the image are collected and put in two arrays array3 and array4
#array4 pixels are collected at slightly different positions to array3 pixels and the
#difference between these arrays is computed after combining them in a single array, array5.
#This gives a measure of the contrast at the edges of shapes.

from PIL import Image #python image library
a=0 # initialising variables used in program
b=0 
f=0
k=0
i=0
e=0
c=0
d=0
count=0
count5=0
array1=[0]
array2=[0]
array3=[0]
array4=[0]
array5=[0]
array6=[0]
array7=[0]
array8=[0]
array9=[0]
array12=[0]
array15=[0]
for p in range (4,5):#next line of code is file location on laptop or desktop
    im = Image.open("C:/Users/User/Desktop/New folder/sea" + str(p) + ".jpg") 
    pix=im.load()
    for r in range (1,9): #this block of code inputs pixel values from across image as square blocks (70 pixels by 70 pixels in this case)
     for s in range (1,17):
      count=0
      for i in range (1,70,10):
       for j in range (1,70,10): 
        wet=pix [-50+i + s*70,-50+j + r*70 ] #changing the value of -50 px ( positive values too ) allows detector to be placed in desired region of image
        count=count+1
        a=a+wet[0] # one red pixel value
        c=c+wet[1] #one green pixel value
        e=e+wet[2] #one blue pixel value
        if count%36==0: #from [i2-i1] times [j2-j1] pixels
         b=b+a
         array1.insert(1,b)
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
      b=0 
      d=0
      f=0
print (array1)
array3=[0]
for h in range(1,17):
 for z in range (1,9):
  k= array1[h+(z-1)*16]
  array3.insert(1,k)    
  from PIL import Image #python image library
a=0 # initialising variables used in program
b=0 
c=0 
d=0 
e=0 
f=0
k=0
y=0
count=0
array2=[0]

for p in range (4,5):#next line of code is file location on laptop or desktop
    im = Image.open("C:/Users/User/Desktop/New folder/sea" + str(p) + ".jpg") 
    pix=im.load()
    for r in range (1,9): 
     for s in range (1,17):
      count=0
      for i in range (1,70,10):
       for j in range (1,70,10): 
        wet=pix [-50+i + s*70,-45 + j + r*70 ] #changing the value to -45 from 50 previously( positive values too ) allows contrast at edges to be detected
        count=count+1
        a=a+wet[0] # one red pixel value
        c=c+wet[1] #one green pixel value
        e=e+wet[2] #one blue pixel value
      
        if count%36==0: #from [i2-i1] times [j2-j1] pixels
         b=b+a
         array2.insert(1,b)
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
       b=0
       d=0
       f=0
count5=0
array1=[0]#making sure arrays are still zeroed
array4=[0]
array5=[0]
for h in range(1,17):
 for z in range (1,9):
  k= array2[h+(z-1)*16]
  array4.insert(1,k)
print (array3)
print (array4)
array5=array3 +array4
print(array5)
count5=0
f=0
e=0
count5=0
print (len(array3))#checking arrays are same length
print (len(array4))
print (len(array5))#checking combined array is twice the length of array3 and array4 combined
for f in range(1,17):
 for e in range (1,9):
  count5=count5+1
  for w in range (1,70):
   for v in range(1,70):
    if 800>array5[count5 +128]-array5[count5]>0:#edge detection over a range of pixel intensities
     im.putpixel([-50 + v + f*70 ,-50+w + e*70],(200,200,0))
     
im.show() #display image with horizontal edges marked to prove they were detected



