# p21_PaperScissorsStone01_text
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
