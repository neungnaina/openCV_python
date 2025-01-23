import cv2

# โหลด cascade classifier
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("eye.xml")
# ฟังก์ชันวาดกรอบและเพิ่มข้อความ
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    return img

# ฟังก์ชันตรวจจับใบหน้า
def detect(img, faceCascade):
    img = draw_boundary(img, faceCascade, 1.1, 5, (0, 255, 0), "Face")
    img = draw_boundary(img, eyeCascade, 1.1, 25, (155, 0, 0), "eye")
    return img

# เปิดใช้งานกล้องเว็บแคม
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ข้อผิดพลาด: ไม่สามารถเปิดกล้องได้")
    exit()

# วนลูปเพื่ออ่านภาพจากกล้อง
while True:
    ret, frame = cap.read()
    if not ret:
        print("ข้อผิดพลาด: ไม่สามารถอ่านเฟรมได้")
        break

    # ตรวจจับใบหน้า
    frame = detect(frame, faceCascade)

    # แสดงผลเฟรม
    cv2.imshow('frame', frame)

    # กด 'e' เพื่อออกจากลูป
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# ปิดการใช้งานกล้องและหน้าต่าง
cap.release()
cv2.destroyAllWindows()
