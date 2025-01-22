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
    img = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face")
    img = draw_boundary(img, eyeCascade, 1.1, 25, (155, 0, 0), "eye")
    return img
# โหลดวิดีโอ

video_path = "video1.mp4" # ชื่อไฟล์วิดีโอ
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("ข้อผิดพลาด: ไม่สามารถโหลดวิดีโอได้")
    exit()
# วนลูปอ่านเฟรมจากวิดีโอ

while True:
    ret, frame = cap.read()
    if not ret:
        print("วิดีโอจบลงแล้ว หรือเกิดข้อผิดพลาดในการอ่าน")
        break

    # ตรวจจับใบหน้าในแต่ละเฟรม
    frame = detect(frame, faceCascade)
    # แสดงผลเฟรม
    cv2.imshow("Video", frame)

    # กดปุ่ม 'e' เพื่อออกจากลูป

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# ปิดการใช้งานวิดีโอและหน้าต่าง
cap.release()
cv2.destroyAllWindows()
