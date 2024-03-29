from PIL import Image

key=open('input/message.txt', 'r').read()
k2=[]

for i in key:
    k2.append(ord(i))
    print(ord(i))
#transforming the key in an unicode list.

imgsrc=Image.open('input/in.png')
pixels=imgsrc.load()
width, height = imgsrc.size
if(len(k2) > width):
    print('the message you want to encode is too long ! It should be less than'
            , width) 
    #since the program is pretty basic and that I want to keep it simple,
    #I will not bother doing a 2nd line.

a=0
#a is a simple counter
for k in k2: 
    pixel = list(imgsrc.getpixel((a, 0)))
    a+=1
    print(*pixel)
#getting the pixel list of the first row of the image, goal is to have the
#pixel's rgb modified on the top row since this is the "easy" program.
#note that this is a test on how to iterate using the base image.

newImageName=f'./output/out.png'
newImage=Image.new(imgsrc.mode, imgsrc.size)
newPixels=newImage.load()
#Creating a new image in the output, with the same pixels as the basic one,
#then loading it.
q=0
for x in range(width):
    for y in range(height):
        if(y==0):
            if(q<=len(k2)-1):
                r, g, b =tuple(imgsrc.getpixel((x,y)))
                newPixels[x,y]=k2[q], g, b 
                print('newpixel value: ', newPixels[x,y])
                q+=1
                #Changing the red values for the first line pixels to encode 
                #the message, keeping original blue and green values.
            else:
                 newPixels[x,y]=imgsrc.getpixel((x,y))
        else:
            newPixels[x,y]=imgsrc.getpixel((x,y))
newImage.save(newImageName)



test=''
for j in k2:
    test+=(chr(j))
print(test)
#Test print of the key.
