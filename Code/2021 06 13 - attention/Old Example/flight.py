'''
image creation tool
January 2018
Eduardo Torrealba
'''

#cairo is the primary drawing library used to create images
import cairocffi as cairo
import math
import numpy as np
import random
import os
import datetime
import time
import torrealba as tor


#this is the funtion that draws the images
def images(num_images):

	for value in range(num_images):
		#start of canvas prep
		#image size in pixels
		w = 3000
		h = 3000

		#Red
		red1 = 220
		green1 = 97
		blue1 = 66

		#blue 1
		red2 = 75
		green2 = 117
		blue2 = 199

		#blue 2
		red3 = 35
		green3 = 57
		blue3 = 117

		surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
		dc = cairo.Context(surface) # drawing context
		red = tor.RGBconv(red1)
		green = tor.RGBconv(green1)
		blue = tor.RGBconv(blue1)
		dc.set_source_rgb(red, green, blue)
		dc.paint()

		#end of canvas prep


		instances = random.randint(2,100)
		for instance in range (instances):
			x_points = random.randint(50,500)
			offset = random.randint(0,3000) - random.randint(0,3000)
			period = random.randint(1,5)
			scale = 0.50
			which = random.random()
			D = random.randint(10,500)

			print(instance)

			if which >= 0.5:
				for x in range(x_points):

					#y_loc = (scale*math.sin(x/(x_points/period)*math.pi)*h)+offset
					#y_loc = (scale*math.sin(x/(x_points/period)*math.pi)*h)+offset


					y_loc = scale*math.exp(x/x_points)*h+offset

					x_loc = (x/x_points)*w

					#tor.circle(dc, x, y_loc, radius)
					#tor.triangle(dc, x, y_loc, hyp, theta)
					tor.circle(dc, x_loc, y_loc, D, red2, green2, blue2)


			if which < 0.5:
				for x in range(x_points):

					#y_loc = (scale*math.sin(x/(x_points/period)*math.pi)*h)+offset
					#y_loc = (scale*math.sin(x/(x_points/period)*math.pi)*h)+offset


					y_loc = scale*math.exp(-x/x_points)*h+offset

					x_loc = (x/x_points)*w

					#tor.circle(dc, x, y_loc, radius)
					#tor.triangle(dc, x, y_loc, hyp, theta)
					#tor.hexagon(dc,D,x_loc,y_loc)
					tor.circle(dc, x_loc, y_loc, D, red3, green3, blue3)



		#rad = 300
		#tor.circle(dc, w/4, h/4, rad, red1, green1, blue1)
		#tor.circle(dc, w/2, h/2, rad, red2, green2, blue2)
		#tor.circle(dc, 3*w/4, 3*h/4, rad, red3, green3, blue3)





		filename = 'whistler_'+ str(value) + '.png'
		surface.write_to_png(filename)
		print(filename)


def main():
	images(20)

if __name__ == '__main__':
	main()
