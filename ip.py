import cv2
img =cv2.imread('mits-swapped.jpg')
r= img[:,:,0]
b= img[:,:,1]
g= img[:,:,2]
newimg=img.copy()
newimg[:,:,0]=g
newimg[:,:,1]=r
newimg[:,:,2]=b
cv2.imwrite('mits.jpg',newimg)
