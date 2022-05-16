from PIL import Image

key=open('input/message.txt', 'r').read()
k2=[]

for i in key:
    k2.append(ord(i))
#transforming the key in an unicode list.

imgsrc=Image.open('input/in.png')
pixels=imgsrc.load()
width, height = imgsrc.size
if(len(k2) > width):
    print('the message you want to encode is too long ! It should be less than', width) 
    ##since the program is pretty basic and that I want to keep it simple, I will not bother doing a 2nd line.

a=0
##a is a simple counter
for k in k2: 
    pixel = list(imgsrc.getpixel((a, 0)))
    a+=1
    print(*pixel)
##getting the pixel list of the first row of the image, goal is to have the pixel's rgb modified on the top row since this is the "easy" program.
##note that this is a test on how to iterate using the base image.

newImageName=f'./output/out.png'
newImage=Image.new(imgsrc.mode, imgsrc.size)
newPixels=newImage.load()
##Creating a new image in the output, with the same pixels as the basic one, then loading it.
b=len(k2)-1
for x in range(width):
    for y in range(height):
        if(y==0):
            if(b>=0):
                newPixels[x,y]=k2[b]
                print('newpixel value: ', newPixels[x,y])
                b-=1
                ##changing the pixels of the first rows, putting the message on the red part of the pixel. I could let the old values for green and blue but maybe later cuz Im lazy.
            else:
                 newPixels[x,y]=imgsrc.getpixel((x,y))
        else:
            newPixels[x,y]=imgsrc.getpixel((x,y))
newImage.save(newImageName)



test=''
for j in k2:
    test+=(chr(j))
print(test)
##test print of the key.
