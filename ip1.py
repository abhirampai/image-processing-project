import cv2
img =cv2.imread('mits-split.jpg')
[b,g,r]=img.shape
newimg=img.copy()
j=b/2
for i in range(0 , b/2):   
  newimg[i]=img[j]
  j=j+1
j=0  
for i in range(b/2,b):
  newimg[i]=img[j]
  j=j+1
cv2.imwrite('mits1.jpg',newimg)
