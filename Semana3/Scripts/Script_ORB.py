import cv2
from matplotlib import pyplot as plt
img = cv2.imread('/home/dani/Descargas/1.JPG',0)



orb = cv2.ORB_create(4000)
kp = orb.detect(img,None)
kp, des = orb.compute(img, kp)
img2 = cv2.drawKeypoints(img,kp,None,color=(255,255,0), flags=0)

plt.imshow(img),plt.show()
plt.imshow(img2),plt.show()

print len(kp)