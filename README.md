# Single View Metrology

This project provides way of comparing heights of different objects in a single image using Single View Metrology and cross-ratio invariance under projective transformation {http://dhoiem.cs.illinois.edu/courses/vision_spring10/sources/criminisi00.pdf}

| <img src="https://raw.githubusercontent.com/kshitiz38/sv-metrology/master/1.jpg" alt="alt text" width="350" height=""> | <img src="https://raw.githubusercontent.com/kshitiz38/sv-metrology/master/2.png" alt="alt text" width="450" height="whatever"> |

##Requirements
1. OpenCV
2. Python

Tested with Python 2.7 on Ubuntu 16.04.

##Instruction to run
Run python sview_height.py
Follow these instructions:
-------------------------INSTRUCTIONS----------------------------"
1. Draw 8 line segments, holding mouse while drawing
2. First two for xVanish (vanishing point)
3. Next two for yVanish (vanishing point)
4. Next two for objects whose lengths are to be compared
5. First draw for shorter object in image plane starting from bottom
6. Then for other object again starting from bottom
7. Finally two for zVanish (vanishing point)
-----------------------------END---------------------------------"

##Feedback
All kind of feedback (code style, bugs, comments etc.) is welcome. Please open an issue on this repo instead of mailing me, since it helps me keep track of things better.

##License
MIT
