# Basic Code Explanations


Basic Code Explanations

import cv2

import numpy as np

cv2: We import the OpenCV library, which provides image processing functions.

numpy: We import the numpy library to use it alongside OpenCV. It is used for numerical and matrix operations.

cap = cv2.VideoCapture(0)

cv2.VideoCapture(0): Starts the camera connected to the computer. (0) refers to the default camera (usually the internal one). If there's an external camera, it can be accessed with another index like (1).

while True:

    ret, frame = cap.read()

    if not ret:

        break

while True: Starts an infinite loop. The camera keeps running and captures new frames.

ret, frame = cap.read(): Captures a frame from the camera. The value of ret is a flag (True or False) to check if the camera is working properly. frame is the image data obtained from the camera.

if not ret: break: Ends the loop if ret is False. This means the camera isn't functioning correctly.

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY): Converts the colored image in frame to grayscale. This is essential for operations like edge detection, as working with grayscale images is faster than color images.

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.GaussianBlur(gray, (5, 5), 0): Applies a Gaussian blur filter to the gray image. (5, 5) defines the size of the blur kernel. This reduces noise and improves edge detection.

edges = cv2.Canny(blurred, 200, 450)

cv2.Canny(blurred, 200, 450): Performs Canny edge detection. 200 and 450 are the lower and upper threshold values used in edge detection. High values help find only the most prominent edges.

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE): Finds contours (boundaries) in the edges image. Extracts contours of the detected shapes.

cv2.RETR_EXTERNAL: Finds only the external contours, ignoring the internal ones.

cv2.CHAIN_APPROX_SIMPLE: Simplifies contours by removing unnecessary points and returns only the essential corner points.

shape_count = 0

shape_count = 0: A counter variable to keep track of the number of shapes found and to be displayed. Used to limit the number of shapes to 5.

for contour in contours:

    if shape_count >= 5:

        break

for contour in contours: Iterates through each detected contour (shape boundary).

if shape_count >= 5: break: Breaks the loop if 5 or more shapes are detected to prevent drawing new ones.

epsilon = 0.02 * cv2.arcLength(contour, True)

cv2.arcLength(contour, True): Calculates the perimeter of the contour. True indicates the contour is a closed shape.

epsilon = 0.02 * cv2.arcLength(contour, True): Takes 2% of the perimeter as the approximation accuracy (epsilon).

approx = cv2.approxPolyDP(contour, epsilon, True)

cv2.approxPolyDP(contour, epsilon, True): Approximates the contour using the given epsilon value, simplifying the number of corners of the shape.

num_vertices = len(approx)

len(approx): Calculates the number of corner points in approx. This indicates the number of vertices of the shape.

shape = 'Unknown'

if num_vertices == 3:

    shape = 'Triangle'

elif num_vertices == 4:

    shape = 'Rectangle'

elif num_vertices > 8:

    shape = 'Circle'

shape = 'Unknown': A variable to hold the name of the shape, defaulted to "Unknown".

if num_vertices == 3: If the number of vertices is 3, the shape is a 'Triangle'.

elif num_vertices == 4: If the number of vertices is 4, the shape is a 'Rectangle'.

elif num_vertices > 8: If more than 8 vertices, the shape is a 'Circle'.

cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)

cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2): Draws the shape on the frame. [approx] represents the contour to be drawn.

(0, 255, 0): Drawing color (green).

2: Line thickness.

x, y = approx.ravel()[0], approx.ravel()[1] - 10

approx.ravel(): Converts the coordinates in approx to a single array.

[0] and [1] - 10: Specifies the x and y coordinates for the text position. The y-value is moved 10 pixels up to display the text above the shape.

cv2.putText(frame, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.putText(...): Draws the name of the shape on the frame.

shape: The text to be drawn (name of the shape).

(x, y): Position of the text.

cv2.FONT_HERSHEY_SIMPLEX: Font type.

0.5: Font size.

(0, 255, 0): Text color (green).

2: Text thickness.

shape_count += 1

shape_count += 1: Increments the number of detected and drawn shapes by one.

cv2.imshow('Camera', frame)

cv2.imshow('Camera', frame): Displays the frame with the title 'Camera'.

if cv2.waitKey(1) & 0xFF == ord('q'):

    break

cv2.waitKey(1): Waits for 1 millisecond. Returns the ASCII value if a key is pressed.

& 0xFF == ord('q'): If the pressed key is 'q', breaks the loop and ends the program.

cap.release()

cv2.destroyAllWindows()

cap.release(): Releases the camera.

cv2.destroyAllWindows(): Closes all open OpenCV windows.
