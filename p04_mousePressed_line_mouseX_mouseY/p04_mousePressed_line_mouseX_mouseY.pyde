#存檔 p04_mousePressed_line_mouseX_mouseY
def setup():
    size(1000,1000)
    background(20,242,240)
def draw():
    if mousePressed:
     line(mouseX,mouseY,pmouseX,pmouseY)
    
