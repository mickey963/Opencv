import cv2

face_haar_cascade = cv2.CascadeClassifier(r"C:\Users\Dr-Sonnie\Favorites\Downloads\Data Science-20250702T100810Z-1-001 (1)\Data Science\haarcascade_frontalface_default.xml")

image = cv2.imread(r"C:\Users\Dr-Sonnie\Favorites\Downloads\download.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()