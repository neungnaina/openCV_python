import cv2


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    return img


def detect(img, faceCascade):
    img = draw_boundary(img, faceCascade, 1.1, 5, (0, 255, 0), "Face")
    return img


img = cv2.imread('women.jpg')


if img is None:
    print("ข้อผิดพลาด: ไม่สามารถโหลดภาพได้")
    exit()


img = detect(img, faceCascade)

cv2.imshow("output", img)


while True:
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cv2.destroyAllWindows()