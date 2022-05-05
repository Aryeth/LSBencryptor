from PIL import Image

key=open('input/message.txt', 'r').read()
k2=[]

for i in key:
    k2.append(ord(i))
#transforming the key in an unicode list.
print(k2)

imgsrc=Image.open('input/in.png')
pixels=imgsrc.load()
width, height = imgsrc.size


a=0
for k in k2: 
    pixel = list(imgsrc.getpixel((a, 0)))
    a+=1
    print(type(pixel[1])) 
    print(*pixel)
##getting the pixel list of the first row of the image, goal is to have the pixel's rgb modified on the top row since this is the "easy" program.
##TODO: create a new image with the modified pixels since I do not wish to alterate the old image.

test=''
for j in k2:
    test+=(chr(j))
print(test)
##test print of the key.
