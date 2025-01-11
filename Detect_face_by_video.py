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
    img = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face")
    return img


video_path = "video1.mp4" 
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("ข้อผิดพลาด: ไม่สามารถโหลดวิดีโอได้")
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        print("วิดีโอจบลงแล้ว หรือเกิดข้อผิดพลาดในการอ่าน")
        break

    frame = detect(frame, faceCascade)

    cv2.imshow("Video", frame)


    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
