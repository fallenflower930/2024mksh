# p12_for_many_image_list_def_mousePressed
def setup():
    global imgBG, imgcapoo
    size(1313,876)# 用background.jpg的大小
    imgBG = loadImage('background.jpg')
    imgcapoo = loadImage('capoo.png') # 找半透明的png
def draw():
    global imgBG, imgcapoo
    image(imgBG, 0, 0)
    for i in range(150):
        image(imgcapoo, x[i]-100, y[i]-115, 200, 200)
    image(imgcapoo, mouseX-100, mouseY-115, 200, 230)
x = [0]*150
y = [0]*150
N = 0
def mousePressed():
    global N
    x[N], y[N] = mouseX, mouseY
    N += 1
