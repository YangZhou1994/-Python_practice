import cv2
import math

res = []
Max_area = 40000
for i in xrange(21):
    res.append([])
img = []

img.append(cv2.imread('/home/yang/Downloads/Test_1_Picture.jpg'))
img.append(cv2.imread('/home/yang/Downloads/Test_2_Picture.jpeg'))
img.append(cv2.imread('/home/yang/Downloads/Test_3_Picture.jpg'))
img.append(cv2.imread('/home/yang/Downloads/Test_4_Picture.jpg'))
img.append(cv2.imread('/home/yang/Downloads/Test_5_Picture.jpg'))
for i in range(0, len(img)):
    print
    print
    img_scale = []
    height, width = img[i].shape[:2]
    print height,width
    size = round(float(height) / float(width))
    new_width = math.sqrt(Max_area/size)
    new_height = Max_area/new_width
    print new_height,new_width
    img_scale.append(new_height / height)
    img_scale.append(new_width / width)
    print img_scale
    img_new = cv2.resize(img[i], None, None, fx=img_scale[1], fy=img_scale[0], interpolation=cv2.INTER_LINEAR)
    print img_new.shape[:2]
    print size
    res[int(size)].append(i)
# print "height : %d, width : %d, ratio : %d" % (height, width, size)

print size
print len(img)