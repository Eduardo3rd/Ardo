let circleX;
let circleY;

function setup() {
  createCanvas(800, 800);
  circleX = width/2;
  circleY = height/2;
}

function draw() {
  background(255);

  // Get the current mouse position
  mouseX = mouseX;
  mouseY = mouseY;

  // Calculate the distance between the mouse and the center of the canvas
  d = dist(mouseX, mouseY, circleX, circleY);

  // Set the size and color of the shape based on the distance
  r = map(d, 0, width/2, 255, 0);
  g = map(d, 0, width/2, 128, 0);
  b = map(d, 0, width/2, 0, 255);
  shapeColor = color(r, g, b);

  // Interpolate between the size of the circle and the size of the square based on the distance
  shapeSize = map(d, 0, width/2, 50, 100);

  // Draw the shape around the mouse cursor with a colored outline and transparent center
  stroke(shapeColor);
  noFill();
  if (shapeSize < 75) {
    // Draw a circle if the size is less than 75
    circle(mouseX, mouseY, shapeSize);
  } else {
    // Draw a square if the size is greater than or equal to 75
    rect(mouseX-shapeSize/2, mouseY-shapeSize/2, shapeSize, shapeSize);
  }
}

