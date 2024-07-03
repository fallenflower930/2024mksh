# p08_two_image
size(1313,876)# 用background.jpg的大小
imgBG = loadImage('background.jpg')
image(imgBG, 0, 0)
imgcapoo = loadImage('capoo.png') # 找半透明的png
image(imgcapoo, 650, 400, 200, 200)
