import cv2 # นำเข้าไลบรารี OpenCV

# โหลดไฟล์ Cascade Classifier สำหรับตรวจจับใบหน้า ดวงตา จมูก ปาก และแมว
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # ตรวจจับใบหน้า
eyeCascade = cv2.CascadeClassifier("eye.xml") # ตรวจจับดวงตา
noseCascade = cv2.CascadeClassifier("nose.xml") # ตรวจจับจมูก
mouthCascade = cv2.CascadeClassifier("mouth.xml") # ตรวจจับปาก
catCascade = cv2.CascadeClassifier("cat_face.xml") # ตรวจจับใบหน้าแมว

# ฟังก์ชันวาดกรอบรอบวัตถุที่ตรวจพบ และเพิ่มข้อความกำกับ
# รับพารามิเตอร์เป็นรูปภาพ, ตัวตรวจจับ, scaleFactor, minNeighbors, สีของกรอบ และข้อความกำกับ
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # แปลงภาพเป็นระดับสีเทา
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    for (x, y, w, h) in features: # วนลูปผ่านสิ่งที่ตรวจพบ
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2) # วาดกรอบสี่เหลี่ยมรอบวัตถุที่ตรวจพบ
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2) # เพิ่มข้อความกำกับ
    return img # คืนค่าภาพที่มีกรอบและข้อความกำกับ

# ฟังก์ชันตรวจจับใบหน้า
def detect(img, faceCascade):
    img = draw_boundary(img, faceCascade, 1.1, 5, (0, 255, 0), "Face") # ตรวจจับใบหน้า
    img = draw_boundary(img, eyeCascade, 1.1, 25, (155, 0, 0), "eye") # ตรวจจับดวงตา
    img = draw_boundary(img, noseCascade, 1.1, 50, (0, 0, 255), "nose") # ตรวจจับจมูก
    img = draw_boundary(img, mouthCascade, 1.2, 40, (70, 0, 100), "mouth") # ตรวจจับปาก
    img = draw_boundary(img, catCascade, 1.1,10, (155, 0, 255), "cat")  # ตรวจจับใบหน้าแมว
    return img

# เปิดใช้งานกล้องเว็บแคม
cap = cv2.VideoCapture(0) # เปิดกล้องหมายเลข 0 (กล้องเริ่มต้นของระบบ)

 # ตรวจสอบว่ากล้องเปิดได้หรือไม่
if not cap.isOpened():
    print("ข้อผิดพลาด: ไม่สามารถเปิดกล้องได้") # แสดงข้อความข้อผิดพลาด
    exit() # ออกจากโปรแกรม

# วนลูปเพื่ออ่านภาพจากกล้องแบบเรียลไทม์
while True:
    ret, frame = cap.read() # อ่านเฟรมจากกล้อง
    if not ret:
        print("ข้อผิดพลาด: ไม่สามารถอ่านเฟรมได้") # แสดงข้อความข้อผิดพลาดหากอ่านเฟรมไม่ได้
        break  # ออกจากลูป

    # ตรวจจับใบหน้า
    frame = detect(frame, faceCascade)  # เรียกใช้ฟังก์ชันตรวจจับเพื่อเพิ่มกรอบรอบใบหน้าและอวัยวะอื่น ๆ 

    # แสดงผลเฟรม
    cv2.imshow('frame', frame) # แสดงผลเฟรมที่ผ่านการตรวจจับ

    # กด 'e' เพื่อออกจากลูป
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# ปิดการใช้งานกล้องและหน้าต่าง

cap.release() # ปิดกล้อง
cv2.destroyAllWindows() # ปิดหน้าต่างแสดงผลทั้งหมด
