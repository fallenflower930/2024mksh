# p11_for_many_image
def setup():
    global imgBG, imgcapoo
    size(1313,876)# 用background.jpg的大小
    imgBG = loadImage('background.jpg')
    imgcapoo = loadImage('capoo.png') # 找半透明的png
def draw():
    image(imgBG, 0, 0)
    for i in range(10):
     for a in range(10):
        image(imgcapoo, i*100, a*100, 200, 200)
    image(imgcapoo, mouseX-100, mouseY-100, 200, 230)
