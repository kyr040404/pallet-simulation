import turtle
import sys
t = turtle.Turtle() #일반
m = turtle.Turtle() #트럭 그리기
m.speed(0)
t.speed(0)
turtle.colormode(255)
#turtle.bgcolor(0, 0, 0) #배경색 설정
t.ht() #터틀 숨기기
m.ht()

size = 55 #화면상 적재물 크기 [turtle에서]
cal_size = 110 #실제 적재물 크기 [계산 값]




def cube(x,y,size): #박스 만드는 함수
    t.up()
    t.goto(x, y)
    t.down()
    
    root = ((size/2)**2 + (size/2)**2)**0.5

    t.fillcolor(218, 65, 88)
    t.begin_fill()
    for i in range(4):
        t.lt(90)
        t.fd(size)
    t.end_fill()

    t.lt(45)

    t.fillcolor(132, 44, 54)
    t.begin_fill()
    t.fd(root)
    t.lt(45)
    t.fd(size)
    t.lt(135)
    t.fd(root)
    t.end_fill()

    t.fillcolor(172, 47, 64)
    t.begin_fill()
    t.rt(45)
    t.fd(size)
    t.rt(135)
    t.fd(root)
    t.rt(45)
    t.fd(size)
    t.end_fill()

    t.up()
    t.goto(x,y)
    t.down()

def map(): #map 함수
    t.up()
    #t.color("white") #배경 색과 반대 색으로
    t.goto(-150,270)
    t.write("상자 계산 프로그램",
            font=("", 40))
    
    
    t.color("black")

    #5톤
    t.goto(95,-190)
    t.down()
    t.left(45)
    t.fd(-100)
    t.write("    5톤 6.2m",
            font=("", 10))
    t.up()
    t.rt(45)
    
    #5톤+5톤 
    t.goto(200,-190)
    t.down()
    t.left(45)
    t.fd(-100)
    t.write("    5톤+5톤축 8.4m",
            font=("", 10))
    t.up()
    t.rt(45)
    
    #11~25톤
    t.goto(290,-190)
    t.down()
    t.left(45)
    t.fd(-100)
    t.write("    11~25톤 10.1m",
            font=("", 10))
    t.up()
    t.rt(45)
    
    #추레라
    t.goto(400,-190)
    t.down()
    t.left(45)
    t.fd(-100)
    t.write("    트레일러 12.0m",
            font=("", 10))
    t.up()
    t.rt(45)


# 트럭디자인 1. cube 안쪽면
    
    m.up()
    m.goto(-240,-190)
    m.down()

    m.lt(45)
    m.fd(90)
    m.rt(45)
    m.fd(630)
    m.fd(-628)
    m.lt(90)
    m.fd(124)
    
    m.up()
 
   
def truck(): #트럭디자인 2. cube 바깥면
    m.home()
    m.down()
    m.width(3)
    m.up()
    m.goto(400,-190)
    m.down()
    for i in range(2):
        m.lt(90)
        m.fd(130)
        m.lt(90)
        m.fd(640)
        
    m.lt(45)
    
    m.fd(80)
    m.lt(45)
    m.fd(130)
    m.lt(135)
    m.fd(80)

    m.rt(45)
    m.fd(640)
    m.rt(135)
    m.fd(80)
    m.rt(45)
    m.fd(640)
    

    m.up() #트럭 운전석
    m.goto(-240,-190)
    m.down()
    m.lt(180)
    m.fd(120)
    m.rt(90)
    m.fd(200)
    m.rt(45)
    m.fd(135)
    m.rt(45)
    m.fd(80)
    m.rt(90)
    m.fd(109)

    m.up() #트럭 바퀴
    m.goto(-290,-190)
    m.down()
    m.circle(40)

    m.up()
    m.goto(290,-190)
    m.down()
    m.circle(40)
    



    


def cube_1(x, y, size): #1층 쌓기
    global box_len_sum #총 상자 크기 전역변수
    for i in range(box_num//2): #나머지 0
        cube(x, y, size)
        cube(x-size/2 -1, y-size/2 -1, size)
        x = x + size +1
        box_len_sum = box_num//2 * cal_size

    if box_num % 2 == 1: #나머지 1 예외처리
        cube(x, y, size)
        box_len_sum = box_len_sum + cal_size


    
def cube_2(x, y, size): #2층 쌓기
    global box_len_sum #총 상자 크기 전역변수
    for i in range(box_num//4): #나머지 0
        cube(x, y, size)
        cube(x-size/2 -1, y-size/2 -1, size) #+- 1은 오차
        cube(x, y+size + 1, size)
        cube(x-size/2 -1, y+size/2 +1, size)
        x = x + size +1
        box_len_sum = box_num//4 * cal_size
        
    if box_num % 4 == 1: #나머지 1 예외처리
        cube(x, y, size)
        box_len_sum = box_len_sum + cal_size
        
    elif box_num % 4 == 2: #나머지 2 예외처리
        cube(x, y, size)
        cube(x-size/2 -1, y-size/2 -1, size)
        box_len_sum = box_len_sum + cal_size
        
        
    elif box_num % 4 == 3: #나머지 3 예외처리
        cube(x, y, size)
        cube(x-size/2 -1, y-size/2 -1, size)
        cube(x, y+size +1, size)
        box_len_sum = box_len_sum + cal_size

################################################      
#main
box_num = int(turtle.textinput("박스 계산","운반 할 상자가 몇개인가요? [1~40]"))
setting = int(turtle.textinput("박스 계산","몇층으로 쌓으시겠습니까? [1~2]"))
box_len_sum = 0

map()

if box_num == 0:
    t.clear()
    m.clear()
    t.up()
    t.goto(-320,0)
    t.write("ERROR: 알맞은 숫자를 다시 입력해주세요.",
            font=("", 20))
    sys.exit()

elif (box_num / setting) > 20:
    t.clear()
    m.clear()
    t.up()
    t.goto(-320,0)
    t.write("도로교통법 위반입니다:\n\t상자의 개수가 1층일 경우 20, 2층일 경우 40개까지만 가능합니다.",
            font=("", 20))
    sys.exit()
    
elif setting == 2 and (box_num / setting) < 21:
    cube_2(-150, -150, size)
    

elif setting == 1 and (box_num / setting) < 21:
    cube_1(-150, -150, size)

else:
    t.clear()
    m.clear()
    t.up()
    t.goto(-320,0)
    t.write("ERROR: 알맞은 숫자를 다시 입력해주세요.",
            font=("", 20))
    sys.exit()

t.up()
t.goto(-320,180)
t.write(f"* 상자 수: {box_num}\n* 층 수: {setting}\n* 총 길이: {box_len_sum/100} m",
            font=("", 20))
t.goto(130, 230)
t.write("* 상자는 파렛트 기준인 1.1m X 1.1m 규격입니다.\n* 결과가 보이지 않으면 창을 늘려보세요.",font=("", 13))

t.goto(100, 60)

if box_len_sum/100 <= 6.2:
    t.write("5톤 차량을 추천합니다.",font=("", 20))
elif box_len_sum/100 > 6.2 and box_len_sum/100 <= 8.4 :
    t.write("5톤+5톤 축 차량을 추천합니다.",font=("", 20))
elif box_len_sum/100 > 8.4 and box_len_sum/100 <= 10.1:
    t.write("11~25톤 차량을 추천합니다.",font=("", 20))
elif box_len_sum/100 > 10.1 and box_len_sum/100 <= 12.0:
    t.write("트레일러를 추천합니다.",font=("", 20))
else:
    t.write("ERROR",font=("", 20))
    
truck()
