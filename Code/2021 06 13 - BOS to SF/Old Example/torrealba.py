'''
this is a rough tool set for generating images using the cairo graphics library
for python 3.x. i started using this workflow during the summer of 2018 and I
contine to build on it todayself.

i believe that each piece of art in existance is fundmentilly a routine running
inside of an enviroment comprised of initial and boundry conditions. those
conditions can take the form of materials, time, budget, skill level of the
artist, the tools available, the laws of physics, social norms, the historical
and political context of the moment, and a host of other limitations on expression.
i have no idea what makes a piece of art great in general, but i personally
find the most enjoyment in art that is challenging or pushing the edge of some
boundry condition. in short - i think that the conditions that shaped the production
of the art are the most intersting thing about the piece.

with all of that in mind, my conditions are supremely uninterestingself.

to do list:

turn common sub routines into functions:

- angled lines
- triangles
- squares
- rectangles
- time stamp each output in a folder
- JSON file with each of the random values from a canvas
- black and white coloring
- ovals
- learn how to use a fade effect

'''

import math
import random
import numpy as np

def RGBconv(value):
    return value/256

#N sided polygons

def triangle(dc, x, y, h, theta):
    theta = np.deg2rad(theta)
    o = math.sin(theta)*h
    a = math.cos(theta)*h

    p = (
        (x,y),
        (x,y+o),
        (x+a,y)
        )
    dc.move_to(x,y)
    for pair in p:
        dc.line_to(pair[0],pair[1])
    dc.close_path()

    #set outline color
    dc.set_source_rgb(RGBconv(256),RGBconv(256),RGBconv(256))
    dc.set_line_width(1)
    dc.stroke()

    #set fill color
    #dc.set_source_rgb(RGBconv(0),RGBconv(0),RGBconv(0))
    #dc.fill()

def square(dc, x, y, w):
    dc.new_sub_path()
    dc.rectangle(x, y, w, w)

    #set outline color
    dc.set_source_rgb(RGBconv(256),RGBconv(256),RGBconv(256))
    dc.set_line_width(1)
    dc.stroke()

    #set fill color
    #dc.set_source_rgb(RGBconv(0),RGBconv(0),RGBconv(0))
    #dc.fill()

#def pentagon(dc,x,y,...)

def hexagon(dc,D,x,y):
    alpha = D/4
    beta = math.sqrt(3)*alpha
    p = (
        (x+beta,y+alpha),
        (x,y+2*alpha),
        (x-beta,y+alpha),
        (x-beta,y-alpha),
        (x,y-2*alpha),
        (x+beta,y-alpha)
        )
    dc.move_to(x+beta,y+alpha)
    for pair in p:
        dc.line_to(pair[0],pair[1])
    dc.close_path()

    #set outline color
    dc.set_source_rgb(RGBconv(0),RGBconv(0),RGBconv(0))
    dc.set_line_width(1)
    dc.stroke()

    #set fill color
    #dc.set_source_rgb(RGBconv(0),RGBconv(0),RGBconv(0))
    #dc.fill()



def circle(dc, x, y, rad,r,g,b):
    dc.new_sub_path()
    dc.arc(x, y, rad, 0, 2 * math.pi)
    dc.set_source_rgb(RGBconv(r),RGBconv(g),RGBconv(b))
    dc.set_line_width(1)
    dc.stroke()



def hemisphere(dc,d,x,y,theta):
    dc.move_to(x,y)
    #values for first line
    theta = np.deg2rad(theta)
    y1 = int(-1*((d*np.sin(theta))-y))
    x1 = int(d*np.cos(theta)+x)
    x_mid = int((d/2)*np.cos(theta)+x)
    y_mid = int(-1*(((d/2)*np.sin(theta))-y))

    dc.line_to(x1,y1)
    dc.move_to(x_mid,y_mid)
    #dc.arc(x_mid,y_mid,d/2,theta,math.pi/2-theta)
    dc.arc_negative(x_mid,y_mid,d/2,theta+math.pi/2,2*math.pi-theta)
    dc.set_source_rgb(RGBconv(249),RGBconv(245),RGBconv(158))
    dc.fill()

def piettangle(dc,x1,y1,x2,y2,color):
    p = (
        (x1,y1),
        (x2,y1),
        (x2,y2),
        (x1,y2)
        )
    dc.move_to(x1,y1)
    for pair in p:
        dc.line_to(pair[0],pair[1])
    dc.close_path()
    dc.set_source_rgb(RGBconv(0),RGBconv(0),RGBconv(0))
    dc.set_line_width(2)
    dc.stroke_preserve()

    if color == 0:
        #red
        dc.set_source_rgb(RGBconv(256),RGBconv(0),RGBconv(0))
        dc.fill()

    if color == 1:
        #blue
        dc.set_source_rgb(RGBconv(0),RGBconv(0),RGBconv(256))
        dc.fill()

    if color == 2:
        #yellow
        dc.set_source_rgb(RGBconv(256),RGBconv(256),RGBconv(0))
        dc.fill()

    if color == 3:
        #white
        dc.set_source_rgb(RGBconv(256),RGBconv(256),RGBconv(256))
        dc.fill()

def piettangle_no(dc,x1,y1,x2,y2,color):
    p = (
        (x1,y1),
        (x2,y1),
        (x2,y2),
        (x1,y2)
        )
    dc.move_to(x1,y1)
    for pair in p:
        dc.line_to(pair[0],pair[1])
    dc.close_path()
    dc.set_source_rgb(RGBconv(0),RGBconv(0),RGBconv(0))
    dc.set_line_width(2)
    dc.stroke_preserve()

    if color == 0:
        #red
        dc.set_source_rgb(RGBconv(256),RGBconv(0),RGBconv(0))
        dc.fill()

    if color == 1:
        #blue
        dc.set_source_rgb(RGBconv(0),RGBconv(0),RGBconv(256))
        dc.fill()

    if color == 2:
        #yellow
        dc.set_source_rgb(RGBconv(256),RGBconv(256),RGBconv(0))
        dc.fill()

    if color == 3:
        #white
        dc.set_source_rgb(RGBconv(256),RGBconv(256),RGBconv(256))
        dc.fill()


def zurich(dc,mid_x,mid_y,frame,frames,max_length,num_arms):
    dc.move_to(mid_x,mid_y)

    angle = 2*math.pi/num_arms

    complete = frame/frames
    points = []

    for i in range(num_arms):
        x = math.cos(angle*i)*max_length*complete
        y = math.sin(angle*i)*max_length*complete
        points.append([x,y])


    for pair in points:
        dc.move_to(mid_x,mid_y)
        dc.line_to(pair[0],pair[1])
        dc.set_source_rgb(RGBconv(256),RGBconv(256),RGBconv(256))
        dc.set_line_width(5)
        dc.stroke_preserve()

def paris_offset(max):
    return random.randint(0,max) - random.randint(0,max)


def skew_poly(dc,w,h,size):

    fudge = random.randint(0,size) - random.randint(0,size)
    start_x = int(.1*w) + int(0.1*fudge)
    start_y = 0
    f_s = random.random()
    p = (
        (start_x,start_y),
        (int(.9*w) + int(f_s*fudge),0),
        (int(.7*w) + int(f_s*fudge),size),
        (int(.3*w) + int(f_s*fudge),size)
        )
    dc.move_to(start_x,start_y)
    for pair in p:
        dc.line_to(pair[0],pair[1])
    dc.close_path()

    coin = random.random()

    if coin >= 0.5:
        dc.set_source_rgb(RGBconv(256),RGBconv(256),RGBconv(256))
    else:
        dc.set_source_rgb(RGBconv(0),RGBconv(0),RGBconv(0))
    dc.fill()
