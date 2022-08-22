from PIL import Image

newImageName=f'./output/out.png'
newImage=Image.open(newImageName)
newPixels=newImage.load()
##loading the image with the key inside

width, height=newImage.size
for x in range(width):
    r,g,b=newPixels[x,0]
    print(chr(r),end = "")
    ##TODO fix this (why tf is it in reverse kekW
