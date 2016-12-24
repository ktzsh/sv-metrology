import cv2
import math
from time import time

boxes = []

xCount = 0
yCount = 0
iter = 0

def on_mouse(event, x, y, flags, params):
    
    global iter
    t = time()

    if event == cv2.EVENT_LBUTTONDOWN:
        print 'Start Mouse Position: '+str(x)+', '+str(y)
        sbox = [x, y]
        boxes.append(sbox)

    elif event == cv2.EVENT_LBUTTONUP:
        print 'End Mouse Position: '+str(x)+', '+str(y)
        ebox = [x, y]
        boxes.append(ebox)
        # print boxes
        iter += 1
        # print iter


def line_intersection(line1, line2):

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) 

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def norm(point1, point2):

    xdiff = point1[0] - point2[0]
    ydiff = point1[1] - point2[1]

    norm = math.sqrt(xdiff*xdiff + ydiff*ydiff)
    # print norm
    return norm


print "-------------------------INSTRUCTIONS----------------------------"
print "Draw 8 line segments, holding mouse while drawing"
print "First two for xVanish"
print "Next two for yVanish"
print "Next two for objects whose lengths are to be compared"
print "First draw for shorter object in image plane starting from bottom"
print "Then for other object again starting from bottom"
print "Finally two for zVanish"
print "-----------------------------END---------------------------------"

count = 0
while(1):
    # print count
    if iter == 8:
        break

    count += 1
    img = cv2.imread('img2.jpg',0)
    # img = cv2.blur(img, (3,3))
    img = cv2.resize(img, None, fx = 0.8,fy = 0.8)

    cv2.namedWindow('real image')
    cv2.setMouseCallback('real image', on_mouse, 0)
    cv2.imshow('real image', img)

    if count < 50:
        if cv2.waitKey(33) == 27:
            cv2.destroyAllWindows()
            break
    elif count >= 50:
        count = 0

xVanish = line_intersection( [boxes[0],boxes[1]], [boxes[2],boxes[3]] )
print xVanish

yVanish = line_intersection( [boxes[4],boxes[5]], [boxes[6],boxes[7]] )
print yVanish

zVanish = line_intersection( [boxes[12],boxes[13]], [boxes[14],boxes[15]] )
print zVanish

print "Assuming bottom is given as first input for each object"
vertex = line_intersection( [xVanish,yVanish], [boxes[8],boxes[10]] )

bot = boxes[10]
ref = line_intersection( [vertex,boxes[9]], [boxes[10],boxes[11]] )
top = boxes[11]

response1 = float(raw_input("Please enter height of shorter object, enter 0 if unknown: "))
response2 = float(raw_input("Please enter height of other object, enter 0 if unknown: "))

response = response1 + response2
# print "Assuming Vz at infinity"
# print response

print "Length of unknown object is"
print ( (norm(top,bot)/norm(ref,bot))*(norm(zVanish,ref)/norm(zVanish,top))*response ) 