# EX-6 EDGE-DETECTION
## Aim:
To perform edge detection using Sobel, Laplacian, and Canny edge detectors.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import all the necessary modules for the program.

### Step2:
Load a image using imread() from cv2 module.

### Step3:
Convert the image to grayscale

### Step4:
Using Sobel operator from cv2,detect the edges of the image.

### Step5:

Using Laplacian operator from cv2,detect the edges of the image and Using Canny operator from cv2,detect the edges of the image.

## PROGRAM:
```
DEVELOPED BY: DIVYA.A
REGISTER NUMBER: 212222230034
```
## IMPORT PACKAGES AND LOAD IMAGES
  ```python
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("image.jpg",0)
gray=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
gray = cv2.GaussianBlur(gray,(3,3),0)
```
## SOBEL EDGE DETECTOR:
**SOBEL X:**
  ```python
  sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
plt.imshow(sobelx,cmap='gray')
plt.title("Sobel X axis")
plt.axis("off")
plt.show()
```
**SOBEL Y:**
```python
sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
plt.imshow(sobely,cmap='gray')
plt.title("Sobel Y axis")
plt.axis("off")
plt.show()
```
**SOBEL XY:**
  ```python
  sobelxy = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=5)
plt.imshow(sobelxy,cmap='gray')
plt.title("Sobel XY axis")
plt.axis("off")
plt.show()
```
## LAPLACIAN EDGE DETECTOR:
```python
lap=cv2.Laplacian(gray,cv2.CV_64F)
plt.imshow(lap,cmap='gray')
plt.title("Laplacian Edge Detector")
plt.axis("off")
plt.show()
```
## CANNY EDGE DETECTOR:
```python
canny=cv2.Canny(gray,120,150)
plt.imshow(canny,cmap='gray')
plt.title("Canny Edge Detector")
plt.axis("off")
plt.show()
```
## Output:
### ORIGINAL IMAGE:
![image](https://github.com/user-attachments/assets/7e6cf788-a510-42f7-a8a5-5a36d9fe3dc5)

### SOBEL EDGE DETECTOR
![Screenshot 2024-10-02 175022](https://github.com/user-attachments/assets/3f7e181b-a7e6-4f8f-be2d-9a4d1747bdc1)

![Screenshot 2024-10-02 175027](https://github.com/user-attachments/assets/287d969c-16b3-4fbd-8b44-eca66fcf297d)

![Screenshot 2024-10-02 175033](https://github.com/user-attachments/assets/7ac818d8-cf86-46c3-be23-872e6621d40d)


### LAPLACIAN EDGE DETECTOR
![Screenshot 2024-10-02 175039](https://github.com/user-attachments/assets/4b440b3e-4290-42db-922c-ac23e4bac1ea)



### CANNY EDGE DETECTOR
![Screenshot 2024-10-02 175045](https://github.com/user-attachments/assets/1b38a391-74c1-4916-9282-abda4103b5a7)


## Result:
Thus the edges are detected using Sobel, Laplacian, and Canny edge detectors.
