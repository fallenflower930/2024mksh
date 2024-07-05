# p22_PaperScissorsStone02_mousePressed
def setup():
    size(600,300)
def draw():
    fill(255)
    rect(0,0,300,300)
    rect(300,0,300,300)
    
    rect(400,100,100,50)
    rect(400,150,100,50)
    rect(400,200,100,50)
    textSize(25)#文字大小
    textAlign(LEFT,TOP)
    fill(0)
    text("Scissor",400,150)
    text("Stone",400,200)
    text("Paper",400,100)
def mousePressed():#若按下mouse
    sselect = -1#沒選擇
    if 400 < mouseX < 400+100:#左右在範圍內
      if 100 < mouseY < 150: select = 0#上下範圍也對
      if 150 < mouseY < 200: select = 1
      if 200 < mouseY < 250: select = 2
    print (select)#印出選擇
