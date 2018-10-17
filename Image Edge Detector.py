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
array1=[0]
array2=[0]
array3=[0]
array4=[0]
array5=[0]
for p in range (4,5):#next line of code is file location on laptop or desktop
    im = Image.open("C:/Users/User/Desktop/New folder/sea" + str(p) + ".jpg") 
    pix=im.load()
    for r in range (1,9): #this block of code generates square blocks made of  smaller square blocks of  pixels  to input pixel values from across image
     for s in range (1,17):
      count=0
      for i in range (1,70,10):
       for j in range (1,70,10): 
        wet=pix [-50+i + s*70,-45+j + r*70 ] #changing the value of -50 ( positive values too ) allows detector to be placed in desired region of image
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
x=250000
y=6000
for h in range(1,17):
 for z in range (1,8):
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
count=0
array2=[0]
for p in range (4,5):#next line of code is file location on laptop or desktop
    im = Image.open("C:/Users/User/Desktop/New folder/sea" + str(p) + ".jpg") 
    pix=im.load()
    for r in range (1,9): #this block of code generates square blocks made of  smaller square blocks of  pixels  to input pixel values from across image
     for s in range (1,17):
      count=0
      for i in range (1,70,10):
       for j in range (1,70,10): 
        wet=pix [-50+i + s*70,-50+ j + r*70 ] #changing the value of -50 ( positive values too ) allows detector to be placed in desired region of image
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
for h in range(1,17):
 for z in range (1,8):
  k= array2[h+(z-1)*16]
  array4.insert(1,k)
for t in range(0,112):
 i=array3[t] - array4[t]
 array5.insert(1,i)
print(array5)
for e in range(1,17):
 for f in range (1,8): 
  if  array5[e*f]>0:
   for w in range (1,70):
    for v in range(1,70):
     im.putpixel([-50 + v+ e*70,-45+w +f*70],(55,55,255))
im.show() #display image with horizontal edges marked to prove they were detected



