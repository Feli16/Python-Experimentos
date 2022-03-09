import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frintalface_default.xml")

img = cv2.imread("Prueba1.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMutltiScale(gray, 1.3,5)

for x,y,w,h in  faces:

    cv2.rectangle(img,(x,y)< (x+w,y+h), (255,0,255),2)

cv2.imwrite('Prueba1.jpg', img)
cv2.imshow('Face Destection', img)
cv2.destroyAllWindows