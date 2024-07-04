# p13_for_list_append
def setup():
    global imgBG, imgcapoo
    size(1313,876)# 用background.jpg的大小
    imgBG = loadImage('background.jpg')
    imgcapoo = loadImage('capoo.png') # 找半透明的png
def draw():
    global imgBG, imgcapoo
    image(imgBG, 0, 0)
    for i in range(len(x)):
        image(imgcapoo, x[i]-100, y[i]-115, 200, 200)
    image(imgcapoo, mouseX-100, mouseY-115, 200, 230)
x = [] # x = [0]*10
y = [] # y = [0]*10
#N = 0
def mousePressed():
    x.append(mouseX)#global N
    y.append(mouseY)
    #x[N], y[N] = mouseX, mouseY
    #N += 1
