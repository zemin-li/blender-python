import cv2
img = cv2.imread("0.png")############图片读取
pictue_size=img.shape
picture_height=pictue_size[0]
picture_width=pictue_size[1]
print(picture_height,picture_width)
img=cv2.resize(img,(int(picture_width/2),int(picture_height/2)))
cv2.namedWindow("img",cv2.WINDOW_FREERATIO)
cv2.imshow('img',img)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.namedWindow("img_hsv",cv2.WINDOW_FREERATIO)
cv2.imshow('img_hsv',img_hsv)

# i = 0
# for a in range(picture_height):
#     for b in range(picture_width):
#         if img[a,b].all() > 0:
#             i= i + 1
# print(i)
cv2.waitKey(0)
