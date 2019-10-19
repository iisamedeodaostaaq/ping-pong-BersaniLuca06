xPos=40
yPos=50
xVers=+1
yVers=+1
zRac=265
zrac=250

def setup():
    size(900,500)
    
    
def draw():
    global xPos,yPos,xVers,yVers,zRac
    background("#072109")
    ellipse(xPos,yPos,50,50)
    xPos=xPos+2.5*xVers
    yPos=yPos+2.5*yVers
    
    if xPos>width or xPos<0:
        xVers=xVers*(-1)
        fill(random(0,255),random(0,255),random(0,255))

    if yPos>height or yPos<0:
        yVers*=-1
        fill(random(0,255),random(0,255),random(0,255))
    
    rect(zRac,height-25,90,60)

    if yPos+25>height-25 and xPos+25>zRac and xPos-25< zRac+90:
        yVers=-1
        
    rect(zrac,height-510, 90,30)
    
    if yPos-25<30 and xPos+25>zrac and xPos-25<zrac+90:
        yVers=+1
    
def keyPressed():
    global zRac,zrac
    
    if (keyCode==RIGHT and zRac<width-90):
        zRac+=10
    
    elif (keyCode==LEFT and zRac>0):
        zRac-=10
    
    if key=='d' and zrac<width-90:
        zrac+=10
    
    elif key=='a' and zrac>0:
        zrac-=10
