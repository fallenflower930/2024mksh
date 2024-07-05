# p24_PaperScissorsStone04_for_simple
select = -1
def setup():
    size(600,300)
def draw():
    global select 
    fill(255)
    rect(0,0,300,300)
    rect(300,0,300,300)
    for i in range (3):
       if select==i:fill(255,0,0)
       else: fill(255)
       rect(400,100+i*50,100,50)
    
    textSize(25)#文字大小
    textAlign(LEFT,TOP)
    fill(0)
    text("Scissor",400,150)
    text("Stone",400,200)
    text("Paper",400,100)
def mousePressed():#若按下mouse
    global select
    if 400 < mouseX < 400+100:#左右在範圍內
      if 100 < mouseY < 150: select = 0#上下範圍也對
      if 150 < mouseY < 200: select = 1
      if 200 < mouseY < 250: select = 2
