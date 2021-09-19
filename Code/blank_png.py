#cairo is the primary drawing library used to create images
import cairocffi as cairo
import math
import numpy as np
import random
import os
import datetime
import time
import ardo 


#this is the funtion that draws the images
def images(num_images):

	for value in range(num_images):
		#start of canvas prep
		
		#image size in pixels
		w = 3000
		h = 3000
		
		# create the canvas 
		surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
		dc = cairo.Context(surface) 
		
		# set and fill the background color 
		dc.set_source_rgb(ardo.color['black'][0],ardo.color['black'][1],ardo.color['black'][2])
		dc.paint()

		#end of canvas prep
		
		
		#start of drawing 
		
		
		
		#write the png 
		filename = 'filename_'+ str(value) + '.png'
		surface.write_to_png(filename)
		print(filename)


def main():
	images(1)

if __name__ == '__main__':
	main()