import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/home/dani/Descargas/1.JPG',0)
sift = cv2.SIFT(4000)
kp, des = sift.detectAndCompute(img, None)
img2 = cv2.drawKeypoints(img, kp, None, (0,255,255), 4)
plt.imshow(img2),plt.show()
print len(kp)