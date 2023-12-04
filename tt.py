# import streamlit as st

# import turtle

# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(0)

#colors = ['red', 'purple', 'blue', 'yelloe', 'orange']

# t.width(2)
#turtle.bgcolor('black')

# length = 5
# for i in range(200):
#     t.forward(length)
#     #t.pencolor(colors[length%6])
#     t.right(70)
#     length += 5






# n = 40
# ang = 360/n
# for i in range(n):
#     t.circle(80)
#     t.left(ang)
  



# turtle.done()








#s = 70

#if s >= 90:
#    '귀하의점수는 ' + str(s) + '점으로 :blue[A등급]입니다'
#elif s >= 80:
#    '귀하의점수는 ' + str(s) + '점으로 :blue[B등급]입니다'
#elif s >= 70:
#    '귀하의점수는 ' + str(s) + '점으로 :blue[C등급]입니다'
#elif s >= 60:
#    '귀하의점수는 ' + str(s) + '점으로 :blue[D등급]입니다' 
#else:
#    '귀하의점수는 ' + str(s) + '점으로 :blue[F등급]입니다' 

# s = 0 #초기값
# for i in range(1, 101, 2):
#     #'s ', s, 'i= ', i
#     s = s + i
#     #'s + i = ', s



# '7과 4의 산술연산'

# '덧샘', 7 + 4
# '뺄샘', 7 - 4
# '곰샘', 7 * 4
# '니늣샘', 7 / 4
# '몫', 7 // 4
# '나머지', 7 % 4 
# '거듭제곱', 2**4 




#import turtle   

#t = turtle.Turtle()
#t.shape('turtle')
#t.speed(1)







#turtle.done()

#distance = 50
#angle = 45
#for i in range(8):
#    t.forward(distance)
#    t.left(angle)

#t.forward(400)
#t.left(144)





#st.write('1'+'1')
#st.write(1+ 1)                                             
#st.write('스트림릿')
#st.title('streamlit image')
#st.image('im.jpg')

# #1
# import streamlit as st
# import time
# '나는 ' + str(12) + '개의 사과를 먹었다'

# #2
# 'apple' + 'grape'
# 'apple' * 30

# #3
# age = 20 
# if age < 20:
#     'aa'
# else:
#     'bb'

# #4
# '11/5', 11/5
# '11//5', 11//5
# '11%5', 11%5

# for i in range(1, 101):
#     if i%5 == 2:
#         i




# def user_sum(n):
#     s = 0
#     for i in range(1, n+1):
#         s = s + i
#     s 

# user_sum(100)
# user_sum(200)    


# s = 0
# for i in range(1, 11):
#     s = s + i
# s

# import tarfile
# import streamlit as st

# st.metric(label="Gas price", value=4, delta=-0.5,
#     delta_color="inverse")

# st.metric(label="Active developers", value=123, delta=123,
#     delta_color="off")

# # st.write('#green[**hello**],😁*woeld!*:sunglasses:')
# # st.write('#green[**hello**],😁*woeld!*:sunglasses:')
# # st.write('#green[**hello**],😁*woeld!*:sunglasses:')
# # st.write('#green[**hello**],😁*woeld!*:sunglasses:')

# import sys
# sys.exit()




# import random 


# import matplotlib.pyplot as pit

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(1, 10))

# plt.plot(numbers)
# plt.ylabel('some random numbers')
# plt.show()





# s1 = 1
# s2 = 2
# s3 = 3
# s4 = 4
# s5 = 5
# s1, s2, s3, s4, s5

# s = [3, 7, 1, 15, -6, 8, 9]

# mx = -1e10
# mx
# for i  in s:
#      if i > mx:
#          mx = i
# mx

# import turtle
# # import random
# t = turtle.Turtle()
# t.shape('turtle')

# def tree(length):
#    if length > 5:
#       t.forward(length)
#       t.right(20)
#       tree(length-15)
#       t.left(40)
#       tree(length-15)
#       t.right(20)
#       t.backward(length)

# t = turtle.Turtle()
# t.left(90)

# t.color('green')
# t.speed(0)
# tree(90)
# t.shape('turtle')
# sh = 3
# t.speed(0)
# t.pensize(5)
# t.goto(0,0)
# while True:
#    for i in range(30):
#       for _ in range(sh):
#           t.forward(1 + 5*i)
#           t.left(360/sh)
      
#       t.color((random.random(),random.random(),random.random()))
#       t.goto(i*10, 0)
# t.clear()
#   t.circle(1+5*i)

# t.forward(300)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(300)
# t.left(90)
# t.forward(100)

# t.up()
# t.goto(0, 0)
# t.down()
# t.circle(50)
# t.up()
# t.goto(200, 0)
# t.down()
# t.circle(50)




# t.fillcolor('blue')
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.forward(100)

# t.fillcolor('orange')
# t.begin_fill()
# t.circle(120)
# t.end_fill()

# screen = turtle.Screen()
# im1 = 'rabbit.gif'
# im2 = 'tuttle.gif'
# im3 = 'r.gif'

# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t3 = turtle.Turtle()

# screen.addshape(iml)
# screen.addshape(im2)
# screen.addshape(im3)

# t1.shape(iml)
# t2.shape(im2)
# t3.shape(im3)

# t1.penup()
# t1.shapesize(3)
# t1.goto(-300,100)

# t2.penup()
# t2.shapesize(3)
# t2.goto(-300,-100)

# t1.pendown()
# t2.pendown()
# t1.speed(1)
# t2.speed(1)


# for i in range(50):
#     d1 = r.randint(1, 30)
#     t1.forward(d1)
#     d2 = r.randint(1, 30)
#     t2.forward(d2)

# for _ in range(6):
#     a1 = r.randint(1, 45)
#     a2 = r.random()
#     a1,a2

# a = 0
# for i in range(100):
#     c = r.choice('abcedf')
#     if c == 'a':
#         a == a + 1





# def square(x, y, lx, ly):
#     t.up()
#     t.goto(x, y)
#     t.down()
#     for i in range(2):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)

# square(-200, 0, 100, 50)
# square(0, 0, 100, 150)
# square(200, 0, 100, 100)

# turtle.done()



import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

col1, col2, col3 = st.columns(3)

with col1:
    c1 = st.radio('선의 색을 선택 하시오', ['red', 'green', 'blue', 'orange'])
with col2:
    s1 = st.radio('선의 형태를 선택하시오', ['-', ':', '-.', '--'])
with col3:
    m1 = st.radio('마커의 형태를 선택하시오', ['o', '^', 's', 'p'])

fig, ax = plt.subplots()


x = []
y = []
for i in range(-20, 21, 2):
    x.append(i)
    y.append(-2*i*i - 3*i + 5)
    

# plt.plot(x,y, 'rs-', label = '2nd equation')
# plt.plot(x, ysin, 'go--', label = 'sin function')
# plt.legend()
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.xlim([-15, 15])
# plt.ylim([-2000, 2000])

plt.plot(x, y, color=c1, linestyle=s1, marker='h')

st.pyplot(fig) 


import sys
sys.exit()

fig, ax = plt.subplots()


