from turtle import *
screensize(500,500)
color('red', 'yellow')
begin_fill()
def tebrik():
    penup()
    setpos(-240,240)
    pendown()
    goto(-240,200)
    penup()
    setpos(-240,220)
    pendown()
    goto(-200,220)
    penup()
    setpos(-200,240)
    pendown()
    goto(-200,200) # end of H
    penup()
    setpos(-180,200)
    pendown()
    goto(-160,240)
    goto(-140,200)
    penup()
    setpos(-143,220)
    pendown()
    goto(-170,220) # end of A
    penup()
    setpos(-130,200)
    pendown()
    goto(-130,220)
    goto(-140,240)
    penup()
    setpos(-130,220)
    pendown()
    goto(-120,240) # end of Y
    penup()
    setpos(-100,200)
    pendown()
    goto(-100,240) # end of I
    penup()
    setpos(-90,200)
    pendown()
    goto(-90,240)
    goto(-70,230)
    goto(-90,220)
    goto(-60,200) # end of R
    penup()
    setpos(-50,240)
    pendown()
    goto(-50,200)
    goto(-30,200) # end of L
    penup()
    setpos(-20,200)
    pendown()
    goto(-20,240) # end of I
    penup()
    setpos(-220,140) # here y(140) is our line
    pendown()
    goto(-240,160)
    goto(-220,180) # end of C
    penup()
    setpos(-200, 180)
    pendown()
    goto(-200,140)
    goto(-170,140)
    goto(-170,180) # end of U
    penup()
    setpos(-150, 140)
    pendown()
    goto(-150,180)
    goto(-140,160)
    goto(-130,180)
    goto(-130,140) # end of M
    penup()
    setpos(-120, 140)
    pendown()
    goto(-110,180)
    goto(-100, 140)
    penup()
    setpos(-105, 160)
    pendown()
    goto(-115,160) # end of A
    penup()
    setpos(-90, 180)
    pendown()
    goto(-90,140)
    goto(-60,140) # end of L
    penup()
    setpos(-50, 140)
    pendown()
    goto(-40,180)
    goto(-30,140)
    penup()
    setpos(-35, 160)
    pendown()
    goto(-45,160) # end of A
    penup()
    setpos(-20, 140)
    pendown()
    goto(-20,180)
    goto(0,170)
    goto(-20,160)
    goto(10,140) # end of R

def star():
    penup()
    setpos(100,10)
    pendown()
    color('red','black')
    begin_fill()
    while True:
        forward(144)
        left(144)
        if abs(pos()) < 1:
            break


end_fill()
tebrik()
star()