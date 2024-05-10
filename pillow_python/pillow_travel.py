from PIL import Image,ImageFilter


# 裁剪图片
def tailor():
    image = Image.open('go.png')
    rect = 80, 20, 310, 360
    image.crop(rect).show()
# tailor()

# 缩量
def abbreviate():
    image = Image.open('go.png')
    size = 1000,1000
    image.thumbnail(size)
    image.show()

# abbreviate()

# 去色
def lujing():
    image = Image.open('go.png')
    image.filter(ImageFilter.CONTOUR).show()

lujing()