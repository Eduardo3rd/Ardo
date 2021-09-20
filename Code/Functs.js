//draw a grid 
for (var x = 0; x <= width; x += width / 100) {
	for (var y = 0; y <= height; y += height / 100) {
	  stroke(360);
	  strokeWeight(1);
	  line(x, 0, x, height);
	  line(0, y, width, y);
	}
  }