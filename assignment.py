from turtle import *


def draw_spiderMan():
    speed(13)  # Painting speed control
    bgcolor("Dark red")
    pensize(10)
    penup()
    goto(0, 50)
    pendown()
    circle(-120)
    penup()
    circle(-120, -60)
    pendown()
    pensize(5)
    right(50)
    circle(70, 55)
    right(85)
    circle(75, 58)
    right(90)
    circle(70, 55)
    right(90)
    circle(70, 58)
    # body
    penup()
    pensize(10)
    goto(80, 15)
    pendown()
    seth(92)
    fd(135)
    seth(125)
    circle(30, 135)
    seth(190)
    fd(50)
    seth(125)
    circle(30, 135)
    seth(275)
    fd(90)
    # Arm 1
    penup()
    pensize(10)
    goto(92, -150)
    seth(240)
    pendown()
    fd(80)
    left(10)
    circle(-28, 185)
    # Arm 2
    penup()
    goto(0, 50)
    seth(0)
    pensize(10)
    circle(-120, -60)
    seth(200)
    pendown()
    fd(72)
    left(20)
    circle(30, 150)
    left(20)
    fd(20)
    right(15)
    fd(10)
    pensize(5)
    fillcolor("#3366cc")
    begin_fill()
    seth(92)
    circle(-120, 31)
    seth(200)
    fd(45)
    left(90)
    fd(52)
    end_fill()
    fd(-12)
    right(90)
    fd(40)
    penup()
    right(90)
    fd(18)
    pendown()
    right(86)
    fd(40)
    penup()
    goto(-152, -86)
    pendown()
    left(40)
    circle(35, 90)
    # Body coloring
    penup()
    goto(-80, 116)
    seth(10)
    pensize(5)
    pendown()
    begin_fill()
    fillcolor("#3366cc")
    fd(155)
    seth(-88)
    fd(37)
    seth(195)
    fd(156)
    end_fill()
    penup()
    goto(-75, 38)
    seth(15)
    pendown()
    begin_fill()
    fd(158)
    seth(-88)
    fd(55)
    seth(140)
    circle(120, 78)
    end_fill()
    # Arm 1 To color
    penup()
    fillcolor("#3366cc")
    pensize(5)
    goto(75, -170)
    pendown()
    begin_fill()
    seth(240)
    fd(30)
    right(90)
    fd(17)
    end_fill()
    fd(10)
    left(80)
    fd(55)
    penup()
    left(90)
    fd(15)
    pendown()
    left(85)
    fd(55)
    penup()
    goto(43, -225)
    left(84)
    pendown()
    circle(60, 51)
    speed(0)
    # Body vertical lines
    for i in range(3):
        penup()
        goto(-70 + i * 15, 135)
        seth(-90)
        pendown()
        pensize(5)
        fd(15 - 2 * i)
    for i in range(3):
        penup()
        goto(36 + i * 15, 156)
        seth(-90)
        pendown()
        pensize(5)
        fd(15 - 2 * i)
        a = -60
        b = 70
    for i in range(4):
        penup()
        goto(a, b)
        a = a + 40
        b = b + 10
        seth(-90)
        pendown()
        pensize(5)
        fd(26)

    def oo(li, jing):
        penup()
        goto(0, 50)
        seth(0)
        circle(-120, li)
        pendown()
        right(jing)
        pensize(5)
        oo(-60, 110)
        fd(130)
        oo(-28, 96)
        fd(140)
        oo(9, 89)
        fd(144)
        oo(42, 70)
        fd(160)
        oo(80, 60)
        fd(130)
        penup()
        goto(-80, -40)
        right(160)
        pendown()
        right(50)
        circle(70, 45)
        right(75)
        circle(70, 38)
        right(50)
        circle(70, 45)
        right(90)
        circle(70, 48)
        penup()
        goto(-53, -70)
        pendown()
        left(40)
        circle(70, 30)
        right(50)
        circle(70, 20)
        right(50)
        circle(70, 38)
        right(70)
        circle(70, 24)
        penup()
        goto(-19, -105)
        left(72)
        pendown()
        fd(22)
        right(60)
        fd(22)
        oo(-140, 80)
        circle(-90, 120)
        penup()
        oo(140, 100)
        circle(90, 13)
        pendown()

    right(-50)
    circle(70, 45)
    right(75)
    circle(70, 38)
    right(50)
    circle(70, 36)
    penup()
    goto(22, -185)
    right(70)
    pendown()
    fd(72)
    penup()
    goto(-40, -182)
    right(38)
    pendown()
    fd(70)
    speed(10)
    # The left eye
    penup()
    pensize(7)
    goto(-15, -110)
    seth(0)
    pendown()
    pensize(10)
    begin_fill()
    left(130)
    fd(110)
    right(250)
    circle(90, 60)
    circle(40, 120)
    fillcolor("#F5FFFA")
    end_fill()
    # Right eye
    penup()
    goto(5, -110)
    pendown()
    begin_fill()
    right(30)
    fd(110)
    right(-250)
    circle(-90, 60)
    circle(-40, 120)
    end_fill()
    done()

def draw_spiral():
    from random import randint
    bgcolor('black')
    x = 1
    speed(0)
    while x < 600:  # 修改：增加循环次数，螺旋更密集
        r = randint(50, 255)  # 修改：限制最小值，避免太暗的颜色
        g = randint(50, 255)
        b = randint(50, 255)

        colormode(255)
        pencolor(r, g, b)
        fd(30 + x * 0.8)  # 修改：调整增长速率，使螺旋更紧凑
        rt(170)  # 修改：微调旋转角度，改变螺旋形状
        x = x + 1.5  # 修改：增加步长，绘图更快

    exitonclick()

def draw_python():
    import turtle as t
    t.setup(800, 300, 200, 200)
    t.penup()
    t.fd(-150)
    t.pendown()
    t.seth(-40)
    t.pensize(25)
    t.pencolor("purple")
    for i in range(4):
        t.circle(40, 80)
        t.circle(-40, 80)
    t.circle(40, 80 / 2)
    t.fd(40)
    t.circle(16, 180)
    t.fd(40 * 2 / 3)
    t.done()


def draw_flower():
    setup(700, 900, 0, 0)  # 修改：增大画布尺寸
    speed(0)
    penup()
    seth(90)
    fd(380)  # 修改：调整起始位置
    seth(0)
    pendown()

    # 花瓣部分 - 优化形状和流畅度
    speed(6)  # 修改：稍微加快速度
    begin_fill()
    fillcolor('#FF6B9D')  # 修改：改为粉红色，更柔和
    circle(55, 35)  # 修改：增大初始圆弧

    # 优化花瓣曲线
    for i in range(12):  # 修改：增加循环次数，曲线更平滑
        fd(1.2)
        left(8)
    circle(45, 45)

    for i in range(8):
        fd(1.5)
        left(2)
    circle(85, 45)  # 修改：调整圆弧大小

    for i in range(25):  # 修改：增加细节，使花瓣更自然
        fd(0.6)
        left(4)
    circle(85, 50)

    for i in range(15):  # 修改：优化曲线
        fd(1.8)
        left(1.5)
    circle(85, 30)

    for i in range(25):
        fd(0.8)
        left(3)
    circle(55, 55)

    # 花瓣主体完成
    circle(130, 60)  # 修改：增大圆弧，使花瓣更丰满

    speed(4)
    seth(-95)  # 修改：调整角度
    fd(75)  # 修改：增加长度

    right(145)  # 修改：优化转折角度
    fd(25)

    left(135)
    circle(150, 95)  # 修改：调整曲线

    left(25)
    circle(170, 105)

    left(135)
    fd(30)  # 修改：增加长度

    penup()
    right(145)
    circle(45, 85)
    pendown()

    left(120)
    fd(65)  # 修改：调整长度

    penup()
    left(175)  # 修改：优化角度
    fd(65)
    pendown()

    end_fill()

    # 花蕊部分 - 优化细节
    right(125)
    circle(-55, 55)
    circle(-25, 95)  # 修改：增大圆弧

    speed(2)
    fd(80)  # 修改：调整长度

    speed(2)
    circle(95, 120)  # 修改：优化曲线

    # 茎部 - 优化流畅度
    penup()
    left(158)
    fd(250)  # 修改：调整位置
    left(165)
    pendown()
    circle(220, 15)  # 修改：增大曲线
    circle(110, 45)
    circle(-60, 120)  # 修改：优化弧度
    left(25)
    circle(110, 25)
    circle(320, 25)  # 修改：增大曲线
    speed(2)
    fd(280)  # 修改：增加茎长度

    # 叶子1 - 优化形状
    penup()
    speed(3)
    left(175)
    fd(280)
    circle(-320, 10)  # 修改：调整曲线
    right(75)
    circle(220, 8)
    pendown()

    left(55)
    begin_fill()
    fillcolor('#2E8B57')  # 修改：改为更自然的绿色
    circle(-85, 110)  # 修改：优化叶子形状
    fd(15)
    left(25)
    circle(-70, 130)  # 修改：调整弧度
    end_fill()

    # 叶子细节
    penup()
    left(45)
    fd(25)
    left(180)
    pendown()
    circle(220, 30)  # 修改：优化连接曲线

    # 叶子2 - 优化对称性
    penup()
    right(155)
    fd(190)  # 修改：调整位置

    right(35)
    pendown()
    begin_fill()
    fillcolor('#2E8B57')
    circle(-95, 85)  # 修改：调整叶子大小
    right(145)
    fd(12)
    left(55)
    circle(-75, 102)  # 修改：优化形状
    end_fill()

    # 完成细节
    penup()
    left(55)
    fd(18)
    left(180)
    pendown()
    speed(2)
    circle(-220, 28)  # 修改：优化最终曲线

    # 添加花蕊细节
    penup()
    goto(0, 380)  # 修改：回到花朵中心
    pendown()
    begin_fill()
    fillcolor('#FFD700')  # 修改：添加黄色花蕊
    circle(15)  # 修改：添加圆形花蕊
    end_fill()

    exitonclick()


print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for python, 2 for flowers， 3 for spiral, 4 for spiderman)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_python()
        elif a == 2:
            draw_flower()
        elif a == 3:
            draw_spiral()
        elif a == 4:
            draw_spiderMan()
        else:
            print("Please input the value in [1,2,3,4]")
    except:
        print("Please input the value in [1,2,3,4]")


