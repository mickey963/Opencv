import cv2

face_haar_cascade = cv2.CascadeClassifier(
    r"C:\Users\Dr-Sonnie\Favorites\Downloads\Data Science-20250702T100810Z-1-001 (1)\Data Science\haarcascade_frontalface_default.xml"
)

image = cv2.imread(r"C:\Users\Dr-Sonnie\Favorites\Downloads\download.jpg")

if image is None:
    print("⚠ Failed to load image!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

faces = face_haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)

cv2.imshow("Detected Faces", image)

k = cv2.waitKey(0) & 0xff
if k == 27:  # Esc key
    cv2.destroyAllWindows()