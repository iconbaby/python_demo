from PIL import Image
import sys

im = Image.open('test.png')
print(im.format, im.size, im.mode)
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')

print(sys.path)
