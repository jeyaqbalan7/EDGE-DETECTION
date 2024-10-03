#DEVELOPED BY: DIVYA.A
#REGISTER NUMBER: 212222230034

## IMPORT PACKAGES AND LOAD IMAGES
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("image.jpg",0)
gray=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
gray = cv2.GaussianBlur(gray,(3,3),0)

## SOBEL EDGE DETECTOR:
## **SOBEL X:**
sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
plt.imshow(sobelx,cmap='gray')
plt.title("Sobel X axis")
plt.axis("off")
plt.show()

## **SOBEL Y:**
sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
plt.imshow(sobely,cmap='gray')
plt.title("Sobel Y axis")
plt.axis("off")
plt.show()

##**SOBEL XY:**
sobelxy = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=5)
plt.imshow(sobelxy,cmap='gray')
plt.title("Sobel XY axis")
plt.axis("off")
plt.show()

## LAPLACIAN EDGE DETECTOR:
lap=cv2.Laplacian(gray,cv2.CV_64F)
plt.imshow(lap,cmap='gray')
plt.title("Laplacian Edge Detector")
plt.axis("off")
plt.show()

## CANNY EDGE DETECTOR:
canny=cv2.Canny(gray,120,150)
plt.imshow(canny,cmap='gray')
plt.title("Canny Edge Detector")
plt.axis("off")
plt.show()

