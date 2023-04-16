let curves;

function setup() {
  createCanvas(windowWidth, windowHeight);
  noLoop();
  curves = generateCurves();
}

function draw() {
  background(255);
  noFill();
  strokeWeight(2);

  curves.forEach((curve) => {
	beginShape();
	curve.forEach((point) => {
	  vertex(point.x, point.y);
	});
	endShape();
  });
}

function generateCurves() {
  const numCurves = random(5, 15);
  const curves = [];

  for (let i = 0; i < numCurves; i++) {
	const numPoints = random(10, 25);
	const points = [];

	for (let j = 0; j < numPoints; j++) {
	  const x = random(width);
	  const y = random(height);
	  points.push(createVector(x, y));
	}

	curves.push(points);
  }

  return curves;
}

function mouseMoved() {
  const brushSize = 40;
  const brushColor = color(random(255), random(255), random(255), 100);

  noStroke();
  fill(brushColor);

  curves.forEach((curve) => {
	curve.forEach((point) => {
	  const d = dist(mouseX, mouseY, point.x, point.y);
	  if (d < brushSize) {
		ellipse(point.x, point.y, brushSize - d, brushSize - d);
	  }
	});
  });
}
